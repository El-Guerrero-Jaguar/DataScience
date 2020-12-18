"""
This module is the entry point for the scraping application
"""
import json
import gob_scraper


def run():
    """
    Entry point of the program
    """
    categories_raw = gob_scraper.send_request(gob_scraper.CATEGORY_URL)['data']
    categories = [info['id'] for info in categories_raw]
    
    print(gob_scraper.get_company_data(2129))


if __name__ == '__main__':
    run()
