# ca-lab

#### Repo also has the theory of all assignments.
 
# Important instructions to download and install the dependencies

1. Clone or Download the repo in Pictures/Downloads of the System
2. Inside the ca-lab folder open the terminal and run <b> sudo bash commands.sh</b> It will run install all the dependencies.

# Important instructions to run the assignments 
# (Note: open terminal in each assignment folder to run the below instructions)

# Assign1 Profiling
1. g++ -Wall -pg main.cpp -o main
2. ./main 10000
3. gprof ./main

#### Description: Here you will get a Flat Profile and Call graph 

# Assign2 VQ
1. python2 main.py

#### Description: Here you will quantized image and some output on terminal which will have the dimesions of the input image and output image, also centroid graph. 

# Assign3 MPI Communication
1. mpicc -g -Wall -o main main.c -lm
2. mpiexec -n 4 ./main

#### Description: Here you will get simple output of all the branch offices collections.

# Assign4 Histogram
1. python2 main1.py

#### Description: Here you will get two histograms of one unequalized and other equalized, also the output will be conversion of rgb image to black and white image.

# Assign5 Linear Programming 
1. g++ main.cpp
2. ./a.out 500 1000 1500 2000

#### Description: Here you will get collections.

# Assign6 Hyper QuickSort
1. mpicc -g -Wall -o sort hypersort.c -lm
2. mpiexec -n 2 ./sort input.txt output.txt

### Description: Data in input.txt has the unsorted array and then will get the sorted array in output.txt

# Assign7 AWK
1. awk -f AWK.awk demo.txt

### Description: The output is the student name grade and relative grade of each student.

# Assign8 Fractal Compression
1. python3 2020BTEIT00060.py

### Description: All the compressed images will the shown if the code is run.


# Recording of the Session
https://drive.google.com/drive/folders/1TX4FeJWERElpqUjCJRUmwS-xie5N2g-L



