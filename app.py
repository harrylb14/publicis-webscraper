import sys

from crawler import Crawler
from s3_service import S3Service
from url_columns import URL_COLUMNS
from url_io import URLImporter


def run_crawler_and_save_to_s3(filepath: str = "/Users/harry.lingardbright/Downloads/ProgressPoint_MVP_Company_List-2.xlsx"):
	crawler = Crawler()
	url_importer = URLImporter(filepath)
	url_importer.turn_hyperlinks_to_urls()
	df = url_importer.load_pandas_df()
	for column in df.columns:
		if url_importer.clean_column_name(column) in URL_COLUMNS:
			print(f"Processing column: {column}")
			url_column = df[column]
			html_column = crawler.scrape_url_column(url_column)
			df[column] = html_column

	print('Finished Processing')
	csv = df.to_csv()
	S3Service().upload_csv_to_s3(csv)
	print('Exported data to S3')


if __name__ == "__main__":
	run_crawler_and_save_to_s3(sys.argv[1])
