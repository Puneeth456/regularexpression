
a=100

def f1():
    print("inside f1")


import re

s=input("Enter email Id")
m=re.fullmatch("[a-zA-Z0-9_.]*@gmail.com",s)
if m!=None:
    print("valid email Id")
else:
    print("Invalid email Id")



import re
s=input("Enter the email Id")
m=re.fullmatch("[a-zA-Z0-9_.]{5-25}@gmail.com",s)
if m!=None:
    print("valid email Id")
else:
    print("Invalid email Id")


Regular expression is for client side or server side validation


Client side validation should be handled using html or java script


client side validation avoids  more request to the server by making  initial check


import re

s=input("enter the mobile number")
m=re.fullmatch("91-([0-9]){10}",s)
if m!=None:
    print("Valid email Id")
else:
    print("Invalid email Id")


import re

s=input("enter the mobile number")
m=re.fullmatch("91-([0-9]){10}",s)
if m!=None:
    print("Valid email Id")
else:
    print("Invalid email Id")


print("Program ended")



Whenever developer make some changes to the repository(push the code)

1) Deployment should be happening automatically
2) make sure deployment is successfull
3) once deployment is done then run the automation script


Jenkins.war file should be run for each and every  not instance

Jenkins.war file should be run for each and every not instance




from abc import *


class flight(ABC):
    @abstractmethod
    def run(self):
        pass




@abstractmethod
def fly(self):
    pass


f1=flight()


In python there is no concept of interface in python.

but we can simulate interface concept by making all method abstract.


Locators:
web page
web element:

web page can have a user name field and password field(text box) this kind of fileds will be called as web element.
each and every web element will have attribute name and attribute
not value
there is no limit for attribute name and attribute value it purely depends on the ui developer


webelement              tag name                        mandatory an and av

text field          input                        type=text, type=email, type ="password"

button                 button /input(            type=submit


dropdown                select

Radio                  input             type =radio


images                      img


tables                      table

link                a                       href





text filed              input   type="email" type="password" type="text"

button                 input/button  type=submit

dropdown                select

Radio                     input    type=raido


images      imng

table      tab;exit(


    link            a   href
)


Grid

Parallel execution
all the test scripts should be independent
hub will distibute testcripts
one hub can hae any number of nodes
we can perform parallex eceuction on the same machine as well./


Grid

Parallel execution
all the test scripts should be independent
hub will distribute the testscripts




gRID

pARALLELEXECT
we can perform parallel executon on the same machine as well



from selenium import webdriver


qspider=webdriver.Chrome()
qspider.get("https://www.facebook.com/")


from selenium import webdriver

qspider=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/New folder (11)/chromedriver.exe")
qspider.get("https://www.facebook.com/")
qspider.find_element_by_id("email").send_keys("9000000000")
qspider.find_element_by_id("pass").send_keys("999999999999")




from selenium import webdriver

qspider=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/New folder (11)/chromedriver.exe")
qspider.find_element_by_class_name("grp-button grp-default").click()


locators are used to identify the web elment
A single web element can have multiple ways of
not identification





from selenium import webdriver

qspider=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/New folder (11)/chromedriver.exe")
qspider.get("https://www.facebook.com/")
qspider.find_element_by_xpath("//input[@id='email']").send_keys("9999999999")
qspider.find_element_by_id("pass").send_keys("0000000000")
qspider.find_element_by_xpath("//input[@id='u_0_b']").click()


from selenium import webdriver

browser='ie'

if (browser=='chrome'):
    driver=webdriver.Chrome(executable_path="C:/Users/Admin/Downloads/New drivers find/chromedriver.exe")
elif (browser=='ff'):
    driver=webdriver.Firefox(executable_path="C:/Users/Admin/Downloads/New drivers find/geckodriver.exe")
elif  (browser=='ie'):
    driver=webdriver.Ie(executable_path="C:/Users/Admin/Downloads/New drivers find/IEDriverServer.exe")

driver.get("https://www.facebook.com/")
driver.implicitly_wait(30)


driver.find_element_by_name("email").send_keys("9999999999")
driver.find_element_by_name("pass").send_keys("sarigampappa")
driver.find_element_by_xpath("//input[@value='Log In']").click()



from selenium import webdriver


browser='ff'


if(browser=='ie'):
    driver=webdriver.Ie()
elif(browser=='chrome'):
    driver=webdriver.Chrome()
elif(browser=='ff'):
    driver=webdriver.Firefox()

driver.implicitly_wait(30)


import select

from selenium import webdriver

driver=webdriver.Chrome()
driver.get("https://www.facebook.com/")
driver.implicitly_wait(30)

day=driver.find_element_by_name("birthday_day")
s1=select(day)
s1.select_by_visible_text("5")



month=driver.find_element_by_id("month")
s2=select(month)
s2.select_by_value("2")



year=driver.find_element_by_id("Year")
s3=select(year)
s3.select_by_index("5")






