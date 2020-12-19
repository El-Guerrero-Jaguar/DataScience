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
            else:
                ## TODO  Here we can put the code to execute the other scraper
                pass

            print('Transforming job list into JSON')

            job_json_list = [job.to_json() for job in job_list]
            job_json = json.dumps(job_json_list, ensure_ascii = False)

            with open('output.json', 'w', encoding = 'utf-8') as output:
                output.write(job_json)

            print('Finished scraping process')
        except ValueError:
            print('Only numbers are valid as an argument')

    else:
        print('The program needs only one argument (index of website to scrap)')


if __name__ == '__main__':
    run()
