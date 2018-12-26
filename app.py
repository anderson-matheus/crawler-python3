import hug
import json
from classes.validate import Validate
from classes.crawler import Crawler

api = hug.get(on_invalid=hug.redirect.not_found)

@api
def crawler(urls: hug.types.multiple, word: hug.types.text):
    validate = Validate()
    crawler = Crawler()
    valid_urls = validate.is_valid_urls(urls)
    if valid_urls == False:
    	return {'error': 'Send valid urls'}
    

    data = {'data': []}
    for url in urls:
        data['data'].append(crawler.find_word_url(url, word))
    return data
