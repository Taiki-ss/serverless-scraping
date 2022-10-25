from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument('--headless')
options.add_argument('--no-sandbox')

s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s,options=options)
driver.get('https://www.city.sasebo.lg.jp/kurashi/sumai/shie/boshu/index.html')
time.sleep(3)

element = driver.find_element(By.XPATH, '//*[@id="tmp_contents"]/ul/li[1]/a')
print(element.text)

driver.quit()
