import requests

# TODO: Add filters to all read-only API calls
# TODO: Add relational filters to list methods
# TODO: Add field filters to list methods

class ServiceSidekick(object):
	
	def __init__(self, api_token, app_name):
		self.token = api_token
		self.app = app_name
	
	""" calls for customers """
	def list_customers(self, filter=None):
		url = 'https://%s.servicesidekick.com/customers.xml' % (self.app)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content
		
	def show_customer(self, customer_id):
		url = 'https://%s.servicesidekick.com/customers/%s.xml' % (customer_id)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content
		
	def create_customer(self, new_customer):
		headers = {'content-type': 'application/xml'}
		# new_customer should be a dict with the customer info
		return "Not implemented"
		
	def update_customer(self, customer_id, customer):
		headers = {'content-type': 'application/xml'}
		# new_customer should be a dict with the customer info
		pass
		
	def delete_customer(self, customer_id):
		url = 'https://%s.servicesidekick.com/customers/%s.xml' % (self.app, customer_id)
		r = requests.delete(url, auth=(self.token, self.token))
		return r.status_code
		
	""" calls for jobs """
	def list_jobs(self):
		url = 'https://%s.servicesidekick.com/jobs.xml' % (self.app)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content
		
	def show_job(self, job_id):
		url = 'https://%s.servicesidekick.com/jobs/%s.xml' % (self.app, job_id)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content
		
	def create_job(self, new_job):
		headers = {'content-type': 'application/xml'}
		# new_job should be a dict with the job info
		return "Not implemented"
		
	def update_job(self, job_id, job):
		headers = {'content-type': 'application/xml'}
		# new_job should be a dict with the job info
		return "Not implemented"
		
	def delete_job(self, job_id):
		url = 'https://%s.servicesidekick.com/jobs/%s.xml' % (self.app, job_id)
		r = requests.delete(url, auth=(self.token, self.token))
		return r.status_code
		
	""" calls for job charges """
	def create_job_charge(self, job_id):
		headers = {'content-type': 'application/xml'}
		return "Not implemented"
		
	""" calls for employees """
	def list_employees(self):
		url = 'https://%s.servicesidekick.com/employees.xml' % (self.app)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content
		
	def show_employee(self, employee_id):
		url = 'https://%s.servicesidekick.com/employees/%s.xml' % (self.app, employee_id)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content
		
	def create_employee(self, new_employee):
		headers = {'content-type': 'application/xml'}
		# new_employee should be a dict with the employee info
		return "Not implemented"
		
	def update_employee(self, employee_id, employee):
		headers = {'content-type': 'application/xml'}
		# new_employee should be a dict with the employee info
		return "Not implemented"
		
	# deletion of employees is not supported, set inactive via update
	
	""" calls for time entries """
	def list_time_entries(self, job_id):
		url = 'https://%s.servicesidekick.com/jobs/%s/time_entries.xml' % (self.app, job_id)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content
		
	def show_time_entry(self, job_id, time_entry_id):
		url = 'https://%s.servicesidekick.com/jobs/%s/time_entries/%s.xml' % (self.app, job_id, time_entry_id)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content
		
	def create_time_entry(self, job_id):
		headers = {'content-type': 'application/xml'}
		return "Not implemented"
		
	def update_time_entry(self, job_id, time_entry_id):
		headers = {'content-type': 'application/xml'}
		return "Not implemented"
		
	def delete_time_entry(self, job_id, time_entry_id):
		url = 'https://%s.servicesidekick.com/jobs/%s/time_entries/%s.xml' % (self.app, job_id, time_entry_id)
		r = requests.delete(url, auth=(self.token, self.token))
		return r.status_code
		
	""" calls for tasks """
	def list_tasks(self):
		url = 'https://%s.servicesidekick.com/tasks.xml' % (self.app)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content
		
	def show_task(self, task_id):
		url = 'https://%s.servicesidekick.com/tasks/%s.xml' % (self.app, task_id)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content
		
	def create_task(self):
		headers = {'content-type': 'application/xml'}
		return "Not implemented"
		
	def update_task(self, task_id):
		headers = {'content-type': 'application/xml'}
		return "Not implemented"
		
	def delete_task(self, task_id):
		url = 'https://%s.servicesidekick.com/tasks/%s.xml' % (self.app, task_id)
		r = requests.delete(url, auth=(self.token, self.token))
		return r.content
		
	""" calls for customer notes """
	def list_customer_notes(self, customer_id):
		url = 'https://%s.servicesidekick.com/customers/%s.xml' % (self.app, customer_id)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content
		
	def show_customer_note(self, customer_id, note_id):
		url = 'https://%s.servicesidekick.com/customers/%s/notes/%s.xml' % (self.app, customer_id, note_id)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content
		
	def update_customer_note(self, customer_id, note_id):
		headers = {'content-type': 'application/xml'}
		return "Not implemented"
		
	def delete_customer_note(self, customer_id, note_id):
		url = 'https://%s.servicesidekick.com/customers/%s/notes/%s.xml' % (self.app, customer_id, note_id)
		r = requests.delete(url, auth=(self.token, self.token))
		return r.content
		
	""" calls for job notes """
	def list_job_notes(self, job_id):
		url = 'https://%s.servicesidekick.com/jobs/%s/notes.xml' % (self.app, job_id)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content
		
	def show_job_note(self, job_id, note_id):
		url = 'https://%s.servicesidekick.com/jobs/%s/notes/%s.xml' % (self.app, job_id, note_id)
		r = requests.get(url, auth=(self.token, self.token))
		return r.content
		
	def create_job_note(self, job_id):
		headers = {'content-type': 'application/xml'}
		return "Not implemented"
		
	def update_job_note(self, job_id, note_id):
		headers = {'content-type': 'application/xml'}
		return "Not implemented"
		
	def delete_job_note(self, job_id, note_id):
		url = 'https://%s.servicesidekick.com/jobs/%s/notes/%s.xml' % (self.app, job_id, note_id)
		r = requests.delete(url, auth=(self.token, self.token))
		return r.content
