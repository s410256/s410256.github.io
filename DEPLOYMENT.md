# GitHub Pages 部署指南

## 快速開始

### 步驟 1：建立 GitHub Repository

1. 登入 GitHub 帳戶
2. 點擊右上角的 "+" 圖示，選擇 "New repository"
3. Repository 名稱：`climate-dashboard`
4. 選擇 "Public"
5. 點擊 "Create repository"

### 步驟 2：上傳檔案

#### 方式 A：使用 GitHub 網頁介面（最簡單）

1. 在新建的 Repository 頁面，點擊 "uploading an existing file"
2. 將此資料夾中的所有檔案拖曳到上傳區域
3. 或點擊 "choose your files" 逐個選擇
4. 點擊 "Commit changes"

#### 方式 B：使用 Git 命令列

```bash
# 在此資料夾中執行
cd climate-dashboard

# 初始化 Git
git init
git add .
git commit -m "Initial commit: Taiwan Climate Data Dashboard"

# 添加遠端倉庫（將 YOUR_USERNAME 替換為您的 GitHub 用戶名）
git remote add origin https://github.com/YOUR_USERNAME/climate-dashboard.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 步驟 3：啟用 GitHub Pages

1. 進入 Repository 頁面
2. 點擊 "Settings"（設定）
3. 左側選單選擇 "Pages"
4. 在 "Source" 下選擇：
   - Branch: `main`
   - Folder: `/ (root)`
5. 點擊 "Save"

### 步驟 4：等待部署

- GitHub 會自動部署您的網頁
- 部署完成後，您會看到一個綠色的勾選標記
- 您的網頁將在以下地址發布：
  ```
  https://YOUR_USERNAME.github.io/climate-dashboard
  ```

## 常見問題

### Q: 我的網頁無法正常顯示？

A: 請確認：
1. Repository 名稱是否正確
2. 所有檔案是否已上傳（特別是 `index.html` 和 `assets/` 資料夾）
3. 是否已在 Settings → Pages 中啟用 GitHub Pages
4. 瀏覽器快取是否已清除（按 Ctrl+Shift+Delete）

### Q: 部署需要多長時間？

A: 通常 1-2 分鐘，但有時可能需要 5-10 分鐘。您可以在 Repository 的 "Actions" 標籤中查看部署進度。

### Q: 我可以使用自訂網域嗎？

A: 可以。在 Settings → Pages 中的 "Custom domain" 欄位輸入您的網域名稱，然後按照指示更新 DNS 記錄。

### Q: 如何更新已發布的網頁？

A: 只需將新檔案推送到 GitHub，GitHub Pages 會自動重新部署。

## 檔案清單

確保以下檔案已上傳到 Repository：

```
climate-dashboard/
├── index.html              # 主頁面
├── assets/
│   ├── index-*.css         # 樣式表
│   └── index-*.js          # JavaScript
├── README.md               # 專案說明
├── DEPLOYMENT.md           # 此檔案
└── .gitignore              # Git 忽略清單
```

## 技術詳情

- **靜態網站**：無需後端伺服器
- **完全離線**：所有資料都內嵌在 HTML 中
- **瀏覽器相容性**：支援所有現代瀏覽器
- **檔案大小**：約 1.5 MB（包括所有資源）

## 支援

如有任何問題，請：
1. 檢查 GitHub Pages 文件：https://docs.github.com/en/pages
2. 查看 Repository 的 "Actions" 標籤中的部署日誌
3. 在 Repository 中提出 Issue

祝您使用愉快！
