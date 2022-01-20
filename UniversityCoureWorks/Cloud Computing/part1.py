from mrjob.job import MRJob


class MRFindMin(MRJob):

  def mapper(self, _, line):
    for number in line.split(','):
      yield None, int(number)

  # Discard key, because it is None
  # After sort and group, the output is only one key-value pair (None, <all_numbers>)
  def reducer(self, _, numbers):
    yield "minimun value is", min(numbers)


if __name__ == '__main__':
  MRFindMin.run()
