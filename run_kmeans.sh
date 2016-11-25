#!/bin/bash

echo '----------------------------------'
echo '... Running K-Means Algorithm  ...'
echo '----------------------------------'

echo
echo "default config: 3 clusters"
echo '>> python k-means.py'
python k-means.py


echo
echo "User config: 4 clusters, 1000 max iterations"
echo '>> python k-means.py 4'
python k-means.py 4
echo "!!! There a linearly separable class 'setosa' and 2 non linearly separable one each other !!!"