# 檔案結構說明

## 完整目錄樹

```
climate-dashboard/
│
├── index.html                      # 主頁面 HTML 檔案
│                                   # 包含所有必要的 Meta 標籤和資源連結
│
├── assets/                         # 靜態資源目錄
│   ├── index-CKNiWqYD.css         # 編譯後的 CSS 樣式表
│   │                              # 包含 Tailwind CSS 和所有組件樣式
│   │
│   └── index-BVs_FjsB.js          # 編譯後的 JavaScript 程式碼
│                                  # 包含 React、Recharts 和應用邏輯
│
├── __manus__/                      # Manus 平台特定檔案（可選）
│   └── debug-collector.js          # 調試工具
│
├── README.md                       # 專案說明文件
│                                  # 包含功能介紹和使用方式
│
├── DEPLOYMENT.md                   # GitHub Pages 部署指南
│                                  # 詳細的部署步驟和常見問題
│
├── STRUCTURE.md                    # 此檔案
│                                  # 檔案結構說明
│
└── .gitignore                      # Git 忽略清單
                                   # 指定不需要上傳到 Git 的檔案
```

## 各檔案說明

### index.html (360 KB)
- **用途**：主頁面入口
- **內容**：
  - HTML 結構
  - Meta 標籤（標題、描述、視口設定等）
  - CSS 和 JavaScript 資源連結
  - React 應用掛載點（`<div id="root"></div>`）
- **特點**：完全自包含，無需額外依賴

### assets/index-*.css (113 KB)
- **用途**：樣式表
- **內容**：
  - Tailwind CSS 基礎樣式
  - 所有 React 組件的樣式
  - 響應式設計規則
  - 深色模式支援
- **壓縮**：已最小化和 gzip 壓縮

### assets/index-*.js (1.0 MB)
- **用途**：應用程式邏輯
- **內容**：
  - React 19 框架
  - 所有 React 組件
  - Recharts 圖表庫
  - 氣候數據（內嵌 JSON）
  - UI 交互邏輯
- **壓縮**：已最小化和 gzip 壓縮

### __manus__/debug-collector.js
- **用途**：開發工具（可選）
- **說明**：Manus 平台的調試工具，可安全刪除

### README.md
- **用途**：專案文件
- **內容**：
  - 功能特性說明
  - 技術堆疊
  - 支援的測站清單
  - 使用方式

### DEPLOYMENT.md
- **用途**：部署指南
- **內容**：
  - GitHub Pages 部署步驟
  - 常見問題解答
  - 自訂網域設定
  - 更新方式

### .gitignore
- **用途**：Git 配置
- **內容**：
  - 忽略 node_modules
  - 忽略 IDE 配置
  - 忽略構建檔案
  - 忽略環境變數

## 部署到 GitHub Pages

### 最小必要檔案

要使網頁在 GitHub Pages 上正常運作，**必須**包含：

1. ✅ `index.html` - 主頁面
2. ✅ `assets/` 目錄及其所有檔案
3. ✅ `.gitignore` - 推薦但非必須

### 可選檔案

以下檔案可選，但推薦包含以提供更好的文件：

- `README.md` - 專案說明
- `DEPLOYMENT.md` - 部署指南
- `STRUCTURE.md` - 此檔案

### 可刪除檔案

以下檔案可安全刪除：

- `__manus__/` - Manus 平台特定檔案

## 檔案大小

| 檔案 | 大小 | 壓縮後 |
|------|------|--------|
| index.html | 360 KB | 105 KB |
| index-*.css | 113 KB | 17.8 KB |
| index-*.js | 1.0 MB | 295 KB |
| **總計** | **1.5 MB** | **418 KB** |

## 資源載入流程

1. 瀏覽器請求 `index.html`
2. 瀏覽器解析 HTML，發現 CSS 和 JS 資源
3. 瀏覽器並行載入 `assets/index-*.css` 和 `assets/index-*.js`
4. CSS 應用到頁面
5. JavaScript 執行，React 應用啟動
6. React 渲染 UI 組件
7. 使用者可以與應用交互

## 跨域資源共享 (CORS)

此應用完全自包含，**無需**任何跨域資源：

- ✅ 所有資源都在本地
- ✅ 無外部 API 呼叫
- ✅ 無 CORS 問題
- ✅ 完全離線可用

## 瀏覽器相容性

支援所有現代瀏覽器：

- Chrome/Edge 90+
- Firefox 88+
- Safari 14+
- Opera 76+

## 效能最佳化

此應用已進行以下最佳化：

- ✅ 代碼最小化
- ✅ Gzip 壓縮
- ✅ 樹搖優化 (Tree-shaking)
- ✅ 代碼分割
- ✅ 資源內嵌

## 安全性

此應用：

- ✅ 無後端伺服器
- ✅ 無資料庫連接
- ✅ 無用戶認證
- ✅ 無敏感資訊
- ✅ 完全靜態

## 更新方式

要更新已發布的應用：

1. 修改本地檔案
2. 重新構建（如果使用原始碼）
3. 將新檔案推送到 GitHub
4. GitHub Pages 自動重新部署（通常 1-2 分鐘）

## 常見問題

### Q: 為什麼 JS 檔案這麼大？

A: 因為它包含了：
- React 框架
- Recharts 圖表庫
- 所有氣候數據
- 所有應用邏輯

所有這些都已最小化和壓縮。

### Q: 我可以刪除 __manus__ 目錄嗎？

A: 可以。它只是開發工具，不影響應用運作。

### Q: 我可以修改 HTML 檔案嗎？

A: 可以修改 `<title>` 和 `<meta>` 標籤，但不建議修改其他部分，因為可能破壞應用。

### Q: 如何自訂網頁標題？

A: 編輯 `index.html` 中的 `<title>` 標籤。

## 支援

如有任何問題，請參考：
- `README.md` - 功能說明
- `DEPLOYMENT.md` - 部署指南
- GitHub Pages 官方文件：https://docs.github.com/en/pages
