import copy

from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import re

driver = webdriver.Chrome()

url = "https://lucky-jet-b.1play.one/?exitUrl=null&language=ru&b=demo"
driver.get(url)
time.sleep(10)

id_mobile = driver.find_element(By.ID, 'root')

#print(id_mobile.text)
id_mob = str(id_mobile.text)

driver.close()


res = re.findall("\d+\.\d+x", id_mob)
