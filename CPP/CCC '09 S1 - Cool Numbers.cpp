#include <bits/stdc++.h>
using namespace std;
int main()
{
    double a,b,ans=0;
    cin>>a>>b;
    int art=(int)cbrt(a);
    int brt=(int)cbrt(b);
    long long cubes[(int)(brt-art+1)];
    for(int i=art;i<(brt+2);i++)
    {
        cubes[(int)(i-art)]=pow(i,3);
    }
    for(long long d:cubes)
    {
        if (sqrt(d)==(int)(sqrt(d)) && d>=a && d<=b) ans+=1;
    }
    cout<<ans;
}