from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import sys
import time
import requests

import handle_data


def main(line_apy_key=None):

    if line_apy_key is None:
        print('not found line_apy_key')
        return

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=options)
    driver.get('https://www.city.sasebo.lg.jp/kurashi/sumai/shie/boshu/index.html')
    time.sleep(3)

    elements = driver.find_elements(
        By.XPATH, '//*[@id="tmp_contents"]/ul/li/a')

    text = ''

    for element in elements:
        text += element.text + '\n' + element.get_attribute('href') + '\n'

    driver.quit()
    print('スクレイピング終了')

    if handle_data.handle_data(text):
        print('変更あり！')
        # LINE 通知

        URL = 'https://api.line.me/v2/bot/message/broadcast'

        headers = {
            'Authorization': 'Bearer ' + line_apy_key,
            'Content-Type': "application/json"
        }

        message = "【市営住宅募集ページ更新】\n\n" + text

        res = requests.post(URL,
                            headers=headers,
                            json={
                                "messages": [{
                                    "type": "text",
                                    "text": message
                                }]
                            }).json()

        print(res)
    else:
        print('変更なし')


if __name__ == "__main__":
    args = sys.argv
    main(args[1])
