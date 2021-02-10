#!/usr/bin/python

#Selenium
"""
Selenium is an open-source project that contains tools and libraries which enable and support the automation of web browsers.
It provides: 
 - Extensions to emulate user interaction with browsers
 - A distribution server for scaling browser allocation
 - The infrastructure for implementations of the W3C WebDriver specification 
   + Allows for interchangeable code for all major web browser
"""

#---[ Install Selenium ]------------------------------------------------------------------------------------------------------------------------------
#Selenium can be installed using the command: pip install selenium
#python -m pip install selenium
#Collecting selenium
#  Downloading selenium-3.141.0-py2.py3-none-any.whl (904 kB)
#     |████████████████████████████████| 904 kB 10.3 MB/s
#Requirement already satisfied: urllib3 in /usr/lib/python3/dist-packages (from selenium) (1.25.8)
#Installing collected packages: selenium
#Successfully installed selenium-3.141.0

#Linux
#Download the geckodriver for Firefox: https://github.com/mozilla/geckodriver/releases
#tar -xvzf geckodriver*
#chmod +x geckodriver
#sudo mv geckodriver /usr/local/bin/

#Windows
#Download the geckodriver for Firefox: https://github.com/mozilla/geckodriver/releases
#Place the driver in a folder [C:\Program Files\Python39\drivers\geckodriver.exe]
#Add the folder location to PATH.

#---[Locator Strategies]------------------------------------------------------------------------------------------------------------------------------
#There are various strategies that can be used to find elements on a page.
"""
Locators 	                          Description
find_element_by_id 	                The first element with the id attribute value matching the location will be returned.
find_element_by_name 	              The first element with the name attribute value matching the location will be returned.
find_element_by_xpath 	            The first element with the xpath syntax matching the location will be returned.
find_element_by_link_text           The first element with the link text value matching the location will be returned.
find_element_by_partial_link_text 	The first element with the partial link text value matching the location will be returned.
find_element_by_tag_name 	          The first element with the given tag name will be returned.
find_element_by_class_name 	        The first element with the matching class attribute name will be returned.
find_element_by_css_selector 	      The first element with the matching CSS selector will be returned.

<form id="loginForm">
login_form = driver.find_element_by_id('loginForm')

<input name="username" type="text" />
element = driver.find_element_by_name('username')

<html> 
 <body> 
  <form id="loginForm"> 
login_form = driver.find_element_by_xpath("/html/body/form[1]")

<a href="continue.html">Continue</a>
login_form = driver.find_element_by_link_text('Continue')
login_form = driver.find_element_by_partial_link_text('Conti')

<h1>Welcome</h1>
login_form = driver.find_element_by_tag_name('h1')

<p class="content">Site content goes here.</p> 
content = driver.find_element_by_class_name('content')

<p class="content">Site content goes here.</p>
content = driver.find_element_by_css_selector('p.content')

"""

#---[Action Methods ]---------------------------------------------------------------------------------------------------------------------------------
#One can perform a huge number of operations using Action chains such as click, right-click, etc. 
# Here is a list of important methods used in Action chains.

"""
Method 	                      Description
click 	                      Clicks an element.
click_and_hold 	              Holds down the left mouse button on an element.
context_click 	              Performs a context-click (right click) on an element.
double_click 	                Double-clicks an element.
drag_and_drop 	              Holds down the left mouse button on the source element, then moves to the target element and releases the mouse button.
drag_and_drop_by_offset 	    Holds down the left mouse button on the source element, then moves to the target offset and releases the mouse button.
key_down 	                    Sends a key press only, without releasing it.
key_up 	                      Releases a modifier key.
move_by_offset 	              Moving the mouse to an offset from current mouse position.
move_to_element 	            Moving the mouse to the middle of an element.
move_to_element_with_offset 	Move the mouse by an offset of the specified element, Offsets are relative to the top-left corner of the element.
perform 	                    Performs all stored actions.
pause 	                      Pause all inputs for the specified duration in seconds
release 	                    Releasing a held mouse button on an element.
reset_actions 	              Clears actions that are already stored locally and on the remote end
send_keys 	                  Sends keys to current focused element.
"""

#---[ Exceptions ]------------------------------------------------------------------------------------------------------------------------------------
#Exceptions are of primary use when you are writing development ready code especially which is at a high risk of causing certain type of exception. 
#So here is list of all exceptions in Selenium Python.

