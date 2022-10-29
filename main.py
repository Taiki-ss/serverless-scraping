from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import requests


def main(line_apy_key=None):

    # if line_apy_key is None:
    #   print('not found line_apy_key')
    #   return

    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    s = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=s, options=options)
    driver.get('https://www.city.sasebo.lg.jp/kurashi/sumai/shie/boshu/index.html')
    time.sleep(3)

    element = driver.find_element(By.XPATH, '//*[@id="tmp_contents"]/ul')

    html = element.get_attribute('innerHTML')

    print(element.get_attribute('innerHTML'))
    print('実行テスト')

    driver.quit()

    # LINE 通知コメントアウト
    # ACCESS_TOKEN ='xxxxxxxxxxxxxxxx'

    # URL = 'https://api.line.me/v2/bot/message/broadcast'

    # headers = {
    #     'Authorization':'Bearer ' + ACCESS_TOKEN,
    #     'Content-Type': "application/json"
    # }

    # message = "メッセージテスト\n" + html

    # res = requests.post(URL,
    #     headers=headers,
    #     json={
    #         "messages": [{
    #             "type" : "text",
    #             "text":message
    #         }]
    #     }).json()

    # print(res)


if __name__ == "__main__":
    main()
