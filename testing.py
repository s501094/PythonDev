import csv

friend = ['josh','adam','fred']
friend.append('harry')
print(friend)
friend.remove('josh')
print(friend)

with open('SampleCSVFile_2kb.csv', 'rb') as f:
	reader = csv.reader(f)
	data = list(reader)
print(data)