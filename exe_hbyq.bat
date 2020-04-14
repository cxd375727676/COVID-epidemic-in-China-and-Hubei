@echo off
:: 我的bat文件起始位置总是desktop
:: 湖北省地市州新冠疫情数据 hbyq
:: 最小化cmd窗口
%1(start /min cmd.exe /c %0 :&exit)
cd Historical-ranking-data-visualization-based-on-d3.js-master\src
python launch_chrome.py hbyq