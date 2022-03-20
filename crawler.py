import os
import pandas as pd
from selenium import webdriver
from bs4 import BeautifulSoup
from webdriver_settings import options, capabilities
from url_io import URLImporter
from url_columns import URL_COLUMNS


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
		:param column:
		:return:
		"""

		unstructured_text_column = []
		for url in column:
			unstructured_text_column.append(self.fetch_unstructured_text_from_url(url))

		return unstructured_text_column


if __name__ == "__main__":
	crawler = Crawler()
	url_importer = URLImporter("/Users/harry.lingardbright/Downloads/ProgressPoint_MVP_Company_List-2.xlsx")
	url_importer.turn_hyperlinks_to_urls()
	df = url_importer.load_pandas_df()
	for column in df.columns:
		if url_importer.clean_column_name(column) in URL_COLUMNS:
			print(f"Processing column: {column}")
			url_column = df[column]
			html_column = crawler.scrape_url_column(url_column)
			df[column] = html_column
	x = df
	y = True
