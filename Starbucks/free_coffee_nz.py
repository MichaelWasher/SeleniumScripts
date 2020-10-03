from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep
import random

# Populate these Values
post_url = "https://starbucksgetone.co.nz/"
first_name = ['example_firstname']
last_names =  ['example_lastname']
domain_name = 'example_domain'

# Setting Element IDs
first_name_input_id = "form_first_name"
last_name_input_id = "form_last_name"
email_address_input_id = "form_email"

email_address = 'starbucks{0}@' + domain_name

def setup_firefox():
    firefox_options = Options()
    firefox_options.add_argument('--dns-prefetch-disable')
    firefox_options.add_argument('--no-sandbox')
    firefox_options.add_argument('--lang=en-US')
    return webdriver.Firefox(executable_path='/usr/local/bin/geckodriver', options=firefox_options)

# Steup Environment
browser = setup_firefox()
counter = 100
# Populate the contents of the form and submit
while(True):
 
    browser.get(post_url)
    browser.execute_script("window.scrollBy(0,1000)");
    first_name_element = browser.find_element_by_id(first_name_input_id)
    first_name_element.click()
    first_name_element.send_keys(first_name)
    
    last_name_element = browser.find_element_by_id(last_name_input_id)
    last_name_element.click()
    last_name_element.send_keys(last_names)
    
    email_element = browser.find_element_by_id(email_address_input_id)
    email_element.click()
    email_element.send_keys(email_address.format(counter))

    tick_box = browser.find_element_by_class_name('ss_alt_icon').click()
    
    # Submit
    browser.find_element_by_class_name('form_submit').click()
    sleep(2)
    counter += 1
