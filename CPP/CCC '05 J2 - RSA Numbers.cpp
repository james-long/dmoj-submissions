#include <iostream>
#include <cmath>
using namespace std;
int main(){
    int b,e;
    cin>>b>>e;
    int counter=0;
    for (double i=b;i<=e;i++){
        if (sqrt(i)!=floor(sqrt(i))){
            int factors=0;
            for (double div=2;div<sqrt(i);div++) if (i/div==floor(i/div)) factors+=1;
            if (factors==1) counter+=1;
        }
    }
    cout<<"The number of RSA numbers between "<<b<<" and "<<e<<" is "<<counter;
}