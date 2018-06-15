## 玩轉Linux操作係統

### 操作係統發展史

![](./res/history-of-os.png)

### Linux概述

Linux是一個通用操作係統。一個操作係統要負責任務調度、內存分配、處理外圍設備I/O等操作。操作係統通常由內核和係統程序（設備驅動、底層庫、shell、服務程序等）兩部分組成。

Linux內核是芬蘭人Linus Torvalds開發的，於1991年9月發布。而Linux操作係統作爲Internet時代的産物，它是由全世界許多開發者共同合作開發的，是一個自由的操作係統（注意是自由不是免費）。

### Linux係統優點

1. 通用操作係統，不跟特定的硬件綁定。
2. 用C語言編寫，有可移植性，有內核編程接口。
3. 支持多用戶和多任務，支持安全的分層文件係統。
4. 大量的實用程序，完善的網絡功能以及強大的支持文檔。
5. 可靠的安全性和良好的穩定性，對開發者更友好。

### 基礎命令

Linux係統的命令通常都是如下所示的格式：

```Shell
命令名稱 [命名參數] [命令對象]
```

1. 獲取登錄信息 - **w** / **who** / **last**。

   ```Shell
   [root@izwz97tbgo9lkabnat2lo8z ~]# w
    23:31:16 up 12:16,  2 users,  load average: 0.00, 0.01, 0.05
   USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
   root     pts/0    182.139.66.250   23:03    4.00s  0.02s  0.00s w
   jackfrue pts/1    182.139.66.250   23:26    3:56   0.00s  0.00s -bash
   [root@izwz97tbgo9lkabnat2lo8z ~]# who
   root     pts/0        2018-04-12 23:03 (182.139.66.250)
   jackfrued pts/1        2018-04-12 23:26 (182.139.66.250)
   [root@izwz97tbgo9lkabnat2lo8z ~]# who am i
   root     pts/0        2018-04-12 23:03 (182.139.66.250)
   ```

2. 查看自己使用的Shell - **ps**。

   Shell也被稱爲“殼”，它是用戶與內核交流的翻譯官，簡單的說就是人與計算機交互的接口。目前很多Linux係統默認的Shell都是bash（<u>B</u>ourne <u>A</u>gain <u>SH</u>ell），因爲它可以使用Tab鍵進行命令補全、可以保存曆史命令、可以方便的配置環境變量以及執行批處理操作等。

   ```Shell
   [root@izwz97tbgo9lkabnat2lo8z ~]# ps
     PID TTY          TIME CMD
    3531 pts/0    00:00:00 bash
    3553 pts/0    00:00:00 ps
   ```

3. 查看命令的說明 - **whatis**。

   ```Shell
   [root@izwz97tbgo9lkabnat2lo8z ~]# whatis ps
   ps (1)        - report a snapshot of the current processes.
   [root@izwz97tbgo9lkabnat2lo8z ~]# whatis python
   python (1)    - an interpreted, interactive, object-oriented programming language
   ```

4. 查看命令的位置 - **which** / **whereis**。

   ```Shell
   [root@izwz97tbgo9lkabnat2lo8z ~]# whereis ps
   ps: /usr/bin/ps /usr/share/man/man1/ps.1.gz
   [root@izwz97tbgo9lkabnat2lo8z ~]# whereis python
   python: /usr/bin/python /usr/bin/python2.7 /usr/lib/python2.7 /usr/lib64/python2.7 /etc/python /usr/include/python2.7 /usr/share/man/man1/python.1.gz
   [root@izwz97tbgo9lkabnat2lo8z ~]# which ps
   /usr/bin/ps
   [root@izwz97tbgo9lkabnat2lo8z ~]# which python
   /usr/bin/python
   ```

