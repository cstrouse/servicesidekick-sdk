import requests

class ServiceSidekick(object):
	
	def __init__(self, api_token, app_name):
		self.token = api_token
		self.app = app_name
		
	# TODO: Add filters
	def list_customers(self):
		url = 'https://%s.servicesidekick.com/customers.xml' % (self.app)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content