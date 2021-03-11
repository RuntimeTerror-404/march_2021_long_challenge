#include <bits/stdc++.h>
using namespace std;

int main(){
    int N, H, x;
    N = 2, H = 6, x = 3;
    vector<int> v = {1, 2};
    sort(v.begin(), v.end());
    int sum = v[N-1] + x;
    if(H <= sum){
        cout<<"YES"<<endl;
    }
    else{
        cout<<"NO"<<endl;
    }
}

/*
H = hours he can solve the problem
x = hours left
*/