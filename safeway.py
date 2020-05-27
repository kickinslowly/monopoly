import pytesseract
import os
import re
from PIL import Image
from selenium import webdriver
import time
import keyboard
# I'm a rookie and still use print statements to help me track how my codes working.
# Don't know why, but I had to point to the .exe to make the things work.
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

code_list = []
used_code_list = []
counter = 0

# This loops through folder of images, extracts text, finds monopoly pattern and adds it to code_list.
for file in os.listdir(r'C:\Users\Humanist\PycharmProjects\first\images'):
    counter += 1
    img = Image.open(r'C:\Users\Humanist\PycharmProjects\first\images\\' + file)

    text = pytesseract.image_to_string(img)
    print(text)
    codeRegex = re.compile(r'....-....-....-....')
    mo = codeRegex.findall(text)
    print(mo)
    try:
        code_list.append(mo[0])
    except IndexError:
        print(f'Excepting IndexError for {file}')
        pass
print(counter)
browser = webdriver.Firefox()
browser.get('https://www.shopplaywin.com/')
time.sleep(2)
elem = browser.find_element_by_css_selector('a.btn.btn-primary.btn-block.mt-sm-3')
elem.click()
# This css_selector will be specific to the store you use, I use Safeway so mine was store-12.
# To find css_selector chrome> Inspect element on page, right click element in dev tools > copy css selector
elem = browser.find_element_by_css_selector('button.store.square.store-12')
elem.click()
elem = browser.find_element_by_css_selector('button.d-block:nth-child(1)')
elem.click()
elem = browser.find_element_by_css_selector('#label-email')
elem.click()
# Use your shopplaywin email login here.
elem.send_keys('exampleemail@example.com')
elem = browser.find_element_by_css_selector('#password')
elem.click()
# Use your shopplaywin password here
elem.send_keys('ExamplePassword123!')
keyboard.press_and_release('enter')
time.sleep(5)
keyboard.press_and_release('esc')

for code in code_list:
    elem = browser.find_element_by_css_selector('#code')
    elem.click()
    elem.send_keys(code)
    keyboard.press_and_release('enter')
    time.sleep(2)
    try:
        elem = browser.find_element_by_css_selector('button.btn-block:nth-child(3)')
        elem.click()
    except:
        elem = browser.find_element_by_css_selector('button.m-1')
        elem.click()
    time.sleep(1)
    elem = browser.find_element_by_css_selector('#code')
    used_code_list.append(code)

print(code_list)
print(used_code_list)






