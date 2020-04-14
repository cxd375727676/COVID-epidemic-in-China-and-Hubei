# -*- coding: utf-8 -*-
""" 
senlenium 测试浏览器可视化时间，
再对MP3进行编辑，
最后利用EV录屏 及 pynput模拟键盘快捷键控制录屏开始和停止。
注意录屏前设置好EV录屏软件，用bat文件启动python脚本，录制浏览器整个渲染过程为mp4文件

注：
pydub安装
pip install pydub, FFmpeg
下载ffmpeg windows平台压缩包，配置环境变量
"""
import time
import sys
import os

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pynput.keyboard import Key, Controller
#import pydub



def display(test=False):
    """ test=True ，测试浏览器可视化时间（秒） """
    cwd = os.getcwd()
    
    options = webdriver.ChromeOptions()
    options.add_argument('log-level=3')
    if test:
        options.add_argument('--headless')
    else:
        # 隐藏 浏览器受自动控制 提示信息
        options.add_experimental_option("excludeSwitches", ["enable-automation"]) # 隐藏 浏览器受自动控制 提示信息
        options.add_experimental_option("useAutomationExtension", False)

    driver = webdriver.Chrome(
            options=options,
            executable_path="驱动路径")
    driver.maximize_window() 
    try:
        driver.get("file:///" + os.path.join(cwd, "bargraph.html"))
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "inputfile"))) # 等待上传文件按钮加载
        button = driver.find_element_by_id("inputfile")
        button.send_keys(os.path.join(cwd, "{}.csv".format(sys.argv[1])))
        WebDriverWait(driver, 10).until_not(EC.visibility_of(button))  # 确认数据文件成功上传
        if test:
            start = time.time()
            WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "end"))) # 等待网页可视化结束
            end = time.time()
            return end - start
        else:
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, "media-player"))) # 等待音频加载
            player = driver.find_element_by_id("media-player")
            size = player.size
            offset_x = size['width'] / 16
            offset_y = size['height'] / 2
            ActionChains(driver).move_to_element_with_offset(player, offset_x, offset_y).click().perform() # 播放
            #将滚动条移动到页面的顶部
            js_top = "var q=document.documentElement.scrollTop=0"
            driver.execute_script(js_top)
            time.sleep(0.5)
            start_screencap()
            WebDriverWait(driver, 300).until(EC.presence_of_element_located((By.ID, "end"))) # 等待网页可视化结束
            time.sleep(5)
            end_screencap()          
    except:
        pass
    finally:
        driver.quit()


def start_screencap():
    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):    #组合按键ctrl+F1
        keyboard.press(Key.f1)
        keyboard.release(Key.f1)


def end_screencap():
    keyboard = Controller()
    with keyboard.pressed(Key.ctrl):    #组合按键ctrl+F2
        keyboard.press(Key.f2)
        keyboard.release(Key.f2) 


#def edit_mp3(start, end, input_, output):
#    """ start, end 是开始和终止，单位：秒 """
#    music = pydub.AudioSegment.from_mp3(input_)
#    music = music[start * 1000 : end * 1000]
#    music = music.fade_in(1000).fade_out(2000)  # 浅入1s淡出2s
#    music.export(output, format="mp3")



if __name__ == '__main__':
#    # 测试: 获取音频保留时间
#    sys.argv.append("chn_ncp")
#    seconds = display(test=True)
#    edit_mp3(0, seconds, "raw_bgm.mp3", "bgm.mp3")
    display()