5. 查看幫助文檔 - **man** / **info** / **apropos**。
   ```Shell
   [root@izwz97tbgo9lkabnat2lo8z ~]# ps --help
   Usage:
    ps [options]
    Try 'ps --help <simple|list|output|threads|misc|all>'
     or 'ps --help <s|l|o|t|m|a>'
    for additional help text.
   For more details see ps(1).
   [root@izwz97tbgo9lkabnat2lo8z ~]# man ps
   PS(1)                                User Commands                                PS(1)
   NAME
          ps - report a snapshot of the current processes.
   SYNOPSIS
          ps [options]
   DESCRIPTION
   ...
   [root@izwz97tbgo9lkabnat2lo8z ~]# info ps
   ...
   ```

6. 切換用戶 - **su**。

   ```Shell
   [root@izwz97tbgo9lkabnat2lo8z ~]# su hellokitty
   [hellokitty@izwz97tbgo9lkabnat2lo8z root]$
   ```

7. 以管理員身份執行命令 - **sudo**。

   ```Shell
   [jackfrued@izwz97tbgo9lkabnat2lo8z ~]$ ls /root
   ls: cannot open directory /root: Permission denied
   [jackfrued@izwz97tbgo9lkabnat2lo8z ~]$ sudo ls /root
   [sudo] password for jackfrued:
   calendar.py  code  error.txt  hehe  hello.c  index.html  myconf  result.txt
   ```

   > **說明**：如果希望用戶能夠以管理員身份執行命令，用戶必須在sudoers（/etc/sudoers）名單中。

8. 登入登出相關 - **logout** / **exit** / **adduser** / **userdel** / **passwd** / **ssh**。

   ```Shell
   [root@izwz97tbgo9lkabnat2lo8z ~]# adduser jackfrued
   [root@izwz97tbgo9lkabnat2lo8z ~]# passwd jackfrued
   Changing password for user jackfrued.
   New password:
   Retype new password:
   passwd: all authentication tokens updated successfully.
   [root@izwz97tbgo9lkabnat2lo8z ~]# ssh hellokitty@1.2.3.4
   hellokitty@1.2.3.4's password:
   Last login: Thu Apr 12 23:05:32 2018 from 10.12.14.16
   [hellokitty@izwz97tbgo9lkabnat2lo8z ~]$ logout
   Connection to 1.2.3.4 closed.
   [root@izwz97tbgo9lkabnat2lo8z ~]#
   ```

9. 查看係統和主機名 - **uname** / **hostname**。

   ```Shell
   [root@izwz97tbgo9lkabnat2lo8z ~]# uname
   Linux
   [root@izwz97tbgo9lkabnat2lo8z ~]# hostname
   izwz97tbgo9lkabnat2lo8z
   [root@iZwz97tbgo9lkabnat2lo8Z ~]# cat /etc/centos-release
   CentOS Linux release 7.4.1708 (Core) 
   ```

10. 重啓和關機 - **reboot** / **init 6** / **shutdown** / **init 0**。

11. 查看曆史命令 - **history**。

### 實用程序

#### 文件和文件夾操作

1. 創建/刪除目錄 - **mkdir** / **rmdir**。

2. 創建/刪除文件 - **touch** / **rm**。

   - touch命令用於創建空白文件或修改文件時間。在Linux係統中一個文件有三種時間：
     - 更改內容的時間（mtime）
     - 更改權限的時間（ctime）
     - 最後訪問時間（atime）

3. 切換和查看當前工作目錄 - **cd** / **pwd**。

4. 查看目錄內容 - **ls**。

5. 查看文件內容 - **cat** / **head** / **tail** / **more** / **less**。

6. 拷貝/移動文件 - **cp** / **mv**。

7. 查看文件及內容 - **find** / **grep**。

   ```Shell
   [root@izwz97tbgo9lkabnat2lo8z ~]# find -name *.html
   ./index.html
   ./code/index.html
   [root@izwz97tbgo9lkabnat2lo8z ~]# grep "<script>" . -R -n
   ./index.html:15:                <script>
   ./code/index.html:2884: <script>
   ./code/foo.html:2:<!--STATUS OK--><html> <head><meta ...
   ```

8. 符號鏈接 - **ln**。

9. 壓縮和歸檔 - **gzip** / **gunzip** / **xz** / **tar**。

