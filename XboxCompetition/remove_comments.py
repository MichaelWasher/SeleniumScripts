from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep


# Customizeable Values
email_address = ""
password = ''
activity_url = ""
profile_id = ""

assert (email_address and password and activity_url and profile_id), "Populate the script" \
    "variables otherwise the script will not be able to run."


def setup_firefox():
    firefox_options = Options()
    firefox_options.add_argument('--dns-prefetch-disable')
    firefox_options.add_argument('--no-sandbox')
    firefox_options.add_argument('--lang=en-US')
    return webdriver.Firefox(executable_path='/usr/local/Cellar/geckodriver/0.24.0/bin/geckodriver', options=firefox_options)


# Login
browser = setup_firefox()
browser.get('https://www.facebook.com/')
signup_elem = browser.find_element_by_id('email')
signup_elem.send_keys(email_address)

login_elem = browser.find_element_by_id('pass')
login_elem.send_keys(password)

ins = browser.find_elements_by_tag_name('input')
for x in ins:
    if x.get_attribute('value') == 'Log In':
        x.click() # here logged in
        break

sleep(1)

# Setting Variables
browser.get(activity_url)
sleep(1)
xpath_command = "//*/a[contains(@href,'profile_id=" + profile_id + "')][text() = 'Delete']"

# Click first delete
while True:
    browser.find_element_by_xpath(
        xpath_command
    ).click()
    sleep(1)