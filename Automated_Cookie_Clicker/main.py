import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

chrome_driver_options = webdriver.ChromeOptions()
chrome_driver_options.add_experimental_option("detach",True)

driver = webdriver.Chrome(options=chrome_driver_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

wait = WebDriverWait(driver, 10)
#items_money = []
items_name = ['Cursor', 'Grandma', 'Factory', 'Mine', 'Shipment', 'Alchemy lab', 'Portal', 'Time machine']
items_money_int=[15, 100, 500, 2000, 7000, 50000, 1000000, 123456789]

items = driver.find_elements(By.CSS_SELECTOR,"#store .grayed b")
# count = 8
# current_count=0
# for i in items:
#     full_item = i.text.split(" - ")
#     if current_count<count:
#         items_name.append(full_item[0])
#         items_money.append(full_item[1])
#     current_count+=1
# print(items_name)
start = time.time()
duration_large = 300
while time.time() - start < duration_large:
    duration = 5
    while time.time() - start < duration:
        try:
            button = driver.find_element(By.ID, "cookie")
            button.click()
        except:
            break
            # for i in items_money:
    #     string_number = i
    #     cleaned_string = string_number.replace(",","")
    #     integer_number = int(cleaned_string)
    #     items_money_int.append(integer_number)
    # print(items_money_int)
    try:
        money_element = wait.until(EC.presence_of_element_located((By.ID, "money")))
        money_str = money_element.text.replace(",", "")
        int_money = int(money_str)
    except:
        int_money = 0
    max_affordable_item = None
    count = 0
    for i in items_money_int:
        if i < int_money:
            max_affordable_item = items_name[count]
        count += 1
    if max_affordable_item:
        try:
            button_item = wait.until(EC.element_to_be_clickable((By.ID, f"buy{max_affordable_item}")))
            button_item.click()
        except:
            pass
driver.quit()