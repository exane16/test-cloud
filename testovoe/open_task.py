from selene import browser
import time
from selene.api import *

browser.open("https://avito-tech-internship-psi.vercel.app/issues")
browser.element('//*[@id="root"]/div/div/div/div[2]/div[1]/div').click()
time.sleep(2)