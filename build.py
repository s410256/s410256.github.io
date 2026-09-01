import json
import os
import shutil
import requests
import urllib3

# 關閉跳過 SSL 驗證時出現的警告訊息
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# 1. API 網址與設定
LIST_API = (
    "https://www.ylsh.ilc.edu.tw/ischool/widget/site_news/news_query_json.php"
)
DETAIL_API = (
    "https://www.ylsh.ilc.edu.tw/ischool/widget/site_news/news_pop_content.php"
)
DATA_FILE = "data.json"

# 2. 全校所有公告區塊 UID 對照表
CATEGORIES = {
    "重要公告": "WID_0_2_0bbe1df056daadf6ca89c11d5e6531eb7f4576e3",
    "榮譽榜": "WID_0_2_6f48a99edc0feabc2b1c3ecd9a4d027137825643",
    "不分類": "WID_0_2_b76d2bdd721a926a53c5dd1e50cef5d40a844666",
    "校內學習": "WID_0_2_494f7d063ea542fc0df8aa7399a7b6f65f4d47e1",
    "校外活動": "WID_0_2_51cfbb837570a73867e5b1005c5bab99613989e2",
    "高中入學": "WID_0_2_ed6ae557185d2e8f6280e253039a80de03f3c6c0",
    "大學升學": "WID_0_2_0b3d993b9858f030c657e25679be0e8af88d9013",
    "教職知能": "WID_0_2_ef4d53aa2964d44c698200b144e14ac6290f7f2b",
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
}


def main():
    # 3. 讀取歷史資料庫 (若不存在則建立空字典)
    db = {}
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, "r", encoding="utf-8") as f:
                db = json.load(f)
        except Exception as e:
            print(f"⚠️ 讀取 {DATA_FILE} 失敗，將重新初始化: {e}")

    new_count = 0

    # 4. 輪詢所有公告區塊
    for cat_name, uid in CATEGORIES.items():
        print(f"🔍 檢查區塊：[{cat_name}]")

        payload = {
            "field": "time",
            "order": "DESC",
            "pageNum": 0,
            "maxRows": 15,  # 定時檢查最新 15 筆即足夠
            "keyword": "",
            "fval": "",
            "flock": "",
            "uid": uid,
            "tf": "1",
            "auth_type": "user",
        }

        try:
            res = requests.post(
                LIST_API, headers=headers, data=payload, verify=False, timeout=10
            )
            if res.status_code != 200:
                print(f"  ❌ [{cat_name}] 列表 API 回應失敗 ({res.status_code})")
                continue

            raw_data = res.json()
            if not raw_data or len(raw_data) <= 1:
                continue

            # raw_data[0] 為元資料，真正公告從 index 1 開始
            articles = raw_data[1:]

            for item in articles:
                nid = str(item.get("newsId"))

                # 增量判斷：只對資料庫未記錄的 NID 發送內文請求
                if nid not in db:
                    print(
                        f"  🆕 發現新公告 NID [{nid}]: {item.get('title')[:15]}..."
                    )

                    detail_params = {"newsId": nid, "uid": uid}
                    content_html = "無內文說明"
                    files = []

                    try:
                        detail_res = requests.get(
                            DETAIL_API,
                            headers=headers,
                            params=detail_params,
                            verify=False,
                            timeout=10,
                        )
                        if detail_res.status_code == 200:
                            detail_data = detail_res.json()
                            content_html = detail_data.get("content", "無內文說明")
                            files = detail_data.get("files", [])
                    except Exception as e:
                        print(f"     ⚠️ 內文抓取失敗: {e}")

                    # 寫入資料庫
                    db[nid] = {
                        "nid": nid,
                        "category": cat_name,
                        "title": item.get("title"),
                        "date": item.get("time"),
                        "unit": item.get("unit_name") or "全校",
                        "clicks": item.get("clicks"),
                        "content": content_html,
                        "files": files,
                    }
                    new_count += 1
                else:
                    # 舊公告同步更新動態的點閱數與類別標籤
                    db[nid]["clicks"] = item.get("clicks")
                    db[nid]["category"] = cat_name

        except Exception as e:
            print(f"  ❌ [{cat_name}] 處理發生例外錯誤: {e}")

    print(
        f"\n✅ 同步完成！新增 {new_count} 筆公告，資料庫總累積共 {len(db)} 筆。"
    )

    # 5. 寫回 data.json 歷史資料庫
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

    # 6. 打包產物至 dist/ 目錄供 GitHub Pages 部署
    os.makedirs("dist", exist_ok=True)

    # 複製壓縮版 data.json 到 dist/
    with open("dist/data.json", "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False)

    # 複製前端 index.html 到 dist/
    if os.path.exists("index.html"):
        shutil.copy("index.html", "dist/index.html")
        print("📦 成功打包 dist/index.html 與 dist/data.json！")
    else:
        print("⚠️ 警告：根目錄找不到 index.html，請補上前端網頁檔案。")


if __name__ == "__main__":
    main()