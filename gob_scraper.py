"""
This module scraps the Get on Board website using its REST API
"""

import requests
from datatypes import JobData, CompanyData


BASE_URL = 'https://www.getonbrd.com/api/v0'
CATEGORY_URL = f'{BASE_URL}/categories'
COMPANY_URL = f'{BASE_URL}/companies'
JOBS_URL = f'{CATEGORY_URL}/$CATEGORY_ID/jobs'
COMPANY_DETAIL_URL = f'{COMPANY_URL}/$COMPANY_ID'


def _parse_endpoint(endpoint, key, value):
    """
    Returns the endpoint with values parameters replaced with their values
    """
    return endpoint.replace(key, str(value))


def _print_response_success(response, index):
    """
    Prints an output according to the response's status
    """
    request_url = response.request.url
    print(f'\n{"*" * 70}')

    if response.status_code == 200:
        print(f'SUCCESS! Obtained response #{index} for {request_url}\n')        
    else:
        print(f'\n{"*" * 70}')
        print(f'Problem with the request to {request_url}. ')
        print(f'Response #{index}: ')
        print(response.status_code)

    print(response.json())
    print(f'{"*" * 70}\n')


def scrap_category_list(verbosity = False):
    """
    Retrieves and returns a list of jobs for every category
    """
    print('Starting to scrap Get on Board. Retrieving category list...')

    categories_raw = _send_request(CATEGORY_URL)['data']
    categories = [info['id'] for info in categories_raw]
    jobs = []

    print(f'\tFound {len(categories)} categories, scraping jobs for each...')

    for i, category in enumerate(categories[:2]): ## TODO
        endpoint = _parse_endpoint(JOBS_URL, '$CATEGORY_ID', category)
        jobs_raw = _send_request(endpoint, i)['data']

        print(f'\tFound {len(jobs_raw)} jobs in the {category} category, packing them...')

        for job in jobs_raw:
            job_attrs = job['attributes']
            company_id = job_attrs['company']['data']['id']
            web = job['links']['public_url']

            jobs.append(JobData(title = job_attrs['title'], functions = job_attrs['functions'],
                                benefits = job_attrs['benefits'], desirable = job_attrs['desirable'],
                                is_remote = job_attrs['remote'], remote_modality = job_attrs['remote_modality'],
                                country = job_attrs['country'], min_salary = job_attrs['min_salary'],
                                max_salary = job_attrs['max_salary'], company = _get_company_data(company_id)))

        print(f'\tFinished listing jobs for the {category} category.')

    print('Finished listing jobs')

    return jobs


def _get_company_data(company_id):
    """
    Retrieves the data of a company identified by the provided id
    """
    endpoint = _parse_endpoint(COMPANY_DETAIL_URL, '$COMPANY_ID', company_id)
    
    response_dict = _send_request(endpoint)['data']['attributes']
    return CompanyData(name = response_dict['name'], 
                       description = response_dict['description'],
                       long_description = response_dict['long_description'],
                       projects = response_dict['projects'], 
                       benefits = response_dict['benefits'],
                       web = response_dict['web'])


def _send_request(endpoint, i = 0, verbosity = False):
    """
    Sends a request and returns its json structure (dict) if correct or None if not
    """
    try:
        response = requests.get(endpoint)

        if verbosity:
            _print_response_success(response, i)

        return response.json()
    except Exception as e:
        print('An error occurred when attempting the request with index {i}. ', e)
        return None
