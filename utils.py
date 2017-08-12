# -*- coding: utf-8 -*-

import time
import random

class Debug(object):
	__LogToFile = True

	@staticmethod
	def __get_time_stamp():
		timeArray = time.localtime(time.time())
		return str(time.strftime("%Y-%m-%d %H:%M:%S", timeArray))

	@staticmethod
	def log_with_prefix(prefix, message):
		final_msg = '[%s] [%s] %s' % (Debug.__get_time_stamp(), prefix,  str(message))

		if Debug.__LogToFile:
			pass

		print(final_msg)

	@staticmethod
	def log(message):
		Debug.log_with_prefix('log', message)

	@staticmethod
	def log_info(message):
		Debug.log_with_prefix('info', message)

	@staticmethod
	def log_error(message):
		Debug.log_with_prefix('error', message)

	@staticmethod
	def write_file(message):
		fp = open('temp.txt', 'w')
		fp.write(message)
		fp.close()

class Math(object):
	@staticmethod
	def clamp(val, lower_limit, upper_limit):
		if val < lower_limit:
			return lower_limit
		elif val > upper_limit:
			return upper_limit
		else:
			return val

	@staticmethod
	def get_random_numbers_in_range(start_val, end_val, count):
		result = []

		while True:
			if len(result) >= count:
				break
			else:
				val = random.randint(start_val, end_val)
				if val not in result:
					result.append(val)

		return result
