from selene import browser
import time
from selene.api import *

browser.open("https://avito-tech-internship-psi.vercel.app/issues")
browser.element('//*[@id="root"]/div/div/div/div[1]/div[1]/div/div').type("Реализация")
time.sleep(2)


