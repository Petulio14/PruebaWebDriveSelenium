from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#ultima noticia del colombiano con Web Scraping (Python y Selenium)

PATH = 'C:/chrome_webdriver/chromedriver.exe'


driver = webdriver.Chrome(PATH)
#driver = webdriver.Firefox(executable_path="C:/firefox_webdriver/geckodriver.exe")

driver.get("https://www.elcolombiano.com/lo-ultimo")

#time.sleep(0)


newColombiano=driver.find_element(By.CLASS_NAME, "right")
print('La ultima noticia del colombiano es: '+ newColombiano.text)

driver.quit()