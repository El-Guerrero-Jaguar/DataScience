import argparse
import logging
logging.basicConfig(level=logging.INFO)

from common import config

logger = logging.getLogger(__name__)

def _talent_scraper(talent_site_uid):
    host = config()['talent_sites'][talent_site_uid]['url']

    logging.info('Beginning scraper for {}'.format(host))

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    talent_site_choices = list(config()['talent_sites'].keys())
    parser.add_argument('talent_site', 
                        help='The talent hunting site you want to scrape', 
                        type=str,
                        choices=talent_site_choices)

    args = parser.parse_args()
    _talent_scraper(args.talent_site)