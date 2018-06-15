## 玩轉PyCharm(上)

PyCharm是由JetBrains公司開發的提供給Python專業的開發者的一個集成開發環境，它最大的優點是能夠大大提升Python開發者的工作效率，爲開發者集成了很多用起來非常順手的功能，包括代碼調試、高亮語法、代碼跳轉、智能提示、自動補全、單元測試、版本控制等等。此外，PyCharm還提供了對一些高級功能的支持，包括支持基於Django框架的Web開發、。

### PyCharm的安裝

可以在[JetBrains公司的官方網站]()找到PyCharm的[下載鏈接](https://www.jetbrains.com/pycharm/download/)，有兩個可供下載的版本一個是社區版一個是專業版，社區版在[Apache許可證](https://zh.wikipedia.org/wiki/Apache%E8%AE%B8%E5%8F%AF%E8%AF%81)下發布，專業版在專用許可證下發布（需要購買授權下載後可試用30天），其擁有許多額外功能。安裝PyCharm需要有JRE（Java運行時環境）的支持，如果沒有可以在安裝過程中選擇在線下載安裝。

> 說明：如果你是一名學生，希望購買PyCharm來使用，可以看看[教育優惠官方申請指南](https://sales.jetbrains.com/hc/zh-cn/articles/207154369)。

### 首次使用的設置

第一次使用PyCharm時，會有一個導入設置的向導，如果之前沒有使用PyCharm或者沒有保存過設置的就直接選擇“Do not import settings”進入下一步即可。

![](./res/pycharm-import-settings.png)

專業版的PyCharm是需要激活的，**強烈建議爲優秀的軟件支付費用**，如果不用做商業用途，我們可以暫時選擇試用30天或者使用社區版的PyCharm。

![](./res/pycharm-activate.png)

 接下來是選擇UI主題，這個可以根據個人喜好進行選擇。

![](./res/pycharm-set-ui-theme.png)

 再接下來是創建可以在終端（命令行）中使用PyCharm項目的啓動腳本，當然也可以直接跳過這一步。

![](./res/pycharm-create-launcher-script.png)

然後可以選擇需要安裝哪些插件，我們可以暫時什麽都不安裝等需要的時候再來決定。

![](./res/pycharm-plugins.png)

### 用PyCharm創建項目

點擊上圖中的“Start using PyCharm”按鈕就可以開始使用PyCharm啦，首先來到的是一個歡迎頁，在歡迎頁上我們可以選擇“創建新項目”、“打開已有項目”和“從版本控制係統中檢出項目”。

![](./res/pycharm-welcome.png)

如果選擇了“Create New Project”來創建新項目就會打一個創建項目的向導頁。

![](./res/pycharm-new-project.png)

在如上圖所示的界面中，我們可以選擇創建項目的模板，包括了純Python項目、基於各種不同框架的Web項目、Web前端項目、跨平台項目等各種不同的項目模板。如果選擇Python的項目，那麽有一個非常重要的設定是選擇“New environment…”（創建新的虛擬環境）還是使用“Existing Interpreter”（已經存在的解釋器）。前者肯定是更好的選擇，因爲新的虛擬環境不會對係統環境變量中配置的Python環境造成影響，簡單舉個例子就是你在虛擬環境下安裝或者更新了任何三方庫，它並不會對係統原有的Python解釋器造成任何的影響，但代價是需要額外的存儲空間來建立這個虛擬環境。

項目創建完成後就可以開始新建各種文件來書寫Python代碼了。

![](./res/pycharm-workspace.png)

在工作窗口的右鍵菜單中可以找到“Run ...”和“Debug ...”菜單項，通過這兩個菜單項我們就可以運行和調試我們的代碼啦。建議關注一下菜單欄中的“Code”、“Refactor”和“Tools”菜單，這裏面爲編寫Python代碼提供了很多有用的幫助，我們在後面也會陸續爲大家介紹這些功能。