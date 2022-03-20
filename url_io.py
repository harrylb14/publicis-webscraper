import pandas as pd
import os
import openpyxl
from url_columns import URL_COLUMNS


class URLImporter:
	def __init__(self, filepath, sheet_name='Sheet1'):
		self.filepath = filepath
		self.spreadsheet = openpyxl.open(self.filepath)
		self.sheet_name = sheet_name
		self.ws = self.spreadsheet.active
		file, ext = os.path.splitext(self.filepath)
		self.cleaned_filepath = file + '_cleaned' + ext

	def turn_hyperlinks_to_urls(self) -> None:
		"""
		Looks at each cell in the input file, and if it contains a hyperlink, changes the text in that cell
		to be the hyperlink destination.
		Returns new spreadsheet.
		"""
		for row in self.ws.iter_rows():
			for cell in row:
				if cell.hyperlink:
					self.ws[cell.coordinate] = cell.hyperlink.target

		self.spreadsheet.save(self.cleaned_filepath)

	def load_pandas_df(self) -> pd.DataFrame:
		return pd.read_excel(self.cleaned_filepath, self.sheet_name)

	@staticmethod
	def clean_column_name(column_name):
		if '.' in column_name:
			column_name = column_name.split('.')[0]
		return column_name
