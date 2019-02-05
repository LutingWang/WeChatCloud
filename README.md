# WeChat History Word Cloud Generator for iOS

## Project Summery

The project provides complementary scripts to generate **WeChat History Word Cloud**, as all data exporting will be done on **louyue Software**. Although the project is intended for **iOS**, **Android** system is fundamentally the same, except that the export procedures might not be applicable. 

The following part of this document serves as not only an explanation to the project per se, but also a documentation on how to manipulate **louyue Software** to backup WeChat documents, decode WeChat history, and using the data exported to eventually generate word cloud.

## Requisitions

- iTunes

  iTunes provides an interface between iPhone/iPad and PC. 

- Louyue iTunes Backup Manager

  Re-organizing backup files and selectively export app data.
  
  [楼月免费iTunes备份管理器](http://www.louyue.com/itunes.htm)

- Louyue WeChat History Helper

  Decode WeChat history files and export as html document. Full version may need activation. 
  
  [楼月微信聊天记录导出恢复助手](http://www.louyue.com/weixin.htm)

- Python 3 Environment

  The main script is written in Python3. Packages BeautifulSoup, jieba, wordcloud, matplotlib, PIL, numpy are required.

## Usage

### Set-up Environment

Clone or download the project. It is preferably not to change the project name, but there is great flexibility speaking of its content. The project consists of *wordcloud_gen.py*, *font.ttf*, and *mask.png*. The last two files are default settings for generating word cloud, which is **simhei** font and **heart-shaped** graph. The file content can be modified but the file names are fixed, otherwise it would cause an exception. 

Make sure when you finish changing the font and mask, the project still has *wordcloud_gen.py*, *font.ttf*, and *mask.png*.

### Backup iPhone

1. Open up iTunes and connect your iPhone to it via USB port.
2. Backup your iPhone without encoding its content.

### Manage Backup File

1. Launch **Louyue iTunes Backup Manager**.
2. On the top double-click your backup.
3. In the pop window, choose **微信聊天记录**. If any error occur or the directory does not exist, it suggests that your backup may be encoded. You can return to the previous step and redo it.
4. Click **Document** and then click on **导出**, and you can save the file anywhere. 
5. For simply exporting WeChat history, you may . However, for generating word cloud, you need to export the Document folder under the project directory, i.e. within the folder **WeChatCloud**.

### Export Chat History

1. Run **Louyue WeChat History Helper**.
2. Follow the instructions on the window. 
3. After you click on **查看记录**, a window should pop up showing your WeChat history, meaning that you have successfully decoded the chat history.
4. On the top right corner, choose File | Export Chat History.
5. In the pop up window, choose the chats you want to export, and then start exporting.
6. Save the file under the project directory, i.e. within the folder **WeChatCloud**.

### Run Python Script

In *cmd* window for Windows, run 

```Shell
cd path/WeChatCloud/
python wordcloud_gen.py
```

where *path* in the code is customized.

### Check Out

You should now see a new *png* file named **username.png**, which is the word cloud intended.

## Acknowledgement

Thanks to the information provided by an anonymous user in **Baidu Zhidao**. [Original Post](https://zhidao.baidu.com/question/2016194301396860828.html)

