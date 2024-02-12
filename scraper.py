from selenium import webdriver


driver = webdriver.Chrome()

driver.get("https://www.immigration.govt.nz/new-zealand-visas/preparing-a-visa-application/working-in-nz/qualifications-for-work/green-list-occupations")

name_list = driver.find_elements("xpath", "//h3[contains(@class, 'content_list_heading')]")
for name in name_list:
    print(name.text)

# driver.quit()
