"""
This module defines the JobData class
"""

import json


class JobData:
    """
    This data class represents a job vacancy
    """
    def __init__(self, title = None, functions = None, benefits = None,
                 desirable = None, is_remote = None, remote_modality = None,
                 country = None, min_salary = None, max_salary = None, web = None,
                 company = None):
        self._title = title
        self._functions = functions
        self._benefits = benefits
        self._desirable = desirable
        self._is_remote = is_remote
        self._remote_modality = remote_modality
        self._country = country
        self._min_salary = min_salary
        self._max_salary = max_salary
        self._web = web
        self._company = company


    def __str__(self):
        return str(self.__dict__)


    def __repr__(self):
        return str(self)


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
