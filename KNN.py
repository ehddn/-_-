import pandas as pd
from math import sqrt
dataset = [
	[2.7810836,2.550537003,0],
	[1.465489372,2.362125076,0],
	[3.396561688,4.400293529,0],
	[1.38807019,1.850220317,0],
	[3.06407232,3.005305973,0],
	[7.627531214,2.759262235,1],
	[5.332441248,2.088626775,1],
	[6.922596716,1.77106367,1],
	[8.675418651,-0.242068655,1],
	[7.673756466,3.508563011,1]
]
# row = [x, y, type]


def euclidean_distance(row1, row2):
	distance = 0.0
	for i in range(0,len(row1)-1):  # (0-1까지)
		distance += (row1[i] - row2[i])**2
	return sqrt(distance)

row0 = [3,3]

# for row in dataset:
# 	print(row)
# 	distance = euclidean_distance(row0, row)
# 	print(distance)

# Locate the most similar neighbors
def get_neighbors(train, test_row, k_value):
	distances = list()  #거리를 저장해둘 리스트
	for train_row in train:
		dist = euclidean_distance(test_row, train_row)
		distances.append((train_row, dist))   #distances에는 train값과 해당하는 거리값
	distances.sort(key=lambda x: x[1])   # dist값을 기준으로 정렬
	
	neighbors = list()
	for i in range(k_value):  # k값만큼 가까운 값 반환
		neighbors.append(distances[i][0])
	return neighbors

# neighbors = get_neighbors(dataset, row0, 6)
# for neighbor in neighbors:
# 	print(neighbor)
#해당 값은 0이 더 가까움 type:0


def predict_classification(train, test_row, k_value):
	neighbors = get_neighbors(train, test_row, k_value)
	for neighbor in neighbors:
		print(neighbor)
	type_0_count=0
	type_1_count=0
	for i in range(0,len(neighbors)):
		type_0_count=type_0_count+neighbors[i].count('사과')
		type_1_count=type_1_count+neighbors[i].count('바나나')
	print("사과의 수: ",type_0_count)
	print("바나나 수: ",type_1_count)

	if(type_0_count>type_1_count):
		return 0
	elif (type_0_count<type_1_count):
		return 1
	else:
		return 10


# row0 = [5,5,0]
#
# prediction = predict_classification(dataset, row0, 3)
# print('Expected %d, Got %d.' % (row0[-1], prediction))

#---------------------실습


data=pd.read_csv("과일.csv")

data_table=[0]*len(data["No"])
for i in range(0,len(data)):
	data_table[i]=([data["무게(kg)"][i],data["색r"][i],data["색g"][i],data["색b"][i],data["가격"][i],data["과일"][i]])



test_fruit=[1.1,0.85,0.45,0.5,2100,'사과']


prediction = predict_classification(data_table, test_fruit, 5)
print('Expected %s, Got %d.' % (test_fruit[5], prediction))