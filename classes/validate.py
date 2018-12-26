import re


class Validate:

    def is_valid_urls(self, urls):
        for url in urls:
            validate = re.compile(
            	r'(http:\/\/www\.|https:\/\/www\.|http:\/\/|https:\/\/)?'  # http:// or https://
		        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+[A-Z]{2,6}\.?|'  # domain...
		        r'localhost|'  # localhost...
		        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # ...or ip
		        r'(?::\d+)?'  # optional port
		        r'(?:/?|[/?]\S+)$', re.IGNORECASE
            )

            if validate.search(url) == None:
                return False

        return True



