## knn.py

To run from the commandline:

    python3 knn.py <k> <trainingfile> <testfile> [-threadcount] [--label-included]

To run as a function: (this returns a dict of points from the test data and a list of their k-nearest points)

    from knn import knn

    knn(int k, [trainingdata], [testdata], int threadcount, bool ifLabel)

`--if-label` and `bool ifLabel` is used if you have labeled data.
Data must be in the format of either rows of features, or label: features. 

Traditionally you calculate k-nearest neighbors by calculating the euclidean distance between the sample datapoint p and the datapoints in the training data and taking the k smallest distances for each point of sample data. This would take O(dn) time for d points of data in the sample data, and n points of data in the test dataset. For large amounts of data, this is slow and costly.

There are a few ways of making this classifier more efficient. One is condensing the training dataset as not all points of training data is relevant. The other is similar in that we check whether we should calculate the euclidean distance to p first. The formermost requires costly heuristics to clean up the training data but has to only be done once. The latter has a little extra overhead of checks and minor computation, but in the long run will save time from doing more costly computations.
We merely check whether either the distance between the training and tests x or y coordinate is greater than the distance of the kth closest neighbor as there would be no way it could be closer.
Let's pretend that the check is half as costly as calculating the distance. 
Each item that passes would cost 1.5 while each failed item would cost .5 
For a small dataset, this would be inefficient, but for large datasets, as closer and closer points's are found less and less items would pass the check. Worst case scenario where the items somehow appear in order of farthest from p to closest to p. Here, so long as more than half the items fail the check, this will be more cost efficient than calculating the distance for every item. The number of items required to fail is smaller the faster the check is-- in fact it is inversely proportional in that if the check is 4 times faster than the computation then only 1/4 have to fail. 

We can do this by using a max heap that only has k slots representing the current nearest neighbors using the distance as the key and some pointer to the data point, if we use labels then we can easily just store the label. (If this was written in C/C++ it would be very easy to point to values)

We start off with k values in the heap and as we find items smaller than the max item we pop out the largest of the k values and push in the new value

We can further optimize this by sorting the training data first on one of the features. The best is a diverse feature, but as long as all the values has some variance it doesnt matter-- the easiest to handle, of course is the first feature. When we sort it, after every update of the kth nearest neighbor, we can easily eliminate at least all items where differences between the first feature is greater than the kth nearest distance because they will be clustered together. We can combine this with binary search to first get "in range" the rest is then running towards one bound which closes in as we discover smaller distances, and then going back and running towards the other.

Note because we have to push the first 7 distances in to compare and the list is sorted by feature, the feature will always be the smallest 7 of those features that could be problematic

Let's say calculating the difference between 2 vectors takes *f* time where *f* is equal to the number of features
Euclidean distance takes 2*f* (diff and square) + 1 (sqrt) \~ 2*f*
Normally before reducing the training data we would have to do 2*f*nm \~O(*f*nm) time
The sorting takes nlogn time. 
Binary search takes at most nlog(n) time. We only need to do this once

----------------

To make this faster, we use parallel computing split up all the items we need to classify into separate processes, as well as splitting up the training data and then getting the knn out of all the knns. Basically a little bit of SDMI and a little MDSI.
This however still has to touch ALL the training data, but in parallel. The choice of how many threads for the training data and how many for the test data has to be chosen carefully