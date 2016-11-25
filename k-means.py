from __future__ import division
import sys
from collections import defaultdict
import random
from pprint import pprint

import input_output as io
import numpy as np
import math

class KMeans(object):

	def __init__(self, numberOfClusters = 3, maxIterations = 1000):
		self.numberOfClusters = numberOfClusters
		self.data = self.__readData()
		self.features = self.data.keys()
		self.maxIterations = maxIterations

	def run(self):
		k = self.numberOfClusters
		centroids = dict((c,[c]) for c in self.features[:k])
		centroids[self.features[k-1]] += self.features[k:]
		for i in xrange(self.maxIterations):
		    newCentroids = self.__assignCentroids(centroids)
		    newCentroids = self.__updateCentroids(newCentroids)
		    if centroids == newCentroids:
		        break
		    else:
		        centroids = newCentroids
		
		self.__printResult(centroids)

	def __assignCentroids(self, centroids):
		newCentroids = defaultdict(list)
		for cx in centroids:
		    for x in centroids[cx]:
		        best = min(centroids, key=lambda c: self.__calculateDistance(x,c))
		        newCentroids[best] += [x]
		return newCentroids

	def __updateCentroids(self, centroids):
		newCentroids = {}
		for c in centroids:
		    newCentroids[self.__mean(centroids[c])] = centroids[c]
		return newCentroids

	def __calculateDistance(self, feature1, feature2):
		features = np.array
		distance = features(feature1)-features(feature2)
		return np.sqrt(np.dot(distance, distance))

	def __mean(self, features):
	    return tuple(np.mean(features, axis=0))

	def __counter(self, alist):
	    count = defaultdict(int)
	    for x in alist:
	        count[x] += 1
	    return dict(count)

	def __readData(self):
		data = [l.strip() for l in open('iris.data') if l.strip()]
		features = [tuple(map(float, x.split(',')[:-1])) for x in data]
		labels = [x.split(',')[-1] for x in data]
		return dict(zip(features, labels))

	def __printResult(self, clusters):
		for c in clusters:
		    print self.__counter([self.data[x] for x in clusters[c]])

if __name__ == "__main__":
    KMeans().run()