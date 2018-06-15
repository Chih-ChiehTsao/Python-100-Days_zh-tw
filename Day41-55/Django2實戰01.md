## Django 2.x實戰(01) - 快速上手

Web開發的早期階段，開發者需要手動編寫每個頁面，例如一個新聞門戶網站，每天都要修改它的HTML頁面，這樣隨著網站規模和體量的增大，這種方式就變得極度糟糕。爲了解決這個問題，開發人員想到了用外部程序來爲Web服務器生成動態內容，也就是說HTML頁面以及頁面中的動態內容不再通過手動編寫而是通過程序自動生成。最早的時候，這項技術被稱爲CGI（公共網關接口），當然隨著時間的推移，CGI暴露出的問題也越來越多，例如大量重複的樣板代碼，總體性能較爲低下等，因此在呼喚新的英雄的時代，PHP、ASP、JSP這類Web應用開發技術在上世紀90年代中後期如雨後春筍般湧現。通常我們說的Web應用是指通過浏覽器來訪問網絡資源的應用程序，因爲浏覽器的普及性以及易用性，Web應用使用起來方便簡單，而且在應用更新時用戶通常不需要做任何的處理就能使用更新後的應用，而且也不用關心用戶到底用的是什麽操作係統，甚至不用區分是PC端還是移動端。

### Web應用機制和術語

下圖向我們展示了Web應用的工作流程，其中涉及到的術語如下表所示。

![](./res/web-application.png)

> 說明：相信有經驗的讀者會發現，這張圖中其實還少了很多東西，例如反向代理服務器、數據庫服務器、防火牆等，而且圖中的每個節點在實際項目部署時可能是一組節點組成的集群。當然，如果你對這些沒有什麽概念也不要緊，後續的課程中我們會爲大家進行講解。

