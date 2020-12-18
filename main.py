"""
This module is the entry point for the scraping application
"""

import sys
import json
import gob_scraper


def run():
    """
    Entry point of the program
    """
    if len(sys.argv) == 2:
        try:
            option = int(sys.argv[1])

            if option == 1:
                job_list = gob_scraper.scrap_category_list()
                print(*job_list, sep='\n')

            else:
                ## TODO  Here we can put the code to execute the other scraper
                pass
        except ValueError:
            print('Only numbers are valid as an argument')

    else:
        print('The program needs only one argument (index of website to scrap)')


if __name__ == '__main__':
    run()
