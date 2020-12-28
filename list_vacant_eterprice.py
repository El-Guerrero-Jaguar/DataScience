import bs4
import requests
from common import config
import json

class ListVacant:
    
    def vacant_link(url):
        response = requests.get(url)

        content = response.content
        soup = bs4.BeautifulSoup(content, 'lxml')

        items = []
        for item in soup.select('.job-eti li'):
            if (item.find('a') != None):
                if (item.find('a').get('href') != None):
                    #print(item.find('a').get('href'))
                    item_job = item.find('a').get('href')
                    #print(item_job)
                    #items.append([item.find('a').get('href')])
                    return ListVacant.vacant_job(item_job)
                    

    def vacant_job(item_job):
        list_jobs = []
        response_job = requests.get(item_job)

        content_job = response_job.content
        soup_job = bs4.BeautifulSoup(content_job, 'lxml')
        
        for link in soup_job.select('.col.l9'):
            #import ipdb; ipdb.set_trace()
            #print(link.select('h3')[0].get_text(), link.select('h1')[0].get_text(), link.select('.field-set-vacancy li p')[1], link.find(id="vacancy-description")('p'))
            list_jobs.append([{"company": link.select('h3')[0].get_text(), "position": link.select('h1')[0].get_text(), "salary": link.select('.field-set-vacancy li p')[1].get_text().lstrip(), "place": link.select('.field-set-vacancy li p')[3].get_text().lstrip(), "type": link.select('.field-set-vacancy li p')[5].get_text().lstrip(), "english": link.select('.field-set-vacancy li p')[7].get_text().lstrip(), "description": str(link.find(id="vacancy-description"))}])
        


        print(list_jobs)
        return list_jobs