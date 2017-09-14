#include <bits/stdc++.h>
using namespace std;
int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    int eps,qs,temp1,temp2;
    cin>>eps>>qs;
    int rsums[eps+1];
    rsums[0]=0;
    for(int i=1;i<eps+1;i++)
    {
        cin>>temp1;
        rsums[i]=rsums[i-1]+temp1;
    }
    for(int i=0;i<qs;i++)
    {
        cin>>temp1>>temp2;
        cout<<rsums[eps]-rsums[temp2]+rsums[temp1-1]<<"\n";
    }
}