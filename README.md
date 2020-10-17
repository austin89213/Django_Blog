# 描述:
主要以 CBV 建構簡易的部落格來展現 Django 框架基本的 CRUD 技術，並進行異步處理以及D3.js的繪圖製作。

# 功能:
- User:
   - 註冊 (註冊後為一般使用者)
   - 登入 (登入後才可以進行發文)
   - Admin連結 (須以Superuser登入才會出現在Navbar)
- Posts:
   - 發文 (需登入，作者自動設定為當前使用者。若未登入，將導向至登入頁面)
   - 編輯與刪除 (需登入且使用者必須為該文章作者)
   - 記錄文章被點擊次數
   - 點選文章中 Analysis 按鈕可查看相關圖表
- Comments:
   - 可於文章中發表評論
   - 若當前使用者為登入狀態，評論者將自動設定為當前使用
   - 若未登入，評論者將自動設定為匿名使用者
- Asynchronous:
   - 將 AJAX 運用於評論功能 (發表後將自動新增評論，無需刷新頁面)
- D3.js:
   - 運用 D3.js 繪製出圓餅圖，觀測該文章被點閱次數以及留言次數之間的比較
- NAVBAR:
   - 當前路徑之連結顏色較深，以提升使用者體驗

# 技術與工具：

- 後端:
   - [Django (3.0.3)] (https://www.djangoproject.com/)
- 前端:
   - [Bootstrap (4)] (https://getbootstrap.com/)
   - [jQuery (3.5)] (https://jquery.com/)
   - [D3.js (6.2)] (https://d3js.org/)


# 使用:
- 1. 使用 git clone https://github.com/austin89213/Django_Blog 或是直接下載此份專案之壓縮檔使用
- 2. 建立虛擬環境並安裝 Python 3 以及 Django
- 3. Termianl / Command Line 移動至 Django_Blog 主目錄
- 4. 執行 python manage.py createsuperuser 建立 superuser 並用其登入
- 5. 執行 python manage.py runserver
- 6. 於瀏覽器中開起所給予的連結 (http://127.0.0.1:8000/)
