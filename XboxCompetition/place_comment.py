from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from time import sleep
import random

# Populate these Values
email_address = ""
password = ""
tagged_friends = []
tagged_friend_ids = []
post_url = ""

assert (email_address and password and tagged_friends and tagged_friend_ids and post_url), "Populate the script" \
    "variables otherwise the script will not be able to run."

comment_messages = ["xbox pls", "your boy needs the xbox", "I won't be friends with you if I don't win.",
                    "But I'm disabled at the moment, so please help a brother out!",
                    "Bored", "Nothing to do all day but post on this. YOU COULD FIX THAT!"]

def setup_firefox():
    firefox_options = Options()
    firefox_options.add_argument('--dns-prefetch-disable')
    firefox_options.add_argument('--no-sandbox')
    firefox_options.add_argument('--lang=en-US')
    return webdriver.Firefox(executable_path='/usr/local/Cellar/geckodriver/0.24.0/bin/geckodriver', options=firefox_options)

# Login to Facebook
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

MAX_COUNT = 10

counter = 1

# Go to post in $post_url and comment tagging friends
while(True):
    friend_index = random.randint(0, len(tagged_friends)) - 1
    comment_message_index = random.randint(0, len(comment_messages)) - 1 # Minus 1 for length > index conversion

    # Setting Variables
    tagged_friend_xpath = '//*/input[@type="checkbox"][@value="' + tagged_friend_ids[friend_index] +'"]'
    comment_message = comment_messages[comment_message_index]
    tagged_friend = tagged_friends[friend_index]

    browser.get(post_url)

    # Search for friend to tag
    browser.find_element_by_name('view_mention').click()
    sleep(1)


    el = browser.find_element_by_name('query')
    el.send_keys(tagged_friend)
    el.send_keys(Keys.ENTER)
    sleep(1)

    browser.find_element_by_xpath(
        tagged_friend_xpath
    ).click()

    browser.find_element_by_xpath(
        '//*/input[@type="submit"][@name="done"]'
    ).click()

    # Write the comment
    ins = browser.find_element_by_name('comment_text')
    ins.send_keys(comment_message)

    # Submit
    browser.find_element_by_name('post').click()
    sleep(5)
    counter = counter + 1

    if counter % MAX_COUNT == 0:
        sleep(60)

