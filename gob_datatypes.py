"""
This module defines datatypes used by the Get on Board scraper
"""

import json
from datetime import datetime


class JobData:
    """
    This data class represents a job vacancy
    """
    def __init__(self, title = None, functions = None, benefits = None,
                 desirable = None, is_remote = None, remote_modality = None,
                 country = None, min_salary = None, max_salary = None, web = None,
                 date = None, company_name = None, company_website = None):
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
        self._date = str(datetime.fromtimestamp(date).date())
        self._company_name = company_name
        self._company_website = company_website

        if self._min_salary == None:
            self._min_salary = 'N/A'

        if self._max_salary == None:
            self._max_salary = 'N/A'


    def __str__(self):
        return str(self.__dict__)


    def __repr__(self):
        return str(self)

    
    def to_json(self):
        """
        Returns a json representation of the JobData instance
        """
        return {
            'titulo': self._title,
            'empresa': self._company_name,
            'pais': self._country,
            'descripcion': f'{self._functions}\n{self._benefits}\n{self._desirable}',
            'modalidad': self._remote_modality,
            'fecha': self._date,
            'salario': f'{self._min_salary}, {self._min_salary}',
            'url_vacante': self._web,
            'url_empresa': self._company_website
        }