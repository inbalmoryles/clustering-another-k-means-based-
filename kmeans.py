import sys

def kmeans_clustering(k, max_iter, vectors, eps=0.001, verbose=True):
    """
biggest changes 
changed the input to work from terminal (stdout and stuff)
also added default valus ( k =3 and max_iter = 400)
the k needs to be changed to error handeling im not doing that (i dont know how to do it in python )
max_iter leave it as it is works good
added reading input from the file happends in main 
almost all the changes are 
a) lack of using the right varibles (using string as int)
b) input handeling abit wrong 
c) some problems that arose from point a) had some problems with cluster and ceontroid pointing to that same place causing problems in memory 
I.E centroids = clusters = [[] for t in range(k)]
then 
centroids[i] = vectors[i] again (strings, not numbers).
ran the code thought ai to add commends cuz im not documanting this 
also varbose=true is to print the center of the cluster on last run
and it also prints clusters and if varvbose = true the center of them 


minimum error handling addeed.

only did test 1 and 2 and worked so yeah

you got this :>
    """
    
    if not vectors:
        print("No data points found!")
        return None
    
    # Ensure consistent dimensions
    vector_dim = len(vectors[0])
    for vector in vectors:
        if len(vector) != vector_dim:
            print("An Error Occurred: Inconsistent dimensions!")
            return None
    
    # Adjust k if it exceeds the number of data points
    if k > len(vectors):
        k = len(vectors)
    
    # Initialize centroids using the first k points
    centroids = [vectors[i] for i in range(k)]
    
    # K-means algorithm
    curr_iter = 0
    flag = False
    while not flag and curr_iter < max_iter:
        curr_iter += 1
        clusters = [[] for _ in range(k)]
        clusters = assign_clusters(vectors, clusters, centroids)
        updated = update_centroids(clusters, centroids, eps)
        centroids = updated[0]
        flag = updated[1]
    
    # Print clusters and centroids if verbose
    if verbose:
        for i, cluster in enumerate(clusters):
            print(f"Cluster {i}:")
            for vector in cluster:
                formatted_vector = [f"{x:.4f}" for x in vector]
                print(formatted_vector)
        print("Centroids:")
        for i, centroid in enumerate(centroids):
            formatted_centroid = [f"{x:.4f}" for x in centroid]
            print(f"Centroid {i}: {formatted_centroid}")
    
    return clusters

def assign_clusters(data, clusters, centroids):
    """Assign each data point to the nearest centroid.

    Args:
        data (list): List of data points.
        clusters (list): List of empty clusters to populate.
        centroids (list): List of current centroids.

    Returns:
        list: Updated clusters with assigned points.
    """
    for vector in data:
        distances = [euclidean_distance(vector, centroid) for centroid in centroids]
        closest_centroid = distances.index(min(distances))
        clusters[closest_centroid].append(vector)
    return clusters

def euclidean_distance(point, centroid):
    """Calculate Euclidean distance between two points.

    Args:
        point (list): Data point coordinates.
        centroid (list): Centroid coordinates.

    Returns:
        float: Euclidean distance.
    """
    return sum((point[i] - centroid[i])**2 for i in range(len(point))) ** 0.5

def update_centroids(clusters, centroids, eps):
    """Update centroids and check for convergence.

    Args:
        clusters (list): Current clusters with assigned points.
        centroids (list): Current centroids.
        eps (float): Convergence threshold.

    Returns:
        tuple: (new_centroids, convergence_flag)
    """
    flag = True
    k = len(centroids)
    new_centroids = []
    for j in range(k):
        if clusters[j]:  # If cluster is not empty
            dim = len(clusters[j][0])
            new_centroid = [0] * dim
            for point in clusters[j]:
                for i in range(dim):
                    new_centroid[i] += point[i]
            for i in range(dim):
                new_centroid[i] /= len(clusters[j])
            if euclidean_distance(centroids[j], new_centroid) > eps:
                flag = False
            new_centroids.append(new_centroid)
        else:  # If cluster is empty, retain old centroid
            new_centroids.append(centroids[j])
    return new_centroids, flag

def main():
    """Handle command-line arguments and execute K-means clustering."""
    args = sys.argv[1:]  # Exclude script name

    # Set default values for k and max_iter
    k = 3
    max_iter = 400

    # Parse k from command-line arguments
    if len(args) >= 1:
        try:
            k = int(args[0])
        except ValueError:
            print("Incorrect number of clusters!")
            return 1
    # Parse max_iter from command-line arguments
    if len(args) >= 2:
        try:
            max_iter = int(args[1])
        except ValueError:
            print("Incorrect maximum iteration!")
            return 1
            

    # Read vectors from standard input
    vectors = []
    for line in sys.stdin:
        line = line.strip()
        if line:
            try:
                vector = list(map(float, line.split(',')))
                vectors.append(vector)
            except ValueError:
                print("An Error Has Occurred")
                return 1

    # Check if any vectors were read
    if not vectors:
        print("An Error Has Occurred")
        return 1

    # Check for consistent dimensions
    vector_dim = len(vectors[0])
    for vector in vectors:
        if len(vector) != vector_dim:
            print("An Error Has Occurred")
            return 1

    # Perform K-means clustering
    clusters = kmeans_clustering(k, max_iter, vectors)
    return 0

if __name__ == "__main__":
    main()