from datetime import datetime

def convert_to_epoch(timestamp):
	diff = (timestamp - datetime(1970, 1, 1))
	# added to support python version < 2.7, otherwise timedelta has total_seconds()
	differenceTotalSeconds = (diff.microseconds + (diff.seconds + diff.days*24*3600) * 1e6) / 1e6
	seconds = int(differenceTotalSeconds)
	return seconds
