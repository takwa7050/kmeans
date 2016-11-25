KMEANS ALGORITHM
----------------

> I added a bash script run_kmeans.sh to run the algorithm twice, once with a default number of cluster K = 3 and once with a K = 4
> To run the script, type: ./run_kmeans.sh

### How to run the algorithm:
* Open a terminal 
* Navigate to where the file is stored
* Type `python k-means.py` *(Default number of clusters K = 3)*
* Output:

    {'Iris-setosa': 28, 'Iris-versicolor': 3}
    {'Iris-virginica': 49, 'Iris-versicolor': 47}
    {'Iris-setosa': 20}


### To change the number of clusters
* Changing the number of clusters to K = 5
* Type `python k-means.py 5`
* Output:

    {'Iris-setosa': 17}
    {'Iris-setosa': 20}
    {'Iris-virginica': 36, 'Iris-versicolor': 3}
    {'Iris-virginica': 13, 'Iris-versicolor': 47}
    {'Iris-setosa': 11}

