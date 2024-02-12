from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

# Get selenium chrome web driver
driver = webdriver.Chrome()

driver.get(
    "https://www.immigration.govt.nz/new-zealand-visas/preparing-a-visa-application/working-in-nz/qualifications-for-work/green-list-occupations"
)

try:
    # Click on "See More" button until the button is NOT displayed, for seeing all 193 jobs
    btn = driver.find_element("xpath", "//button[contains(@class, 'results_loadbtn')]")
    while btn.is_displayed():
        driver.execute_script("arguments[0].click();", btn)
        btn = driver.find_element(
            "xpath", "//button[contains(@class, 'results_loadbtn')]"
        )

    # Scrape all job titles
    job_titles = driver.find_elements(
        "xpath", "//h3[contains(@class, 'content_list_heading')]"
    )

    # Write to file
    with open("new_zealand_jobs_list", "w") as file:
        for title in job_titles:
            file.write(title.text + "\n")

except NoSuchElementException:
    print("The elements not found in this page!")

driver.quit()
