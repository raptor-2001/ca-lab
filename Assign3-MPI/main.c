#include<mpi.h>
#include<stdio.h>
#include<string.h>

void send_data_branch(int *arr, int n, int size, int rank);
void receive_data_branch(int my_rank);
void receive_data_headOffice(int my_rank, int size);


int main(int argc, char **argv){
	MPI_Init(&argc, &argv);
	
	int rank, size;
	MPI_Comm_rank(MPI_COMM_WORLD, &rank);
	MPI_Comm_size(MPI_COMM_WORLD, &size);
	
	printf("%d ", rank);
	if(rank == 0){
		receive_data_headOffice(rank, size);
	}
	else{
		int n=5;
		int arr[n];
		for(int i=0;i<n;i++){
			arr[i] = i+rank;
		}
		
		send_data_branch(arr, n, size, rank);
		receive_data_branch(rank);
	}
	
	MPI_Finalize();
}

void send_data_branch(int *arr, int n, int size, int rank){
	// printf("Branch Send\n");
	MPI_Send(arr, n, MPI_INT, 0, 8, MPI_COMM_WORLD);
}

void receive_data_branch(int my_rank){
	// printf("Branch Receive\n");
	int arr[6];
	MPI_Status status;
	MPI_Recv(arr, 6, MPI_INT, 0, 8, MPI_COMM_WORLD, &status);
	
	printf("Sum of items computed for Branch %d is %d\n", my_rank, arr[5]);
}

void receive_data_headOffice(int my_rank, int size){
	// printf("Head Office Receive\n");
	int arr[6];
	MPI_Status status;
	for(int i=1;i<size;i++){
		MPI_Recv(arr, 5, MPI_INT, i, 8, MPI_COMM_WORLD, &status);
		
		int sum=0;
		for(int i=0;i<5;i++){
			sum += arr[i];
		}
		arr[5] = sum;
		MPI_Send(arr, 6, MPI_INT, i, 8, MPI_COMM_WORLD);
	}
}

