import input_output as io
import numpy as np
import math

class KMeans(object):

	def __init__(self, numberOfClusters = 3):
		self.numberOfClusters = numberOfClusters
		self.max_iterations = 1000
		self.data = io.read_file('iris.data')
		self.centroids = self.__randomizeCentroids()
		self.oldCentroids = [[] for i in range(self.numberOfClusters)]

	def run(self):
		iterations = 0
		print(self.__has_converged(iterations))
		while not (self.__has_converged(iterations)):
			iterations = iterations + 1

			clusters = [[] for i in range(self.numberOfClusters)]

		# assign data points to clusters
		clusters = self.__calculateEuclideanDistance(clusters)

		# recalculate centroids
		index = 0
		for cluster in clusters:
			oldCentroids[index] = centroids[index]
			centroids[index] = np.mean(cluster, axis=0).tolist()
			index += 1


			print("The total number of data instances is: " + str(len(data)))
			print("The total number of iterations necessary is: " + str(iterations))
			print("The means of each cluster are: " + str(centroids))
			print("The clusters are as follows:")
			for cluster in clusters:
				print("Cluster with a size of " + str(len(cluster)) + " starts here:")
				print(np.array(cluster).tolist())
				print("Cluster ends here.")

				return

	def __calculateEuclideanDistance(self, instance1, instance2, length):
		distance = 0
		for x in range(length):
			distance += pow((instance1[x] - instance2[x]), 2)
		return math.sqrt(distance)

	def __randomizeCentroids(self):
		centroids = []
		for cluster in range(0, self.numberOfClusters):
			centroids.append(self.data[np.random.randint(0, len(self.data))])
		return centroids;

	def __has_converged(self, iterations):
		if iterations > self.max_iterations:
			return True
		return self.oldCentroids == self.centroids



kmeans = KMeans()
print("Printing centroids:")
print(kmeans.centroids)
print("Printing old centroids:")
print(kmeans.oldCentroids)
print("Running algorithm:")
kmeans.run()