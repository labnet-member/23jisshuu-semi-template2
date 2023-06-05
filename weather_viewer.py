import requests
import os
import sys

#openweatherAPI
URL_CURRENT="https://api.openweathermap.org/data/2.5/weather?lat=34.3999649&lon=132.7135802&appid=<APIKey>&units=metric"
URL_FORCAST="https://api.openweathermap.org/data/2.5/forecast?lat=34.3999649&lon=132.7135802&appid=<APIKey>&units=metric"



#現在の天気を持ってくるコードを記述
r = requests.get()

#３時間おきの天気予報を４つ持ってくるコードを記述
r = requests.get()

#天気予報を検証し点灯させるLEDを制御するコードを記述

#雨が降るなら赤く点灯
os.system('echo 0 > /sys/class/leds/led0/brightness ')
os.system('echo 1 > /sys/class/leds/led1/brightness ')
sys.exit(0)

#雨が降らない予報なら緑に点灯
os.system('echo 0 > /sys/class/leds/led1/brightness ')
os.system('echo 1 > /sys/class/leds/led0/brightness ')