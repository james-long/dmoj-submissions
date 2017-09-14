#include <string>
#include <iostream>
using namespace std;
int main()
{
    float hr=-1.0,rating;
    int total;
    string highest=" ",current=" ";
    cin>>total;
    for(int i=0;i<total;i++)
    {
        cin>>current>>rating;
        if (rating>hr) {hr=rating; highest=current;}
    }
    cout<<highest;
}