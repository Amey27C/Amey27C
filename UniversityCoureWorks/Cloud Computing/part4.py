from mrjob.job import MRJob
import csv

class mapping(MRJob):
  def mapper(self, __, line):
    for word in line.split(','):
      word= word.strip(' ')
      yield(word, line)
    
    
  def reducer(self, key, value):
    invert = []
    for v in value:
      invert.append(v)
    
    yield(key, invert)

if __name__ == '__main__':
  mapping.run()