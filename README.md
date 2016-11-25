# KMEANS ALGORITHM

### How to run the algorithm:
* Open a terminal 
* Navigate to where the file is stored
* Type `python k-means.py` (Default number of clusters K = 3, and default max number of iterations = 1000)
* Output:
{'Iris-setosa': 28, 'Iris-versicolor': 3}
{'Iris-virginica': 49, 'Iris-versicolor': 47}
{'Iris-setosa': 20}

We can see that some features are not linearly seperated

### To change the number of clusters
* Changing the number of clusters to K = 5
* Type `python k-means.py 5`
* Output:
{'Iris-setosa': 17}
{'Iris-setosa': 20}
{'Iris-virginica': 36, 'Iris-versicolor': 3}
{'Iris-virginica': 13, 'Iris-versicolor': 47}
{'Iris-setosa': 11}

### Running with a defined number of max iterations
* Type `python k-means.py 3 1000`
