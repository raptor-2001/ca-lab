#include<bits/stdc++.h>
using namespace std;

void luDecomposition(vector<vector<int>> arr, vector<int> &voters){

    int row = arr.size();

    vector<vector<int>> lower(row, vector<int> (row, 0));
    vector<vector<int>> upper(row, vector<int> (row, 0));

    // Decomposition of matrix into lower and upper triangular matrix.
    for(int i=0;i<row;i++){

        // Upper Triangular.
        for(int k=i;k<row;k++){
            int sum=0;
            for(int j=0;j<i;j++){
                sum += (lower[i][j]*upper[j][k]);
            }
            upper[i][k] = arr[i][k] - sum;
        }

        // Lower Triangular.
        for(int k=i;k<row;k++){
            // Diagonal will be 1.
            if(i == k){
                lower[i][k] = 1;
            }
            else{
                int sum=0;
                for(int j=0;j<i;j++){
                    sum += (lower[k][j]*upper[j][i]);
                }
                lower[k][i] = (arr[k][i]-sum)/upper[i][i];
            }
        }
    }

    // Now I have both lower and upper triangular matrix.
    /*
        Initially AX = B was the equation. Now for simplicity we have breaked the equation int to LUX = B, where A = LU.
        Let's consider UX = Y. Hence, LY = B. So first we will identify L with the help of this equation.
    */

    vector<float> y(arr.size());

    for(int i=0;i<lower.size();i++){
        float sum = 0;
        for(int j=0;j<i;j++){
            sum += (lower[i][j]*y[j]);
        }
        y[i] = float((voters[i]-sum)/lower[i][i]);
    }

    // Now as we have the array y, So we can finally compute required amount to be spent on particular advertisement. UX = Y
    vector<int> x(arr.size());
    for(int i=arr.size()-1;i>=0;i--){
        float sum = 0;
        for(int j=row-1;j>i;j--){
            sum += (upper[i][j]*x[j]);
        }
        x[i] = float((y[i] - sum)/upper[i][i]);
    }

    cout<<"Expenses on"<<endl;
    for(int i=0;i<x.size();i++){
        cout<<"Policy #"<<i+1<<" ";
        cout<<abs(x[i]*4000)<<endl;
    }
}

int main()
{
    vector<vector<int>> arr = {
        {-2, 5, 3, 6}, {8, 2, -5, -2}, {1, 3, 10, 4}, {10, 6, -2, 5}
    };

    vector<int> voters(arr.size());
    for(int i=0;i<arr.size();i++){
        cin>>voters[i];
    }

    luDecomposition(arr, voters);
    return 0;
}