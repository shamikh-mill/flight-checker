import webbrowser
from datetime import datetime
from threading import Timer

# http://stackoverflow.com/questions/11523918/python-start-a-function-at-given-time
# http://stackoverflow.com/questions/15088037/python-script-to-do-something-at-the-same-time-every-day

current = datetime.today()

#next_day_sametime = current.replace(day= current.day +  1, hour = 1, minute = 0, second = 0, microsecond = 0)
next_day_sametime = current.replace(day= current.day, hour = current.hour, minute = 48, second = 0, microsecond = 0)
change_in_time = next_day_sametime - current 
print (current, change_in_time)


secs = change_in_time.seconds + 1

def open(): 
	url = 'https://www.southwest.com/air/flight-status/index.html'
	webbrowser.open_new_tab(url + 'doc/')  # Open URL in a new tab, if a browser window is already open.
	return 

# Open URL in new window, raising the window if possible.
#webbrowser.open_new(url)

#open(url)

time_watch = Timer(secs, open)
time_watch.start()
print ("Flight Checker Initialized")