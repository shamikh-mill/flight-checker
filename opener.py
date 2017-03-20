import webbrowser
from datetime import datetime
from threading import Timer

# http://stackoverflow.com/questions/11523918/python-start-a-function-at-given-time
# http://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day


# time is in 24-hour format
current_time = datetime.today()
check_in_time = current_time.replace(day= current_time.day, hour = current_time.hour, minute = 18, second = 0, microsecond = 0)
change_in_time = check_in_time - current_time 

print ('current_time date and time: ', current_time)
print ('time remaining: ', change_in_time)

seconds = change_in_time.seconds + 1

def open(): 
	url = 'https://www.southwest.com/air/flight-status/index.html'
	try:
		webbrowser.open_new_tab(url)  # Open URL in a new tab, if a browser window is already open.
	except: 
		webbrowser.open_new(url)
	return "Check in page opened!"

time_watch = Timer(seconds, open)
time_watch.start()
print ("Flight Checker Initialized", check_in_time)