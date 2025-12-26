from selene import browser
import time
from selene.api import *

browser.open("https://avito-tech-internship-psi.vercel.app/issues")
browser.element(by.text("Создать задачу")).click()
browser.element('//*[@id=":r1j:"]').click
browser.element("/html/body/div[2]/div[3]/div/div[3]/div/div").click()
browser.element('//*[@id=":r1t:"]/li[1]').click()
browser.element("/html/body/div[2]/div[3]/div/div[4]/div/div").click()
browser.element('//*[@id=":r1u:"]/li[1]').click()
browser.element("/html/body/div[2]/div[3]/div/div[6]/div/div").click()
browser.element('//*[@id=":r20:"]/li[2]').click()
browser.element(by.text("Создать")).click()
time.sleep(2)





