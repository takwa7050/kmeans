from __future__ import division
import sys
from collections import defaultdict
import random
from pprint import pprint

import input_output as io
import numpy as np
import math

class KMeans(object):

	def __init__(self, numberOfClusters = 3):
		self.numberOfClusters = numberOfClusters
		self.max_iterations = 1000
		self.data = self.__readData()
		self.features = self.data.keys()

	def run(self):
		k = self.numberOfClusters
		centroids = dict((c,[c]) for c in self.features[:k])
		centroids[self.features[k-1]] += self.features[k:]
		for i in xrange(self.max_iterations):
		    new_centroids = self.__assignCentroids(centroids)
		    new_centroids = self.__updateCentroids(new_centroids)
		    if centroids == new_centroids:
		        break
		    else:
		        centroids = new_centroids
		self.__printResult(centroids)

	def __assignCentroids(self, centroids):
		new_centroids = defaultdict(list)
		for cx in centroids:
		    for x in centroids[cx]:
		        best = min(centroids, key=lambda c: self.__calculateDistance(x,c))
		        new_centroids[best] += [x]
		return new_centroids

	def __updateCentroids(self, centroids):
		new_centroids = {}
		for c in centroids:
		    new_centroids[self.__mean(centroids[c])] = centroids[c]
		return new_centroids

	def __calculateDistance(self, feature1, feature2):
		a = np.array
		d = a(feature1)-a(feature2)
		return np.sqrt(np.dot(d, d))

	def __mean(self, features):
	    return tuple(np.mean(features, axis=0))

	def __counter(self, alist):
	    count = defaultdict(int)
	    for x in alist:
	        count[x] += 1
	    return dict(count)

	def __printResult(self, clusters):
		for c in clusters:
		    print self.__counter([self.data[x] for x in clusters[c]])

	def __readData(self):
		data = [l.strip() for l in open('iris.data') if l.strip()]
		features = [tuple(map(float, x.split(',')[:-1])) for x in data]
		labels = [x.split(',')[-1] for x in data]
		return dict(zip(features, labels))


if __name__ == "__main__":
    KMeans().run()