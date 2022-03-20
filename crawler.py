import os

from bs4 import BeautifulSoup
from selenium import webdriver

from webdriver_settings import options, capabilities


class Crawler:

	def __init__(self):
		if os.name == "nt":
			self.browser = webdriver.Chrome('C:\chromedriver_win32\chromedriver.exe', options=options)
		else:
			self.browser = webdriver.Chrome(options=options, desired_capabilities=capabilities, port=4444)

	def fetch_unstructured_text_from_url(self, url: str) -> str:
		"""
		Returns full HTML from a webpage, given a URL. Returns an error string if an error is thrown.
		"""
		try:
			print(f'Fetching from {url}')
			self.browser.get(url)
			content = self.browser.page_source
			html = BeautifulSoup(content, features="html.parser")

		except:
			html = "Unable to get data."

		return html

	def scrape_url_column(self, column) -> list:
		"""
		Returns a list of HTML strings, containing HTML from each URL in a list of URLs.
		"""

		unstructured_text_column = []
		for url in column:
			unstructured_text_column.append(self.fetch_unstructured_text_from_url(url))

		return unstructured_text_column
