from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

PATH = "./chromedriver.exe"

driver = webdriver.Chrome(PATH)
driver.get("https://orteil.dashnet.org/cookieclicker/")

#We wont have this  5s to load up everything
driver.implicitly_wait(5)

cookie = driver.find_element_by_id("bigCookie")
cookie_count = driver.find_element_by_id('cookies')
#Loop from product 1 on website - more expensive item first on website
items = [driver.find_element_by_id("productPrice" + str(i)) for i in range(1,-1,-1)]



action = ActionChains(driver)
action.click(cookie)

for i in range(5000):
    action.perform() # Will do click - perform actions before that
    count = int(cookie_count.text.split(" ")[0])
    for item in items:
        value = int(item.text)
        if value <= count:
            upgrade_action = ActionChains(driver)
            #Przesyń do miejsca item 1 i 0 do pętlenia sprawdzania czy już masz odpowiednią ilość aby zakupić upgrade
            upgrade_action.move_to_element(item)
            upgrade_action.click()
            upgrade_action.perform()