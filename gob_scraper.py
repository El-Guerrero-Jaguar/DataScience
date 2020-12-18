"""
This module scraps the Get on Board website using its REST API
"""

import requests
from job_data import JobData, CompanyData


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


def scrap_category_list(categories):
    """
    Retrieves and returns a list of jobs for every category in the input list
    """
    jobs = []

    for i, category in enumerate(categories):
        endpoint = _parse_endpoint(CATEGORY_URL, '$CATEGORY_ID', category)
        response_dict = send_request(endpoint, i)


    return jobs


def get_company_data(company_id):
    """
    Retrieves the data of a company identified by the provided id
    """
    endpoint = _parse_endpoint(COMPANY_DETAIL_URL, '$COMPANY_ID', company_id)
    
    response_dict = send_request(endpoint)['data']['attributes']
    return CompanyData(name = response_dict['name'], 
                       description = response_dict['description'],
                       long_description = response_dict['long_description'],
                       projects = response_dict['projects'], 
                       benefits = response_dict['benefits'],
                       web = response_dict['web'])


def send_request(endpoint, i = 0):
    """
    Sends a request and returns its json structure (dict) if correct or None if not
    """
    try:
        response = requests.get(endpoint)
        _print_response_success(response, i)
        return response.json()
    except Exception as e:
        print('An error occurred when attempting the request with index {i}. ', e)
        return None
