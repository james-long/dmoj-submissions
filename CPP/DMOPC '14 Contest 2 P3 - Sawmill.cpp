#include <bits/stdc++.h>
using namespace std;
int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    int total,temp;
    long nrg=0;
    cin>>total;
    int saws[total],logs[total];
    for(int i=0;i<total;i++)
    {
        cin>>temp;
        saws[i]=temp;
    }
    for(int i=0;i<total;i++)
    {
        cin>>temp;
        logs[i]=temp;
    }
    sort(saws,saws+total);
    sort(logs,logs+total);
    for(int i=0;i<total;i++)
    {
        nrg+=(saws[i]*logs[total-(i+1)]);
    }
    cout<<nrg;
}