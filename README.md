# Clustering-Data
1. Read the data from the file. Use only the floating point values for the clustering. Don’t discard the class information. While you
can’t use it for clustering, you will need it later for assigning names to the clusters and for checking the accuracy of the clusters.
2. Apply the k-means algorithm to find clusters. There are 3 natural clusters in the case of the iris data. (See below for more
information on k-means).
3. Use Euclidean distance as your distance measure.
4. Assign each final cluster a name by choosing the most frequently occurring class label of the examples in the cluster.
5. Find the number of data points that were put in clusters in which they didn’t belong. (based on having a different class label
than the cluster name).
k-means algorithm:
Given k initial points that will act as the centroids of the clusters for the first iteration, you will run the standard k-means clustering algorithm
that we discussed in class.
• For each point, place it in the cluster whose current centroid it is nearest to.
• After all points are assigned, update the locations of centroids of the k clusters.
• Repeat for the specified number of iterations.
