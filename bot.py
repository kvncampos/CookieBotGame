from chrome_setup import chrome_setup
from selenium.webdriver.common.by import By
from time import sleep

driver = chrome_setup()
driver.get('https://orteil.dashnet.org/cookieclicker/')
sleep(2)
start_english_game = driver.find_element(By.ID, value='langSelect-EN')
start_english_game.click()

sleep(2)
cookie_button = driver.find_element(By.ID, value='bigCookie')

counter = 1
cursor_counter = 1
grandma_counter = 1
farm_counter = 1
mine_counter = 1
product4 = 1
product5 = 1

for x in range(100000000000):
    cookie_button.click()
    counter += 1

    if product4 % 2 == 0:
        print("Attempt To Purchase: ???")
        unknown = driver.find_element(By.ID, value='product5')
        unknown.click()
        unknown += 1
        product4 = 0

    if mine_counter % 2 == 0:
        print("Attempt To Purchase: FACTORY")
        factory_buy = driver.find_element(By.ID, value='product4')
        factory_buy.click()
        product4 += 1
        mine_counter = 0

    if farm_counter % 5 == 0:
        print("Attempt To Purchase: FARM")
        mine_buy = driver.find_element(By.ID, value='product3')
        mine_buy.click()
        mine_counter += 1
        farm_counter = 0

    if grandma_counter % 10 == 0:
        try:
            upgrade0 = driver.find_element(By.ID, value='upgrade2')
            upgrade0.click()
            upgrade0 = driver.find_element(By.ID, value='upgrade3')
            upgrade0.click()
            print("Upgrade Purchased.")
        except:
            print("No Upgrades")

        print("Attempt To Purchase: FARM")
        farm_buy = driver.find_element(By.ID, value='product2')
        farm_buy.click()
        farm_counter += 1
        grandma_counter = 0

    if cursor_counter % 20 == 0:
        print("Attempt to Purchase: GRANDMA")
        try:
            upgrade0 = driver.find_element(By.ID, value='upgrade0')
            upgrade0.click()
            upgrade0 = driver.find_element(By.ID, value='upgrade1')
            upgrade0.click()
            print("Upgrade Purchased.")
        except:
            print("No Upgrades")

        grandma_buy = driver.find_element(By.ID, value='product1')
        grandma_buy.click()
        grandma_counter += 1
        cursor_counter = 0


    if counter == 20:
        # print("Attempt To Purchase: CURSOR.")
        curser_buy = driver.find_element(By.ID, value='product0')
        curser_buy.click()
        cursor_counter += 1
        counter = 0


# print("CheckScore")
# driver.quit()
