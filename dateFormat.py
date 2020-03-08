'''Create a function that converts a date formatted as MM/DD/YYYY to YYYYDDMM'''

def format_date(date):
	return date[-4:] + date[3:5] + date[:2]