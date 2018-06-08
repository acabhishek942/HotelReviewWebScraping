from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from random import randint
import datetime
import os
import time
import pandas as pd

url = 'https://www.makemytrip.com/hotels/'

# hard-coded hotel name
hotel_name = 'The Chancery Pavilion'

# perform search relative to current date
current_time = datetime.datetime.now()
current_time.strftime("%m/%d/%Y")

# some parameters to customize the search
nights_stay = 2
weeks_from_now_to_look = 13
how_many_weeks_to_check = 4

for week in range(how_many_weeks_to_check):
    start_date = current_time + datetime.timedelta(days=week*7) + datetime.timedelta(days=weeks_from_now_to_look*7)
    end_date = start_date + datetime.timedelta(days=nights_stay)
    print(start_date.strftime("%d %b, %a") + ' to ' + end_date.strftime("%d %b, %a"))

css_selector_calendar = '.ui-datepicker-calendar tbody tr td a'
id_destination_textbox = 'hp-widget__sDest'
id_checkin_textbox = 'hp-widget__chkIn'
id_checkOut_tetbox = 'hp-widget__chkOut'
id_search_button = 'searchBtn'
id_user_review_tab = 'details-nav-userreview'
css_selector_review_sources = '.htD-user-rating-company'
css_selector_reviews_content = 'hlD-user-review-list li'

chromedriver_path = '../webdrivers/chromedriver'
os.environ["webdriver.chrome.driver"] = chromedriver_path

driver = webdriver.Chrome(chromedriver_path)

time_delay = randint(3,6)


# Open the MMT hotel search website
driver.get(url)
time.sleep(time_delay)

# set the checkin and checkout date
# start_date = current_time + datetime.timedelta(days=week*7) + datetime.timedelta(days=weeks_from_now_to_look*7)
# end_date = start_date + datetime.timedelta(days=nights_stay)

# enter the destinataion
destinataion_hotel = driver.find_element_by_id(id_destination_textbox)
destinataion_hotel.click()
destinataion_hotel.clear()
destinataion_hotel.send_keys(hotel_name)

time.sleep(time_delay)

# click on the check in date textbox
checkin_date_element=driver.find_element_by_id(id_checkin_textbox)
checkin_date_element.click()

time.sleep(time_delay)

# click on the checkout date textbox
checkout_date_element=driver.find_element_by_id(id_checkOut_tetbox)
checkout_date_element.click()

time.sleep(time_delay)

# click on the search button
driver.find_element_by_id(id_search_button).click()
time.sleep(time_delay)
time.sleep(time_delay)

# need to put double delay above because 'user review takes a bit to load'

# click on the user review tab
driver.find_element_by_id(id_user_review_tab).click()

time.sleep(time_delay)

# close web driver
driver.close()
