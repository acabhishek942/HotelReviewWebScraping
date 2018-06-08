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
