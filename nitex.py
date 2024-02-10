# importing necessary modules
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
import time

# installing chrome driver
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

# opening the event scheduler page
driver.get('url to event scheduler page')

# filling up the event details form
event_title = driver.find_element(by='xpath', value="xpath of event title input element")
event_title.send_keys("Test Event")

event_date = driver.find_element(by='xpath', value="xpath of event date input element")
event_date.send_keys("2024-02-15")

event_participants = driver.find_element(by='xpath', value="xpath of event participants input element")
event_participants.send_keys("participant1@yopmail.com, participant2@yopmail.com")

# submitting the event schedule form
submit_button = driver.find_element(by='xpath', value="xpath of submit button")
submit_button.click()

time.sleep(3)

# getting all events list elements 
events_list = driver.find_elements(by='xpath', value="xpath of events list")

# assuming the latest event is the first one in the list
latest_event = events_list[0]

# getting event details
event_title = latest_event.find_element(by='xpath', value="xpath of event title element").text
event_date = latest_event.find_element(by='xpath', value="xpath of event date element").text
event_participants = latest_event.find_element(by='xpath', value="xpath of event participants element").text

# list of assertion errors to be updated
errors = []

# verifying event details
# veriying the event title
try:
    assert event_title == "Test Event"
except AssertionError as e:
    errors.append("Assertion error for event title")

# verifying the event date
try:
    assert event_date == "2024-02-09"
except AssertionError as e:
    errors.append("Assertion error for event date")

# verfying the event participants
try:
    assert event_participants == "participant1@yopmail.com, participant2@yopmail.com"
except AssertionError as e:
    errors.append("Assertion error for event participants")

# printing verification result
if not errors:
    print("Event details verified successfully.")
else:
    print("Event details verification failed.")
    print("Errors:")
    # all errors will be printed
    for error in errors:
        print(error)

time.sleep(3)

# closing the webdriver
driver.close()