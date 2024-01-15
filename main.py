import time
from bs4 import *
from requests import *
from selenium import webdriver
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys

GOOGLE_FORM_LINK = "https://forms.gle/uHSnCVzn9mBJaZpT8"

response = get("https://appbrewery.github.io/Zillow-Clone/")
soup = BeautifulSoup(response.text, "html.parser")
# print(soup.title)

# LINKS LIST
lets_create_list = soup.select(".ListItem-c11n-8-84-3-StyledListCardWrapper .StyledPropertyCardDataWrapper a")
links_list = [i.get("href") for i in lets_create_list]
# print(links_list)

# PRICE LIST
lets_create_list2 = soup.select(".ListItem-c11n-8-84-3-StyledListCardWrapper .PropertyCardWrapper__StyledPriceLine")
price_list = [i.text.replace("+", "/").split("/")[0] for i in lets_create_list2]
# pprint(price_list)

# ADDRESS LIST
lets_create_list3 = soup.select(".ListItem-c11n-8-84-3-StyledListCardWrapper address")
address_list = [i.text.strip(" \n") for i in lets_create_list3]
# print(address_list)

#print(len(links_list), len(address_list), len(price_list))
# print(links_list)


driver_opt = webdriver.ChromeOptions()
driver_opt.add_experimental_option("detach", True)
driver = webdriver.Chrome(driver_opt)

driver.get(GOOGLE_FORM_LINK)
time.sleep(3)

for i in range(0, 44):
    fill_address = driver.find_element(By.XPATH,
                                       '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]'
                                       '/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill_address.send_keys(address_list[i])

    fill_price = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]'
                                     '/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill_price.send_keys(price_list[i])

    fill_link = driver.find_element(By.XPATH,
                                    '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]'
                                    '/div/div/div[2]/div/div[1]/div/div[1]/input')
    fill_link.send_keys(links_list[i])

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()

    time.sleep(1)

    another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()
    time.sleep(1)

driver.quit()