#!?
# https://habr.com/ru/post/585034/
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np

n = 2
dim = 3
k = 4

def data_distribution(array, cluster):
	cluster_content = [[] for i in range(k)]

	for i in range(n):
		min_distance = float('inf')
		situable_cluster = -1
		for j in range(k):
			distance = 0
			for q in range(dim):
				distance += (array[i][q] - cluster[j][q]) ** 2

			distance = distance ** (1 / 2)
			if distance < min_distance:
				min_distance = distance
				situable_cluster = j

		cluster_content[situable_cluster].append(array[i])

	return cluster_content

def cluster_update(cluster, cluster_content, dim):
	k = len(cluster)
	for i in range(k):  #по i кластерам
		for q in range(dim):  #по q параметрам
			updated_parameter = 0
			for j in range(len(cluster_content[i])):
				updated_parameter += cluster_content[i][j][q]
			if len(cluster_content[i]) != 0:
				updated_parameter = updated_parameter / len(cluster_content[i])
			cluster[i][q] = updated_parameter
	return cluster

def clusterization (array, k,):
	n = len(array)
	dim = len(array[0])

	cluster = [[0 for i in range(dim)] for q in range(k)]
	cluster_content = [[] for i in range(k)]

	for i in range(dim):
		for q in range(k):
			cluster[q][i] = random.randint(0, max_cluster_value)

	cluster_content = data_distribution(array, cluster)

	privious_cluster = copy.deepcopy(cluster)
	while 1:
		cluster = cluster_update(cluster, cluster_content, dim)
		cluster_content = data_distribution(array, cluster)
		if cluster == privious_cluster:
			break
		privious_cluster = copy.deepcopy(cluster)