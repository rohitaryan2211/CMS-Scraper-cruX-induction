# This script downloads all the handouts present in the csv provided to it which have links extracted from previous
# script.

# Here, we are using example-CMS_links.csv as an example to extract the handouts from the links present in it.

# Use your BITS mail credentials in the creds.py file in order to log in to your CMS account and scrape handouts.

# Here's a recorded video of demonstration of this code on example-CMS_links.csv - (Use BITS mail to view)
# https://tinyurl.com/handout-scraping-demonstration


from selenium import webdriver
import creds
import time
import csv
from re import search

PATH = "C:\Python\chromedriver.exe"
filename = "example-CMS_links.csv"

# initializing the titles and rows list
fields = []
rows = []

if creds.username == "example@email.com":
    print("Please use your BITS mail credentials in the creds.py inorder to log in to your CMS account.")
    quit()

options = webdriver.ChromeOptions()
preferences = {'download.default_directory': 'D:\Handouts'}
options.add_experimental_option('prefs', preferences)

driver = webdriver.Chrome(PATH, chrome_options=options)
driver.maximize_window()

driver.get("https://cms.bits-hyderabad.ac.in/my/")
driver.find_element_by_xpath('//*[@id="region-main"]/div/div[2]/div/div/div/div/div/div[2]/div[3]/div/a').click()

driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(creds.username)
driver.find_element_by_xpath('//*[@id="identifierNext"]/div/button/span').click()

driver.implicitly_wait(40)

driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(creds.password)
driver.find_element_by_xpath('//*[@id="passwordNext"]/div/button/span').click()

print("Logged into the account.")

time.sleep(5)

with open(filename, 'r') as csvfile:
    # creating a csv reader object
    csvreader = csv.reader(csvfile)

    # extracting field names through first row
    fields = next(csvreader)

    # extracting each data row one by one
    for row in csvreader:
        rows.append(row)

    # get total number of rows
    print("Total no. of rows: %d" % csvreader.line_num)

# printing the field names
print('Field names are:' + ', '.join(field for field in fields))

for row in rows:

    ahref = []
    pattern = "https://cms.bits-hyderabad.ac.in/mod/resource/view.php?"

    # enrolling
    driver.get(f"{row[3]}")
    driver.find_element_by_xpath('//*[@id="id_submitbutton"]').click()

    # Downloading Handouts
    a = driver.find_elements_by_class_name('aalink')
    for elem in a:
        href = elem.get_attribute('href')
        if search(pattern, href):
            ahref.append(href)

    driver.get(ahref[0])
    time.sleep(1)

    # unenrolling
    driver.find_element_by_xpath('//*[@id="action-menu-toggle-2"]').click()
    driver.find_element_by_xpath('//*[@id="action-menu-2-menu"]/div[1]').click()
    driver.find_element_by_xpath('//*[@id="modal-footer"]/div/div[1]/form').click()

    print(f"{row[2]} handout scraped.")

time.sleep(5)

driver.find_element_by_xpath('//*[@id="action-menu-toggle-1"]/span/span[1]').click()
driver.find_element_by_xpath('//*[@id="actionmenuaction-6"]').click()
print("Logged out of the account.")

time.sleep(5)

driver.quit()
print("Program is fully executed.")
