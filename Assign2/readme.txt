Ideas to parallelize image compression: 
	a) Vector quantization is clustring a vectors of pixels using kmean algorithm.
		____________
		|	    |
		|128vectors |
		|	    |
		-------------
		|	    |
		|128vectors |
		|	    |
		-------------
		|           |
		 (Codebook)
	
	b) Dividing image in blocks of 4*4 (or of given size) is also can be made parallaly.
		(In kmean algorithm we manually decides two or more centroid values and compute values of all vectors around it)
		-------------
		|   |   |   |
	(4*4)	|   |   |   | (Image is divided in blocks of size 4*4 or of given size)
		-------------
		|   |   |   |
		|   |   |   |
		-------------
		|   |   |   |
		|   |   |   | (4*4)
		-------------
	b) Clustering of number of vectors is independent process and hence it can be computed parallaly.
	c) Mapping of those computed centroid vectors to real image is also independent one.
	
