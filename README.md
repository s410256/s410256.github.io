# 台灣氣候數據儀表板 (Taiwan Climate Data Dashboard)

一個互動式的氣候數據可視化網頁，展示台灣 22 個測站的完整氣象數據。

## 功能特性

- **22 個測站數據**：涵蓋台灣全島的氣象觀測站
- **五項氣象指標**：氣溫、雲量、日照時數、降水量-平均、降水量-中位數
- **互動式選擇器**：快速切換測站查看數據
- **多維度圖表**：折線圖和柱狀圖展示月度變化
- **完整數據表格**：詳細的月份數據一覽
- **響應式設計**：完美適配桌面和行動設備

## 部署到 GitHub Pages

### 方法 1：使用 GitHub 網頁介面

1. 在 GitHub 上建立新的 Repository（例如：`climate-dashboard`）
2. 將此資料夾中的所有檔案上傳到 Repository
3. 進入 Repository 設定 → Pages
4. 選擇 "Deploy from a branch"
5. 選擇 `main` 分支和 `/ (root)` 目錄
6. 儲存後，您的網頁將在 `https://[your-username].github.io/climate-dashboard` 發布

### 方法 2：使用 Git 命令列

```bash
# 初始化 Git 倉庫
git init
git add .
git commit -m "Initial commit: Climate Dashboard"

# 添加遠端倉庫
git remote add origin https://github.com/[your-username]/climate-dashboard.git

# 推送到 GitHub
git branch -M main
git push -u origin main
```

### 方法 3：使用 GitHub CLI

```bash
gh repo create climate-dashboard --public --source=. --remote=origin --push
```

## 檔案結構

```
├── index.html           # 主頁面 HTML
├── assets/              # 靜態資源（CSS、JavaScript）
│   ├── index-*.css      # 樣式表
│   └── index-*.js       # JavaScript 程式碼
└── README.md            # 此檔案
```

## 技術堆疊

- **React 19** - UI 框架
- **Tailwind CSS 4** - 樣式設計
- **Recharts** - 圖表庫
- **Vite** - 構建工具

## 數據來源

數據來自台灣中央氣象署（CWA）的氣象觀測站，統計期間為 1991-2020 年。

## 支援的測站

臺北、竹子湖、基隆、彭佳嶼、花蓮、蘇澳、宜蘭、東吉島、澎湖、臺南、高雄、嘉義、臺中、阿里山、大武、玉山、新竹、恆春、成功、蘭嶼、日月潭、臺東、梧棲

## 使用方式

1. 在下拉選單中選擇要查看的測站
2. 查看四個資訊卡片顯示的基本數據
3. 在圖表中觀察月度變化趨勢
4. 向下滾動查看完整的月份數據表格

## 瀏覽器支援

- Chrome/Edge (最新版本)
- Firefox (最新版本)
- Safari (最新版本)

## 授權

MIT License

## 聯絡方式

如有任何問題或建議，歡迎提出 Issue 或 Pull Request。
