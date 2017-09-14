#include <bits/stdc++.h>
using namespace std;
int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    int eps,qs,temp,q1,q2;
    cin>>eps>>qs;
    int ratings[eps+1][10];
    for (int i=0;i<=eps;i++)
    {
        for(int x=0;x<10;x++) ratings[i][x]=0;
    }
    for(int i=1;i<=eps;i++)
    {
        cin>>temp;
        for(int x=0;x<10;x++) ratings[i][x]=ratings[i-1][x];
        ratings[i][temp-1]=ratings[i-1][temp-1]+1;
    }
    int allratings[1][10];
    for(int query=0;query<qs;query++)
    {
        cin>>q1>>q2;
        for(int i=0;i<10;i++)
        {
            allratings[0][i]=ratings[eps][i]-ratings[q2][i]+ratings[q1-1][i];
        }
        for(int i=9;i>=0;i--)
        {
            if (allratings[0][i]!=0)
            {
                cout<<i+1<<" "<<allratings[0][i]<<"\n";
                break;
            }
        }
    }
}