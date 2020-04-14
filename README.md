# Dynamic-Bar
thanks for refer,
借助的，做了微小修改，可视化中国各省疫情和湖北各地市州疫情
具体修改如下：

- src
 1.bargraph.html修改title，添加标题, 添加audio标签播放背景音乐

 2.增加背景音乐raw_bgm.mp3（victory)

 3.中国各省新冠累计确诊数据chn_ncp.csv 和湖北省各地市州省新冠累计确诊数据hbyq.csv

 4.调整config.js适合自己的屏幕

 5.用python脚本launch_chrome.py上传数据；测试可视化过程，编辑背景音乐raw_bgm.mp3-->bgm.mp3，使其完美配合动态可视化过程；结合EV录屏软件，利用pynput库模拟组合快捷键录屏
 6.修改visual.js，可视化结束后在bargraph.html中添加作者信息（右下角），便于python脚本判断driver.quit()的时机
- exe_hbyq.bat:启动python脚本
- result:两个MP4文件，可视化展示
