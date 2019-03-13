from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.firefox.options import Options
from time import sleep
import random as rand

BUSINESS_DOMAIN = ""
WEBSITE_URL = ""

assert BUSINESS_DOMAIN, "A business domain with a catch-all email address must be provided."
assert WEBSITE_URL, "A WEBSITE url must be provided. Please populate the starting constants."

SUBURBS = ["Frantkon", "Rototuna", "Hamilton East", "Tamahere", "Huntington", "Flagstaff", "Chartwell",
           "Fairview Downs", "Fairfield", "Hillcrest", "Hamilton Central", "Glenview", "Dinsdale", ]
TOTAL_MONTHS = 12


def subscribe_email(browser, first_name, last_name, select_index, male_gender, email, suburb):
    '''
    Used to subscribe a single email address
    NOTE: Assumes that the current location is
    https://www.chartwellshopping.co.nz/vip
    '''
    # F_NAME
    el_tb = browser.find_element_by_id("mce-FNAME")
    el_tb.send_keys(first_name)

    # L_NAME
    el_tb = browser.find_element_by_id("mce-LNAME")
    el_tb.send_keys(last_name)

    # Birthday
    el_select = Select(browser.find_element_by_name("merge_fields[MMERGE3]"))
    el_select.select_by_index(select_index)

    # M = mce-MMERGE4-m , F = mce-MMERGE4-f
    if male_gender:
        el_rb = browser.find_element_by_id("mce-MMERGE4-m")
    else:
        el_rb = browser.find_element_by_id("mce-MMERGE4-f")
    browser.execute_script("arguments[0].click();", el_rb)

    # EMAIL
    el_tb = browser.find_element_by_id("mce-EMAIL")
    el_tb.send_keys(email)

    # Suburb
    el_tb = browser.find_element_by_id("suburb")
    el_tb.send_keys(suburb)

    # Status
    el_cb = browser.find_element_by_name("status")
    browser.execute_script("arguments[0].click();", el_cb)

    el_btn = browser.find_element_by_id("mc-form-btn")
    browser.execute_script("arguments[0].click();", el_btn)
    sleep(1)


def setup_firefox():
    firefox_options = Options()
    firefox_options.add_argument('--lang=en-US')
    return webdriver.Firefox(executable_path='/usr/local/Cellar/geckodriver/0.24.0/bin/geckodriver', options=firefox_options)


def setup_browser():
    return setup_firefox() # TODO Change the browser type to unseen when not in debug


def get_email_link(fname, lname):
    return f'{fname.lower()}.{lname.lower()}@{BUSINESS_DOMAIN.lower()}'


def get_birthday():
    return rand.randint(0, TOTAL_MONTHS-1)


def get_gender(gender):
    return True if gender == "M" else False


def get_suburb():
    return SUBURBS[rand.randint(0, len(SUBURBS)-1)]


def main():
    # parse the male nameslist file
    browser = setup_browser()
    with open("name-list.txt", "r") as name_file:
        for line in name_file:
            try:
                # Setup the browser and change to page
                browser.get(WEBSITE_URL)

                # Clean the input and get values
                line = line.strip()
                [first_name, last_name, gender] = line.split()
                # Collect other values
                email_address = get_email_link(first_name, last_name)
                gender = get_gender(gender)
                birthday = get_birthday()
                suburb = get_suburb()

                # Subscribe to Email
                subscribe_email(browser, first_name, last_name, birthday, gender, email_address, suburb)
            except Exception as e:
                print(f"The name {line} has failed.")
                print(e)
                continue

if __name__ == "__main__":
    main()
