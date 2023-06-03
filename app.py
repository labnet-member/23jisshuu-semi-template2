import json
import datetime
import time
import logging
import requests

LOWER_HOUR = 9  # 9:00 ~
UPPER_HOUR = 18 #  ~ 18:00
INTERVAL = 600
HUM_THR = 60
NG_weather_groups = ["Thunderstorm", "Drizzle", "Rain", "Snow"]
# 以下は各自置き換える
SB_TOKEN = "xxxxxxx"
OW_TOKEN = "xxxxxxx"
TURN_ON_URL = "https://maker.ifttt.com/trigger/turn_on/json/with/key/xxxxxxxxx"
TURN_OFF_URL = "https://maker.ifttt.com/trigger/turn_off/json/with/key/xxxxxxxxx"

# OpenWeatherAPIから天気予報を取得
def get_forecast() -> dict:
    response = requests.get(
        # (?) OpenWeatherAPIを叩く
    )
    return json.loads(response.text)

# NGな天気が含まれるかの確認
def contains_NG_weather(forecast: dict) -> bool:
    now = datetime.datetime.now()
    # 今日の9:00と18:00を表すdatetimeを作成
    dt_upper = now.replace(hour=UPPER_HOUR, minute=0, second=0, microsecond=0)
    dt_lower = now.replace(hour=LOWER_HOUR, minute=0, second=0, microsecond=0)
    for x in forecast["list"]:
        dt = datetime.datetime.fromtimestamp(int(x["dt"]))
        if # (?) dtが今日の9:00 ~ 18:00に含まれるかどうか
            for y in x["weather"]:
                if # (?) yがNGな天気かどうか
                    return True
    return False

# SwitchBotから湿度を取得
def get_humidity() -> int:
    response = requests.get(
        # (?) SwichBotAPIを叩く
    )
    ret = json.loads(response.text)
    humidity = # (?) 湿度を抽出
    return humidity

# main
if __name__ == "__main__":
    forecast = get_forecast()
    if contains_NG_weather(forecast):
        logging.info('Move on to dehumidifier-controlling mode')
        while True:
            if  # (?) 湿度が閾値以上であれば
                # (?) 除湿機を付ける
                logging.info('Turned on the plug')
            else:
                # (?) 除湿機を消す
                logging.info('Turned off the plug')
            time.sleep(INTERVAL)
