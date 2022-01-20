from mrjob.job import MRJob
import csv
from mrjob.step import MRStep
import mrjob

def read_csv(line):
  for row in csv.reader([line]):
    return row

desc= {}

class mapping(MRJob):
  
  OUTPUT_PROTOCOL= mrjob.protocol.JSONValueProtocol
  
  def steps(self):
        return [
            MRStep(mapper=self.mapper_gets,
                   reducer=self.reducer_list),
            MRStep(reducer=self.reducer_ans)
        ]
    

  def mapper_gets(self, __, line):
    cell= read_csv(line)
    yield cell[0], (1, cell[1])
    yield cell[1], (0, cell[0])
    
     
  def reducer_list(self, key, value):
    item= []
    for v in value:
      if v[0] == 1:
        item.append(v[1])
    desc[key]= item
    yield key, item
    
  
  def reducer_ans(self, key, key_list_item):
    u= key
    for items in key_list_item:
      for v in items:
        item= desc[v]
        if len(item)!= 0:
          for w in item:
            yield None, (u, v, w)

if __name__ == '__main__':
  mapping.run()