10. 其他工具 - **sort** / **uniq** / **diff** / **file** / **wc**。

#### 管道和重定向

1. 管道的使用 - **\|**。
2. 輸出重定向和錯誤重定向 - **\>** / **2\>**。
3. 輸入重定向 - **\<**。

#### 別名

1. **alias**
2. **unalias**

#### 其他程序

1. 時間和日期 - **date** / **cal**。
2. 錄制操作腳本 - **script**。
3. 給用戶發送消息 - **mesg** / **write** / **wall** / **mail**。

### 文件係統

#### 文件和路徑

1. 命名規則
2. 擴展名
3. 隱藏文件
4. 工作目錄和主目錄
5. 絕對路徑和相對路徑

#### 目錄結構

1. /bin - 基本命令的二進制文件
2. /boot - 引導加載程序的靜態文件
3. /dev - 設備文件
4. /etc - 配置文件
5. /home - 用戶主目錄的父目錄
6. /lib - 共享庫文件
7. /lib64 - 共享64位庫文件
8. /lost+found - 存放未鏈接文件
9. /media - 自動識別設備的挂載目錄
10. /mnt - 臨時挂載文件係統的挂載點
11. /opt - 可選插件軟件包安裝位置
12. /proc -  內核和進程信息
13. /root - root賬戶主目錄
14. /run - 存放係統運行時需要的東西
15. /sbin - 超級用戶的二進制文件
16. /sys - 設備的僞文件係統
17. /tmp - 臨時文件夾
18. /usr - 用戶應用目錄
19. /var - 變量數據目錄

#### 訪問權限

1. **chmod**。
2. **chown**。

#### 磁盤管理

1. 列出文件係統的磁盤使用狀況 - **df**。
2. 磁盤分區表操作 - **fdisk**。
3. 格式化文件係統 - **mkfs**。
4. 文件係統檢查 - **fsck**。
5. 挂載/卸載 - **mount** / **umount**。

### 編輯器vim

1. 啓動和退出

2. 命令模式和編輯模式

3. 光標操作

4. 文本操作

5. 查找和替換

   /正則表達式

   :1,$s/正則表達式/替換後的內容/gice

   g - global

   i - ignore case

   c - confirm

   e - error

6. 參數設定

   .vimrc

   set ts=4

   set nu

7. 高級技巧

   - 映射快捷鍵
     - inoremap key:...
   - 錄制宏
     - 在命令模式下輸入qa開始錄制宏（qa/qb/qc/qd）
     - 執行你的操作，這些操作都會被錄制下來
     - 如果要錄制的操作完成了，按q結束錄制
     - @a播放宏（1000@a - 將宏播放1000次）

### 環境變量

1. HOME
2. SHELL
3. HISTSIZE
4. RANDOM
5. PATH

### 軟件安裝和配置

#### yum

- yum update
- yum install / yum remove
- yum list / yum search
- yum makecache

#### rpm

- rpm -ivh \-\-force \-\-nodeps
- rpm -e 
- rpm -qa | grep

#### 源代碼構建安裝

- ...
- make && make install

#### 實例

1. 安裝MySQL。
2. 安裝Redis。
3. 安裝NginX。

### 配置服務

1. systemctl start / stop / restart / status
2. systemctl enable / disable
3. 計劃任務 - **crontab**。
4. 開機自啓。

### 網絡訪問和管理

1. 通過網絡獲取資源 - **wget**。
   - -b 後台下載模式
   - -O 下載到指定的目錄
   - -r 遞歸下載
2. 顯示/操作網絡配置（舊） - **ipconfig**。
3. 顯示/操作網絡配置（新） - **ip**。
4. 網絡可達性檢查 - **ping**。
5. 查看網絡服務和端口 - **netstat**。
6. 安全文件拷貝 - **scp**。
7. 安全文件傳輸 - **sftp**。

### Shell和Shell編程

1. 通配符。
2. 後台運行。

### 其他內容

1. awk
2. sed
3. xargs