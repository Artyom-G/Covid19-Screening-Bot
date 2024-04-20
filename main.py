from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException, WebDriverException
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from keep_alive import keep_alive
import requests
import schedule
import time

class CovidScreenBot:
	def __init__(self, _username, _password):
		print("Instantiating CovidBot...")
		self.element = None
		options = Options()
		options.add_argument("--headless")
		options.add_argument("--disable-dev-shm-usage")
		options.add_argument("--no-sandbox")
		print("Starting Firefox")
		self.wd = webdriver.Firefox(options=options)
		self.wd.set_page_load_timeout(15)
		print("CovidBot Created")
		print("Starting CovidBot....")
		self.wd.get("https://screen.wrdsb.ca/login.aspx?ReturnUrl=%2f")
		print("At screen.wrdsb.ca")
		print(f"Logging into {_username}")
		time.sleep(1)
		self.fastrack = WebDriverWait(self.wd, 3).until(ec.visibility_of_element_located((By.ID, "tbPalId")))
		self.textboxUsername = self.wd.find_element_by_id("tbPalId")
		self.textboxUsername.send_keys(_username)
		self.textboxUsername.submit()
		self.fastrack = WebDriverWait(self.wd, 3).until(ec.visibility_of_element_located((By.ID, "tbPassword")))
		self.textboxPassword = self.wd.find_element_by_id("tbPassword")
		self.textboxPassword.send_keys(_password)
		self.textboxPassword.submit()
		self.fastrack = WebDriverWait(self.wd, 3).until(ec.visibility_of_element_located((By.ID, "btnLogin")))
		self.loginButton = self.wd.find_element_by_id("btnLogin")
		self.loginButton.click()
		print("Logged in")
		self.fastrack = WebDriverWait(self.wd, 3).until(ec.visibility_of_element_located((By.ID, "rbGreen")))
		self.greenCheckmarkButton = self.wd.find_element_by_id("rbGreen")
		self.greenCheckmarkButton.click()
		self.fastrack = WebDriverWait(self.wd, 3).until(ec.visibility_of_element_located((By.ID, "btnSubmit")))
		self.submitButton = self.wd.find_element_by_id("btnSubmit")
		self.submitButton.click()
		print("Self screening complete")

	def close(self):
		self.wd.quit()
		print("Bot Shut Down")

cb = CovidScreenBot("USERNAME", "PASSWORD")
keep_alive()