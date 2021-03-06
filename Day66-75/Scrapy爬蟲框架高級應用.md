## Scrapy爬蟲框架高級應用

### Spider的用法

在Scrapy框架中，我們自定義的蜘蛛都繼承自scrapy.spiders.Spider，這個類有一係列的屬性和方法，具體如下所示：

1. name：爬蟲的名字。
2. allowed_domains：允許爬取的域名，不在此範圍的鏈接不會被跟進爬取。
3. start_urls：起始URL列表，當我們沒有重寫start_requests()方法時，就會從這個列表開始爬取。
4. custom_settings：用來存放蜘蛛專屬配置的字典，這裏的設置會覆蓋全局的設置。
5. crawler：由from_crawler()方法設置的和蜘蛛對應的Crawler對象，Crawler對象包含了很多項目組件，利用它我們可以獲取項目的配置信息，如調用crawler.settings.get()方法。
6. settings：用來獲取爬蟲全局設置的變量。
7. start_requests()：此方法用於生成初始請求，它返回一個可疊代對象。該方法默認是使用GET請求訪問起始URL，如果起始URL需要使用POST請求來訪問就必須重寫這個方法。
8. parse()：當Response沒有指定回調函數時，該方法就會被調用，它負責處理Response對象並返回結果，從中提取出需要的數據和後續的請求，該方法需要返回類型爲Request或Item的可疊代對象（生成器當前也包含在其中，因此根據實際需要可以用return或yield來産生返回值）。
9. closed()：當蜘蛛關閉時，該方法會被調用，通常用來做一些釋放資源的善後操作。

### 中間件的應用

#### 下載中間件



#### 蜘蛛中間件



### Scrapy對接Selenium



### Scrapy部署到Docker

