from selene import browser
import time
from selene.api import *

browser.open("https://avito-tech-internship-psi.vercel.app/issues")
browser.element(by.text("Проекты")).click()
time.sleep(2)