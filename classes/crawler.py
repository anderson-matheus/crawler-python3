import re
import urllib3
from urllib3.exceptions import HTTPError
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)



class Crawler:

	def find_word_url(url, word):
		http = urllib3.PoolManager()
		try:
			r = http.request('GET', url)
			string_html = r.data.decode('utf-8') # transform r.data in string
			results = re.findall('(para)', string_html, re.IGNORECASE)
			return {'url': url, 'searched_word': word, 'occurrence': len(results), 'success': True}
		except HTTPError as e:
			return {'url': url, 'searched_word': word, 'occurrence': 0, 'success': False}