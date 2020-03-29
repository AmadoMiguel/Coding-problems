class ListOptimSum(object):
	def __init__(self, list=[]):
		self.list = list
		self.runSum = [0] + list
		
		runSum = 0
		for i in range(len(self.list)):
			runSum += self.list[i]
			self.runSum[i + 1] = runSum
	
	def sum(self, start, stop):
		if 0 <= start <= stop and stop <= len(self.list):
			return self.runSum[stop] - self.runSum[start]
		raise IndexError("Index out of bounds")
	

nums = [1, 2, 3, 4, 5, 6, 7]
myList = ListOptimSum(nums)
print(myList.sum(0, 7))
