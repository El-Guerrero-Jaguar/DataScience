"""
This module defines the JobData class
"""

class JobData:
    """
    This data class represents a job vacancy
    """
    def __init__(self, title = None, functions = None, benefits = None,
                 desireable = None, is_remote = None, remote_modality = None,
                 country = None, min_salary = None, max_salary = None,
                 company = None):
        self._title = title
        self._functions = functions
        self._benefits = benefits
        self._desireable = desireable
        self._is_remote = is_remote
        self._remote_modality = remote_modality
        self._country = country
        self._min_salary = min_salary
        self._max_salary = max_salary
        self._company = company


class CompanyData:
    """
    This class contains information of a company
    """
    def __init__(self, name = None, description = None, long_description = None,
                 projects = None, benefits = None, web = None):
        self._name = name
        self._descritpion = description
        self._long_description = long_description
        self._projects = projects
        self._benefits = benefits
        self._web = web
