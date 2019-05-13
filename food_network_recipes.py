### Scraping Food Network for recipes

website = 'https://www.foodnetwork.com/search/lemon-blueberry-'

# GET Request
def get_request(url):
	try: 
		with closing(get(url, stream = True)) as resp:
			if good_response(resp):
				return resp.content
			else:
				return None
	# except RequestException as e:
	# 	log_error('Error during requests to {0} : {1}'.format(url, str(e)))
	# 	return None


# Returns true is response is HTML
def good_response(resp): 
content_type = resp.headers['Content-Type'].lower()
	return (resp.status_code == 200
			and content-type is not None
			and content-type.find('html')>-1)

# Prints log error
def log_error(e):
	print e

#runs script
get_request(website)