#include <bits/stdc++.h>
using namespace std;
int sdrs[10001]={};
int main()
{
    cin.sync_with_stdio(0);
    cin.tie(0);
    int sdrnum,ldrs,ranking,sdrank;
    cin>>sdrnum>>ldrs>>ranking;
    for(int i=0;i<sdrnum;i++)
    {
        cin>>sdrank;
        sdrs[i]=sdrank;
    }
    sort(sdrs,sdrs+sdrnum);
    int cnt=1,totpow=0;
    for(int i=sdrnum-1;i>=0;i--)
    {
        if(cnt==ranking) totpow+=sdrs[i];
        cnt++;
        if(cnt==ldrs+1) cnt=1;
    }
    cout<<totpow;
}