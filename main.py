"""
This module is the entry point for the scraping application
"""

import sys
import json
import logging
import argparse
import gob_scraper
import talent_placement_objects as talent
from common import config
from graphqldb import send_graphql_data
from list_vacant_eterprice import ListVacant as lstvacant


logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def scrap_gob():
    """
    Executes GetOnBoard scraping
    """
    try:
        job_list = gob_scraper.scrap_category_list()
        
        print('Transforming job list into JSON')

        job_json_list = [job.to_json() for job in job_list]
        job_json = json.dumps(job_json_list, ensure_ascii = False)

        with open('gob_output.json', 'w', encoding = 'utf-8') as output:
            output.write(job_json)
            
        #print(job_json_list[:2])
        send_graphql_data(job_json_list)

        # send_graphql_data([{"title":"titulito",
        # "company":"platzi",
        # "description":"description",
        # "town":"town",
        # "modality":"modality",
        # "date":"2020-10-12",
        # "salary":"salary",
        # "urlVacant":"urlVacant",
        # "urlCompany":"urlCompany"},
        # {"title":"otro mas",
        # "company":"la mejor",
        # "description":"description",
        # "town":"town",
        # "modality":"modality",
        # "date":"2020-10-12",
        # "salary":"salary",
        # "urlVacant":"urlVacant",
        # "urlCompany":"urlCompany"}])

    except ValueError:
        print('Only numbers are valid as an argument')


def scrap_empleosti(talent_site_uid):
    """
    Executes EmpleosTI scraping
    """
    host = config()['talent_sites'][talent_site_uid]['url']

    logging.info('Beginning scraper for {}'.format(host))
    homepage = talent.HomePage(talent_site_uid, host)

    total_list = []
    for link in homepage.talent_links:
        total_list.append(lstvacant.vacant_link(link))
    
    #print(total_list)

    with open('totjob.json', 'w') as file:
        json.dump(total_list, file, indent=4)
        
    #return total_list


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    talent_site_choices = list(config()['talent_sites'].keys())

    parser.add_argument('talent_site',
                        help = 'The talent hunting site you want to scrape', 
                        type = str,
                        choices = talent_site_choices)


    args = parser.parse_args()

    if talent_site_choices[0] == args.talent_site:
        scrap_gob()

    else:
        scrap_empleosti(args.talent_site)

    print('Finished scraping process')