| 術語          | 解釋                                                         |
| ------------- | ------------------------------------------------------------ |
| **URL/URI**   | 統一資源定位符/統一資源標識符，網絡資源的唯一標識            |
| **域名**      | 與Web服務器地址對應的一個易於記憶的字符串名字                |
| **DNS**       | 域名解析服務，可以將域名轉換成對應的IP地址                   |
| **IP地址**    | 網絡上的主機的身份標識，通過IP地址可以區分不同的主機         |
| **HTTP**      | 超文本傳輸協議，應用層協議，萬維網數據通信的基礎             |
| **反向代理**  | 代理客戶端向服務器發出請求，然後將服務器返回的資源返回給客戶端 |
| **Web服務器** | 接受HTTP請求，然後返回HTML文件、純文本文件、圖像等資源給請求者 |
| **Nginx**     | 高性能的Web服務器，也可以用作[反向代理](https://zh.wikipedia.org/wiki/%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86)，[負載均衡](https://zh.wikipedia.org/wiki/%E8%B4%9F%E8%BD%BD%E5%9D%87%E8%A1%A1) 和 [HTTP緩存](https://zh.wikipedia.org/wiki/HTTP%E7%BC%93%E5%AD%98) |

#### HTTP協議

這裏我們稍微費一些筆墨來談談上面提到的HTTP。HTTP（超文本傳輸協議）是構建於TCP（傳輸控制協議）之上應用級協議，它利用了TCP提供的可靠的傳輸服務實現了Web應用中的數據交換。按照維基百科上的介紹，設計HTTP最初的目的是爲了提供一種發布和接收[HTML](https://zh.wikipedia.org/wiki/HTML)頁面的方法，也就是說這個協議是浏覽器和Web服務器之間傳輸的數據的載體。關於這個協議的詳細信息以及目前的發展狀況，大家可以閱讀阮一峰老師的[《HTTP 協議入門》](http://www.ruanyifeng.com/blog/2016/08/http.html)、[《互聯網協議入門》](http://www.ruanyifeng.com/blog/2012/05/internet_protocol_suite_part_i.html)係列以及[《圖解HTTPS協議》](http://www.ruanyifeng.com/blog/2014/09/illustration-ssl.html)進行了解，下圖是我於2009年9月10日淩晨4點在四川省網絡通信技術重點實驗室用開源協議分析工具Ethereal（抓包工具WireShark的前身）截取的訪問百度首頁時的HTTP請求和響應的報文（協議數據），由於Ethereal截取的是經過網絡適配器的數據，因此可以清晰的看到從物理鏈路層到應用層的協議數據。

HTTP請求（請求行+請求頭+空行+[消息體]）：

![](./res/http-request.png)

HTTP響應（響應行+響應頭+空行+消息體）：

![](./res/http-response.png)

>  說明：但願這兩張如同泛黃的照片般的截圖幫助你大概的了解到HTTP是一個怎樣的協議。

### Django概述

Python的Web框架有上百個，比它的關鍵字還要多。所謂Web框架，就是用於開發Web服務器端應用的基礎設施（通常指封裝好的模塊和一係列的工具）。事實上，即便沒有Web框架，我們仍然可以通過socket或[CGI](https://zh.wikipedia.org/wiki/%E9%80%9A%E7%94%A8%E7%BD%91%E5%85%B3%E6%8E%A5%E5%8F%A3)來開發Web服務器端應用，但是這樣做的成本和代價在實際開發中通常是不能接受的。通過Web框架，我們可以化繁爲簡，同時降低創建、更新、擴展應用程序的工作量。Python的Web框架中比較有名的有：Flask、Django、Tornado、Pyramid、Bottle、Web2py、web.py等。

在基於Python的Web框架中，Django是所有重量級選手中最有代表性的一位，開發者可以基於Django快速的開發可靠的Web應用程序，因爲它減少了Web開發中不必要的開銷，對常用的設計和開發模式進行了封裝，並對MVC架構提供了支持（MTV）。許多成功的網站和App都是基於Django框架構建的，國內比較有代表性的網站包括：知乎、豆瓣網、果殼網、搜狐閃電郵箱、101圍棋網、海報時尚網、背書吧、堆糖、手機搜狐網、咕咚、愛福窩、果庫等。

![](./res/mvc.png)

Django誕生於2003年，它是一個在真正的應用中成長起來的項目，由勞倫斯出版集團旗下在線新聞網站的內容管理係統（CMS）研發團隊編寫（主要是Adrian Holovaty和Simon Willison），以比利時的吉普賽爵士吉他手Django Reinhardt來命名，在2005年夏天作爲開源框架發布。使用Django能用很短的時間構建出功能完備的網站，因爲它代替程序員完成了所有乏味和重複的勞動，剩下真正有意義的核心業務給程序員，這一點就是對DRY（Don't Repeat Yourself）理念的最好踐行。

### 快速上手

#### 準備工作

1. 檢查Python環境：Django 1.11需要Python 2.7或Python 3.4以上的版本；Django 2.0需要Python 3.4以上的版本。

   ```Shell
   $ python3 --version
   ```

   ```Shell
   $ python3
   >>> import sys
   >>> sys.version
   >>> sys.version_info
   ```

2. 創建項目文件夾並切換到該目錄，例如我們要實例一個OA（辦公自動化）項目。

   ```Shell
   $ mkdir oa
   $ cd oa
   ```

3. 創建並激活虛擬環境。

   ```Shell
   $ python3 -m venv venv
   $ source venv/bin/activate
   ```
   > 注意：Windows係統下是執行`venv/Scripts/activate.bat`批處理文件。

4. 更新包管理工具pip。

   ```Shell
   (venv)$ python -m pip install --upgrade pip
   ```
   > 注意：請注意終端提示符發生的變化，前面的`(venv)`說明我們已經進入虛擬環境，而虛擬環境下的python和pip已經是Python 3的解釋器和包管理工具了。

5. 安裝Django。

   ```Shell
   (venv)$ pip install django
   ```

   或指定版本號來安裝對應的Django的版本。

   ```Shell
   (venv)$ pip install django==1.11
   ```

6. 檢查Django的版本。

   ```Shell
   (venv)$ python -m django --version
   (venv)$ django-admin --version
   ```

   ```Shell
   (venv)$ python
   >>> import django
   >>> django.get_version()
   ```
   下圖展示了Django版本和Python版本的對應關係，在我們的項目中我們選擇了最新的Django 2.0的版本。

   | Django版本 | Python版本              |
   | ---------- | ----------------------- |
   | 1.8        | 2.7、3.2、3.3、3.4、3.5 |
   | 1.9、1.10  | 2.7、3.4、3.5           |
   | 1.11       | 2.7、3.4、3.5、3.6      |
   | 2.0        | 3.4、3.5、3.6           |

   > 說明：在創建這篇文章時Django 2.1版本尚未正式發布，因此我們的教程使用了2.0.5版本。

7. 使用`django-admin`創建項目，項目命名爲oa。

   ```Shell
   (venv)$ django-admin startproject oa .
   ```

   > 注意：上面的命令最後的那個點，它表示在當前路徑下創建項目。

   執行上面的命令後看看生成的文件和文件夾，它們的作用如下所示：

   - `manage.py`： 一個讓你用各種方式管理 Django 項目的命令行工具。
   - `oa/__init__.py`：一個空文件，告訴 Python 這個目錄應該被認爲是一個 Python 包。
   - `oa/settings.py`：Django 項目的配置文件。
   - `oa/urls.py`：Django 項目的 URL 聲明，就像你網站的“目錄”。
   - `oa/wsgi.py`：作爲你的項目的運行在 WSGI 兼容的Web服務器上的入口。

8. 啓動服務器運行項目。

   ```Shell
   (venv)$ python manage.py runserver
   ```

   在浏覽器中輸入<http://127.0.0.1:8000>訪問我們的服務器，效果如下圖所示。

   ![](./res/django-index-1.png)


   > 說明1：剛剛啓動的是Django自帶的用於開發和測試的服務器，它是一個用純Python編寫的輕量級Web服務器，但它並不是真正意義上的生産級別的服務器，千萬不要將這個服務器用於和生産環境相關的任何地方。

   > 說明2：用於開發的服務器在需要的情況下會對每一次的訪問請求重新載入一遍Python代碼。所以你不需要爲了讓修改的代碼生效而頻繁的重新啓動服務器。然而，一些動作，比如添加新文件，將不會觸發自動重新加載，這時你得自己手動重啓服務器。

   > 說明3：可以通過`python manage.py help`命令查看可用命令列表；在啓動服務器時，也可以通過`python manage.py runserver 1.2.3.4:56789`來指定綁定的IP地址和端口。

   > 說明4：可以通過Ctrl+C來終止服務器的運行。

9. 接下來我們進入項目目錄oa並修改配置文件settings.py，Django是一個支持國際化和本地化的框架，因此剛才我們看到的默認首頁也是支持國際化的，我們將默認語言修改爲中文，時區設置爲東八區。

   ```Shell
   (venv)$ cd oa
   (venv)$ vim settings.py
   ```

   ```Python
   # 此處省略上面的內容
   
   # 設置語言代碼
   LANGUAGE_CODE = 'zh-hans'
   # 設置時區
   TIME_ZONE = 'Asia/Chongqing'
   
   # 此處省略下面的內容
   ```

10. 回到manage.py所在的目錄，刷新剛才的頁面。

  ```Shell
  (venv)$ cd ..
  (venv)$ python manage.py runserver
  ```

  ![](./res/django-index-2.png)

#### 動態頁面

1. 創建名爲hrs（人力資源係統）的應用（注：一個項目可以包含多個應用）。

   ```Shell
   (venv)$ python manage.py startapp hrs
   ```

   執行上面的命令會在當前路徑下創建hrs目錄，其目錄結構如下所示：

   - `__init__.py`：一個空文件，告訴 Python 這個目錄應該被認爲是一個 Python 包。
   - `admin.py`：可以用來注冊模型，讓Django自動創建管理界面。
   -  `apps.py`：當前應用的配置。
   - `migrations`：存放與模型有關的數據庫遷移信息。
     - `__init__.py`：一個空文件，告訴 Python 這個目錄應該被認爲是一個 Python 包。
   - `models.py`：存放應用的數據模型，即實體類及其之間的關係（MVC/MVT中的M）。
   - `tests.py`：包含測試應用各項功能的測試類和測試函數。
   - `views.py`：處理請求並返回響應的函數（MVC中的C，MVT中的V）。
2. 進入應用目錄修改視圖文件views.py。

   ```Shell
   (venv)$ cd hrs
   (venv)$ vim views.py
   ```

   ```Python
   from django.http import HttpResponse
   
   
   def index(request):
       return HttpResponse('<h1>Hello, Django!</h1>')
   
   ```

3. 在應用目錄創建一個urls.py文件並映射URL。

   ```Shell
   (venv)$ touch urls.py
   (venv)$ vim urls.py
   ```

   ```Python
   from django.urls import path
   
   from hrs import views
   
   urlpatterns = [
       path('', views.index, name='index'),
   ]
   ```
   > 說明：上面使用的path函數是Django 2.x中新添加的函數，除此之外還有re_path是支持正則表達式的URL映射函數；Django 1.x中是用url函數來設定URL映射。

4. 切換到項目目錄，修改該目錄下的urls.py文件，對應用中設定的URL進行合並。

   ```Shell
   (venv) $ cd ..
   (venv) $ cd oa
   (venv) $ vim urls.py
   ```

   ```Python
   from django.contrib import admin
   from django.urls import path, include
   
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('hrs/', include('hrs.urls')),
   ]
   ```

5. 啓動項目並訪問應用。

   ```Shell
   (venv)$ cd ..
   (venv)$ python manage.py runserver
   ```

   在浏覽器中訪問<http://localhost:8000/hrs>。

   > 說明：如果想實現遠程訪問，需要先確認防火牆是否已經打開了8000端口，而且需要在配置文件settings.py中修改ALLOWED_HOSTS的設置，添加一個'*'表示允許所有的客戶端訪問Web應用。

6. 修改views.py生成動態內容。

   ```Shell
   (venv)$ cd hrs
   (venv)$ vim views.py
   ```

   ```Python
   from django.http import HttpResponse
   
   from io import StringIO
   from random import randrange
   
   fruits = ['蘋果', '草莓', '榴蓮', '香蕉', '葡萄', '山竹', '藍莓', '西瓜']
   
   
   def index(request):
       output = StringIO()
       output.write('<html>\n')
       output.write('<head>\n')
       output.write('\t<meta charset="utf-8">\n')
       output.write('\t<title>首頁</title>')
       output.write('</head>\n')
       output.write('<body>\n')
       output.write('\t<h1>Hello, world!</h1>\n')
       output.write('\t<hr>\n')
       output.write('\t<ol>\n')
       for _ in range(3):
           rindex = randrange(0, len(fruits))
           output.write('\t\t<li>' + fruits[rindex]  + '</li>\n')
       output.write('\t</ol>\n')
       output.write('</body>\n')
       output.write('</html>\n')
       return HttpResponse(output.getvalue())
   
   ```

#### 使用視圖模板

上面通過拼接HTML代碼的方式生成動態視圖的做法在實際開發中是無能接受的，這一點我相信是不言而喻的。爲了解決這個問題，我們可以提前準備一個模板頁，所謂模板頁就是一個帶占位符的HTML頁面，當我們將程序中獲得的數據替換掉頁面中的占位符時，一個動態頁面就産生了。

我們可以用Django框架中template模塊的Template類創建模板對象，通過模板對象的render方法實現對模板的渲染。所謂的渲染就是用數據替換掉模板頁中的占位符，Django框架通過shortcuts模塊的快捷函數render簡化了渲染模板的操作，具體的用法如下所示。

1. 先回到manage.py文件所在的目錄創建一個templates文件夾。

   ```Shell
   (venv)$ cd ..
   (venv)$ mkdir templates
   (venv)$ cd templates
   ```

2. 創建模板頁index.html。

   ```Shell
   (venv)$ touch index.html
   (venv)$ vim index.html
   ```
   ```HTML
   <!DOCTYPE html>
   <html lang="en">
   <head>
   	<meta charset="UTF-8">
   	<title>首頁</title>
   </head>
   <body>
   	<h1>{{ greeting }}</h1>
   	<hr>
   	<h3>今天推薦{{ num }}種水果是:</h3>
   	<ul>
   		{% for fruit in fruits %}
   		<li>{{ fruit }}</li>
   		{% endfor %}
   	</ul>
   </body>
   </html>
   ```
   注意在模板頁中我們使用了`{{ greeting }}`這樣的模板占位符語法，也使用了`{% for %}`這樣的模板指令，如果對此不熟悉並不要緊，我們會在後續的內容中進一步的講解模板的用法。

3. 回到應用目錄，修改views.py文件。

   ```Shell
   (venv)$ cd ..
   (venv)$ cd hrs
   (venv)$ vim views.py
   ```

   ```Python
   from django.shortcuts import render
   from random import randrange
   
   
   def index(request):
       fruits = ['蘋果', '香蕉', '草莓', '葡萄', '山竹', '楊梅', '西瓜', '榴蓮']
       start, end = 0, randrange(len(fruits))
       ctx = {
           'greeting': 'Hello, Django!',
           'num': end + 1,
           'fruits': fruits[start:end + 1]
       }
       return render(request, 'index.html', ctx)
   
   ```

   到此爲止，我們還沒有辦法讓views.py中的render函數找到模板文件index.html，爲此我們需要修改settings.py文件，配置模板文件所在的路徑。

4. 切換到項目目錄修改settings.py文件。

   ```Shell
   (venv)$ cd ..
   (venv)$ cd oa
   (venv)$ vim settings.py
   ```

   ```Python
   # 此處省略上面的內容
   
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'APP_DIRS': True,
           'OPTIONS': {
               'context_processors': [
                   'django.template.context_processors.debug',
                   'django.template.context_processors.request',
                   'django.contrib.auth.context_processors.auth',
                   'django.contrib.messages.context_processors.messages',
               ],
           },
       },
   ]
   
   # 此處省略下面的內容
   ```

5. 重新運行項目並查看結果。

   ```Shell
   (venv)$ cd ..
   (venv)$ python manage.py runserver
   ```

   ![](./res/runserver.png)

### 總結

至此，我們已經利用Django框架完成了一個非常小的Web應用，雖然它並沒有任何的實際價值，但是我們需要通過這個項目了解到Django框架的使用方式。當然，如果使用PyCharm的Professional版本，也可以通過PyCharm的創建項目的選項直接創建Django項目，使用PyCharm的好處在於編寫代碼時可以獲得代碼提示、錯誤修複、自動導入等功能，從而提升開發效率，但是代價是需要支付對應的費用才能使用專業版的PyCharm，社區版的PyCharm中並未包含對Web框架的支持。

此外，學習Django最好的資料肯定是它的[官方文檔](https://docs.djangoproject.com/zh-hans/2.0/)，除此之外圖靈社區最近出版的[《Django基礎教程》](http://www.ituring.com.cn/book/2630)也是非常適合初學者的讀物。 