"""
Exception 	                      Description
--------------------------------  --------------------------------------------------------------------------------------------------------------------
ElementClickInterceptedException 	The Element Click command could not be completed because the element receiving the events is obscuring the element 
                                  that was requested clicked.
ElementNotInteractableException 	Thrown when an element is present in the DOM but interactions with that element will hit another element do to paint 
                                  order
ElementNotSelectableException 	  Thrown when trying to select an unselectable element.
ElementNotVisibleException 	      Thrown when an element is present on the DOM, but it is not visible, and so is not able to be interacted with.
ErrorInResponseException 	        Thrown when an error has occurred on the server side.
ImeActivationFailedException 	    Thrown when activating an IME engine has failed.
ImeNotAvailableException 	        Thrown when IME support is not available.
InsecureCertificateException 	    Navigation caused the user agent to hit a certificate warning, which is usually the result of an expired or invalid 
                                  TLS certificate.
InvalidArgumentException 	        The arguments passed to a command are either invalid or malformed.
InvalidCookieDomainException 	    Thrown when attempting to add a cookie under a different domain than the current URL.
InvalidCoordinatesException 	    The coordinates provided to an interactions operation are invalid.
InvalidElementStateException 	    Thrown when a command could not be completed because the element is in an invalid state.
InvalidSelectorException 	        Thrown when the selector which is used to find an element does not return a WebElement.
InvalidSessionIdException 	      Occurs if the given session id is not in the list of active sessions, meaning the session either does not exist or 
                                  that it’s not active.
InvalidSwitchToTargetException 	  Thrown when frame or window target to be switched doesn’t exist.
MoveTargetOutOfBoundsException 	  Thrown when the target provided to the ActionsChains move() method is invalid, i.e. out of document.
NoAlertPresentException 	        Thrown when switching to no presented alert.
NoSuchAttributeException 	        Thrown when the attribute of element could not be found.
NoSuchCookieException 	          No cookie matching the given path name was found amongst the associated cookies of the current browsing context’s 
                                  active document.
NoSuchFrameException 	            Thrown when frame target to be switched doesn’t exist.
NoSuchWindowException 	          Thrown when window target to be switched doesn’t exist.
StaleElementReferenceException 	  Thrown when a reference to an element is now “stale”.
TimeoutException 	                Thrown when a command does not complete in enough time.
UnableToSetCookieException 	      Thrown when a driver fails to set a cookie.
UnexpectedAlertPresentException 	Thrown when an unexpected alert is appeared.
UnexpectedTagNameException 	      Thrown when a support class did not get an expected web element 
"""

#---[ Simple Script ]---------------------------------------------------------------------------------------------------------------------------------
from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("https://www.geeksforgeeks.org/")

time.sleep(5)

element = driver.find_element_by_class_name("gfg-icon_search")

element.click()

searchbox = driver.find_element_by_id("gsc-i-id1")

searchbox.send_keys("Arrays")

footer_address = driver.find_element_by_class_name("footer-wrapper_branding-address")

print(footer_address.text)                    #5th Floor, A-118,
                                              #Sector-136, Noida, Uttar Pradesh - 201305

#---[ Action Chains ]---------------------------------------------------------------------------------------------------------------------------------
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Firefox()
action = ActionChains(driver)

driver.get("https://www.geeksforgeeks.org/")

action.pause(5)

element = driver.find_element_by_class_name("gfg-icon_search")

action.click(on_element = element)

searchbox = driver.find_element_by_id("gsc-i-id1")

action.send_keys_to_element(searchbox, "Arrays")

action.perform()

#You can also put all actions together in one chain
action.send_keys_to_element(searchbox, "Arrays").perform()

#---[ Exception Catching ]----------------------------------------------------------------------------------------------------------------------------
from selenium import webdriver 
import time
  
driver = webdriver.Firefox() 

driver.get("https://www.geeksforgeeks.org/") 

time.sleep(5)
  
element = driver.find_element_by_link_text("abrakadabra") 

print(element.click())                      #selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: abrakadabra 

#---[ Retrieve URL ]----------------------------------------------------------------------------------------------------------------------------------
from selenium import webdriver 
  
driver = webdriver.Firefox() 

driver.get("https://www.geeksforgeeks.org/") 

print(driver.current_url)                     #https://www.geeksforgeeks.org/

#---[ Retrieve Title ]--------------------------------------------------------------------------------------------------------------------------------
from selenium import webdriver 
  
driver = webdriver.Firefox() 

driver.get("https://www.geeksforgeeks.org/") 

print(driver.title)                             #GeeksforGeeks | A computer science portal for geeks

#---[ Window Control ]--------------------------------------------------------------------------------------------------------------------------------
from selenium import webdriver 
import time
  
driver = webdriver.Firefox() 

driver.get("https://www.geeksforgeeks.org/") 

driver.get("https://duckduckgo.com") 

time.sleep(5)

print(driver.window_handles)                  #['15']

handle = driver.current_window_handle

print(handle)                                 #15

driver.switch_to.window(handle)

driver.refresh()

driver.maximize_window()

driver.minimize_window()

#close current window
driver.close()

#close all windows
driver.quit()