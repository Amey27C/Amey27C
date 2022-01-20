from mrjob.job import MRJob
from statistics import stdev
import statistics
import mrjob
import csv 

class MRFindStDev(MRJob):
	def mapper(self, __, line):
		for number in line.split(','):
			yield None, int(number)

	def reducer(self, __, num):
		yield "DEVIATION=",statistics.stdev(num)
		
if __name__ == '__main__':
	MRFindStDev.run()