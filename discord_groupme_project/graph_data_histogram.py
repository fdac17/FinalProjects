from datetime import datetime
import time
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from data_processing import *

#function to graph the number of 
def graph_timeofday_histogram(data, name):
	hour_data = group_by_hour(data)
	print(len(hour_data[4]))
	#day = int(datetime.fromtimestamp(d['created_at']).strftime('%H'))
	hour_counts = [int(datetime.fromtimestamp(i['created_at']).strftime('%H')) for i in data]
	fig, ax = plt.subplots()
	n, bins, patches = ax.hist(hour_counts, 24)
	x_axis = [i for i in range(24)]
	#$plt.bar(offset, hour_counts, align='center', alpha=0.5)

	ax.set_xlabel('Time of Day (Hour)')
	ax.set_ylabel('Number of Posts')
	ax.set_title(r'Histogram of Posts By Hour - ' + name)

	# Tweak spacing to prevent clipping of ylabel
	fig.tight_layout()
	plt.savefig(name + ".png")
	#plt.show()
	return 0;

start = datetime(2017, 11, 1, 0, 0, 0)
end = datetime(2017, 11, 30, 23,59, 59)
for i in groups:
	data = get_data_range(start, end, i)
	graph_timeofday_histogram(data, group_names[i])
