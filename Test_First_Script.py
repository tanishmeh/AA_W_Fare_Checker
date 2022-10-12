from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "/Users/tanishmehta/Downloads/chromedriver"
driver = webdriver.Chrome(PATH)
driver.get("https://matrix.itasoftware.com/search?search=eyJ0eXBlIjoicm91bmQtdHJpcCIsInNsaWNlcyI6W3sib3JpZ2luIjpbIk5ZQyJdLCJkZXN0IjpbIkRFTCJdLCJkYXRlcyI6eyJzZWFyY2hEYXRlVHlwZSI6InNwZWNpZmljIiwiZGVwYXJ0dXJlRGF0ZSI6IjIwMjMtMDEtMDIiLCJkZXBhcnR1cmVEYXRlUHJlZmVycmVkVGltZXMiOltdLCJkdXJhdGlvbiI6IjMwIiwicmV0dXJuRGF0ZSI6IjIwMjMtMDEtMzAiLCJyZXR1cm5EYXRlUHJlZmVycmVkVGltZXMiOltdfX1dLCJvcHRpb25zIjp7ImNhYmluIjoiUFJFTUlVTS1DT0FDSCIsInN0b3BzIjoiMCIsImV4dHJhU3RvcHMiOiItMSIsImFsbG93QWlycG9ydENoYW5nZXMiOiJ0cnVlIiwic2hvd09ubHlBdmFpbGFibGUiOiJ0cnVlIn0sInBheCI6eyJhZHVsdHMiOiIxIn19")
print(driver.title)

# driver.find_element(By.CSS_SELECTOR, ".mat-end-date").click()
# driver.find_element(By.CSS_SELECTOR, ".cdk-overlay-backdrop").click()

def changeDate(startDate, endDate):
    date = driver.find_element(By.CSS_SELECTOR, ".mat-end-date")
    date.send_keys("\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b\b")




# sdate = driver.find_element(By.CSS_SELECTOR, ".mat-start-date")
# edate = driver.find_element(By.CSS_SELECTOR, ".mat-end-date")
# sdate.clear()
# edate.clear()



# elem = driver.find_element(By.ID, "mat-chip-list-input-0")
# elem.clear()
# elem.send_keys("nyc")
# elem.send_keys(Keys.RETURN)
# elem2 = driver.find_element(By.ID, "mat-chip-list-input-1")
# elem2.send_keys("delhi")
#
# time.sleep(3)
# elem2.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
