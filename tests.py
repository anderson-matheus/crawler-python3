from classes.validate import Validate
from classes.crawler import Crawler
import hug
import app

def test_valid_urls():
	urls = [
		'http://www.google.com',
		'https://www.google.com'
		'http://localhost'
		'uol.com.br',
	]
	assert Validate.is_valid_urls(urls) == True

def test_invalid_urls():
	urls = [
		'test',
		'invalid test'
		'http://testurl'
	]
	assert Validate.is_valid_urls(urls) == False

def test_crawler_valid_url():
	result = Crawler.find_word_url('uol.com.br', 'assine')
	assert result['success'] == True

def test_crawler_invalid_url():
	result = Crawler.find_word_url('invalidurl', 'assine')
	assert result['success'] == False


def test_api_crawler():
	urls = [
		'http://www.ig.com',
		'uol.com.br',
	]
	word = 'assine'
	result = hug.test.get(app, '/crawler', params={'urls': urls, 'word': word})