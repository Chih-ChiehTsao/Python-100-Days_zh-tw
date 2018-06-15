## Web前端概述

### HTML簡史

1. 1991年10月：一個非正式CERN（[歐洲核子研究中心](https://zh.wikipedia.org/wiki/%E6%AD%90%E6%B4%B2%E6%A0%B8%E5%AD%90%E7%A0%94%E7%A9%B6%E7%B5%84%E7%B9%94)）文件首次公開18個HTML標簽，這個文件的作者是物理學家[蒂姆·伯納斯-李](https://zh.wikipedia.org/wiki/%E8%92%82%E5%A7%86%C2%B7%E4%BC%AF%E7%BA%B3%E6%96%AF-%E6%9D%8E)，因此他是[萬維網](https://zh.wikipedia.org/wiki/%E4%B8%87%E7%BB%B4%E7%BD%91)的發明者，也是[萬維網聯盟](https://zh.wikipedia.org/wiki/%E4%B8%87%E7%BB%B4%E7%BD%91%E8%81%94%E7%9B%9F)的主席。
2. 1995年11月：HTML 2.0標準發布（RFC 1866）。
3. 1997年1月：HTML 3.2作爲[W3C](https://zh.wikipedia.org/wiki/W3C)推薦標準發布。
4. 1997年12月：HTML 4.0作爲W3C推薦標準發布。
5.  1999年12月：HTML4.01作爲W3C推薦標準發布。
6. 2008年1月：HTML5由W3C作爲工作草案發布。
7. 2011年5月：W3C將HTML5推進至“最終征求”（Last Call）階段。
8. 2012年12月：W3C指定HTML5作爲“候選推薦”階段。
9. 2014年10月：HTML5作爲穩定W3C推薦標準發布，這意味著HTML5的標準化已經完成。

#### HTML5新特性

1. 引入原生多媒體支持（audio和video標簽）
2. 引入可編程內容（canvas標簽）
3. 引入語義Web（article、aside、details、figure、footer、header、nav、section、summary等標簽）
4. 引入新的表單控件（日曆、郵箱、搜索等）
5. 引入對離線存儲更好的支持
6. 引入對定位、拖放、WebSocket、後台任務等的支持

### 使用標簽承載內容

####  結構

- head
  - title
  - meta
- body

#### 文本

- 標題和段落
- 粗體和斜體
- 上標和下標
- 空白（白色空間折疊）
- 折行和水平標尺
- 語義化標記
  - 加粗和強調
  - 引用
  - 縮寫詞和首字母縮寫詞
  - 引文
  - 所有者聯係信息
  - 內容的修改

#### 列表（list）

 - 有序列表（ordered list）
 - 無序列表（unordered list）
 - 定義列表（definition list）

#### 鏈接（anchor）

- 頁面鏈接
- 錨鏈接
- 功能鏈接

#### 圖像（image）

- 圖像存儲位置
- 圖像及其寬高
- 選擇正確的圖像格式
  - JPEG
  - GIF
  - PNG
- 矢量圖
- figure標簽

#### 表格（table）

- 基本的表格結構
- 表格的標題
- 跨行和跨列
- 長表格

#### 表單（form）

- 如何收集信息
- 表單控件（input）
  - 文本框 / 密碼框 / 文本域
  - 單選按鈕 / 複選按鈕 / 下拉列表
  - 提交按鈕 / 圖像按鈕 / 文件上傳
- 組合表單元素
  - fieldset / legend
- HTML5的表單控件
  - 日期
  - 電子郵件 / URL
  - 搜索

#### 音視頻（audio / video）

- 視頻格式和播放器
- 視頻托管服務
- 添加視頻的準備工作
- video標簽和屬性
- audio標簽和屬性

#### 其他

- 文檔類型
- 注釋
- 屬性
  - id
  - class
- 塊級元素 / 行級元素
- 內聯框架（internal frame）
- 頁面信息（meta）
- 轉義字符（實體替換符）

### 使用CSS渲染頁面

#### 簡介

- CSS的作用
- CSS的工作原理
- 規則、屬性和值

#### 顔色（color）

- 如何指定顔色
- 顔色術語和顔色對比
- 背景色

#### 文本（text / font）

- 文本的大小和字型(font-size / font-family)
- 斜體、粗體、大寫和下劃線(font-weight / font-style / text-decoration)
- 行間距(line-height)、字母間距(letter-spacing)和單詞間距(word-spacing)
- 對齊(text-align)方式和縮進(text-ident)
- 鏈接樣式（:link / :visited / :active / :hover）
- CSS3新屬性
  - 投影
  - 首字母和首行文本(p:first-letter / p:first-line)
  - 響應用戶

#### 盒子（box model）

- 盒子大小的控制（width / height）
- 盒子的邊框、外邊距和內邊距（border /  margin / padding）
- 盒子的顯示和隱藏（display / visibility）
- CSS3新屬性
  - 邊框圖像（border-image）
  - 投影（border-shadow）
  - 圓角（border-radius）

#### 列表、表格和表單

- 列表的項目符號（list-style）
- 表格的邊框和背景（border-collapse）
- 表單控件的外觀
- 表單控件的對齊
- 浏覽器的開發者工具

#### 圖像

- 控制圖像的大小（display: inline-block）
- 對齊圖像
- 背景圖像（background / background-image / background-repeat / background-position）

#### 布局

- 控制元素的位置（position / z-index）
  - 普通流
  - 相對定位
  - 絕對定位
  - 固定定位
  - 浮動元素（float / clear）
- 網站布局
  - HTML5布局
- 適配屏幕尺寸
  - 固定寬度布局
  - 流體布局
  - 布局網格

### 使用JavaScript控制行爲

#### JavaScript基本語法

- 語句和注釋
- 變量和數據類型
  - 聲明和賦值
  - 簡單數據類型和複雜數據類型
  - 變量的命名規則
- 表達式和運算符
  - 賦值運算符
  - 算術運算符
  - 比較運算符
  - 邏輯運算符
- 分支結構
  - if…else...
  - switch…case…default...
- 循環結構
  - for循環
  - while循環
  - do…while循環
- 數組
  - 創建數組
  - 操作數組中的元素
- 函數
  - 聲明函數
  - 調用函數
  - 參數和返回值
  - 匿名函數
  - 立即調用函數

#### 面向對象

 - 對象的概念
 - 創建對象的字面量語法
 - 訪問成員運算符
 - 創建對象的構造函數語法
    - this關鍵字
 - 添加和刪除屬性
    - delete關鍵字
 - 全局對象
    - Number / String / Boolean
    - Date / Math / RegEx / Array

#### BOM

 - window對象的屬性和方法
 - history對象
    - forward() / back() / go()
 - location對象
 - navigator對象
 - screen對象

#### DOM

 - DOM樹
 - 訪問元素
    - getElementById() / querySelector()
    - getElementsByClassName() / getElementsByTagName() / querySelectorAll()
    - parentNode / previousSibling / nextSibling / firstChild / lastChild
- 操作元素
  - nodeValue
  - innerHTML / textContent / createElement() / createTextNode() / appendChild() / removeChild()
  - className / id / hasAttribute() / getAttribute() / setAttribute() / removeAttribute()
- 事件處理
  - 事件類型
    - UI事件：load / unload / error / resize / scroll
    - 鍵盤事件：keydown / keyup / keypress
    - 鼠標事件：click / dbclick / mousedown / mouseup / mousemove / mouseover / mouseout
    - 焦點事件：focus / blur
    - 表單事件：input / change / submit / reset / cut / copy / paste / select
  - 事件綁定
    - HTML事件處理程序（不推薦使用，因爲要做到標簽與代碼分離）
    - 傳統的DOM事件處理程序（只能附加一個回調函數）
    - 事件監聽器（舊的浏覽器中不被支持）
  - 事件流：事件捕獲 / 事件冒泡
  - 事件對象（低版本IE中的window.event）
    - target（低版本IE中的srcElement）
    - type
    - cancelable
    - preventDefault()
    - stopPropagation()（低版本IE中的cancelBubble）
  - 鼠標事件 - 事件發生的位置
    - 屏幕位置：screenX和screenY
    - 頁面位置：pageX和pageY
    - 客戶端位置：clientX和clientY
  - 鍵盤事件 - 哪個鍵被按下了
    - keyCode屬性
    - String.fromCharCode(event.keyCode)
  - HTML5事件
    - DOMContentLoaded
    - hashchange
    - beforeunload

#### JavaScript API

- HTML5中的API：geolocation / localStorage / sessionStorage / history

### 使用jQuery

#### jQuery概述

1. Write Less Do More（用更少的代碼來完成更多的工作）
2. 使用CSS選擇器來查找元素（更簡單更方便）
3. 使用jQuery方法來操作元素（解決浏覽器兼容性問題、應用於所有元素並施加多個方法）

#### 引入jQuery

- 下載jQuery的開發版和壓縮版
- 從CDN加載jQuery

```HTML

<script src="https://cdn.bootcss.com/jquery/3.3.1/jquery.min.js"></script>
<script>
    window.jQuery || 
        document.write('<script src="js/jquery-3.3.1.min.js"></script>')
</script>
```

#### 查找元素

- 選擇器
  - \* / element / #id / .class / selector1, selector2
  - ancestor descendant / parent>child / previous+next / previous~siblings 
- 篩選器
  - 基本篩選器：:not(selector) / :first / :last / :even / :odd / :eq(index) / :gt(index) / :lt(index) / :animated / :focus
  - 內容篩選器：:contains('…') / :empty / :parent / :has(selector)
  - 可見性篩選器：:hidden / :visible
  - 子節點篩選器：:nth-child(expr) / :first-child / :last-child / :only-child
  - 屬性篩選器：[attribute] / [attribute='value'] / [attribute!='value'] / [attribute^='value'] / [attribute$='value'] / [attribute|='value'] / [attribute~='value']
- 表單：:input / :text / :password / :radio / :checkbox / :submit / :image / :reset / :button / :file / :selected / :enabled / :disabled / :checked

#### 執行操作

- 內容操作
  - 獲取/修改內容：html() / text() / replaceWith() / remove()
  - 獲取/設置元素：before() / after() / prepend() / append() / remove() / clone() / unwrap() / detach() / empty() / add()
  - 獲取/修改屬性：attr() / removeAttr() / addClass() / removeClass() / css()
  - 獲取/設置表單值：val()
- 查找操作
  - 查找方法：find() /  parent() / children() / siblings() / next() / nextAll() / prev() / prevAll()
  - 篩選器：filter() / not() / has() / is() / contains()
  - 索引編號：eq()
- 尺寸和位置
  - 尺寸相關：height() / width() / innerHeight() / innerWidth() / outerWidth() / outerHeight()
  - 位置相關：offset() / position() / scrollLeft() / scrollTop()
- 特效和動畫
  - 基本動畫：show() / hide() / toggle()
  - 消失出現：fadeIn() / fadeOut() / fadeTo() / fadeToggle()
  - 滑動效果：slideDown() / slideUp() / slideToggle()
  - 自定義：delay() / stop() / animate()
- 事件
  - 文檔加載：ready() / load()
  - 用戶交互：on() / off()

#### 鏈式操作

#### 檢測頁面是否可用

```HTML

<script>
    $(document).ready(function() {
        
    });
</script>
```

```HTML

<script>
    $(function() {
        
    });
</script>
```

#### jQuery插件

- jQuery Validation
- jQuery Treeview
- jQuery Autocomplete
- jQuery UI

#### 避免和其他庫的沖突

先引入其他庫再引入jQuery的情況。

```HTML

<script src="other.js"></script>
<script src="jquery.js"></script>
<script>
	jQuery.noConflict();
    jQuery(function() {
        jQuery('div').hide();
    });
</script>
```

先引入jQuery再引入其他庫的情況。

```HTML

<script src="jquery.js"></script>
<script src="other.js"></script>
<script>
    jQuery(function() {
        jQuery('div').hide();
    });
</script>
```

#### 使用Ajax

- 原生的Ajax
- 基於jQuery的Ajax
  - 加載內容
  - 提交表單

### 使用Bootstrap

#### 特點

1. 支持主流的浏覽器和移動設備
2. 容易上手
3. 響應式設計

#### 內容

1. 網格係統
2. 封裝的CSS
3. 現成的組件
4. JavaScript插件

