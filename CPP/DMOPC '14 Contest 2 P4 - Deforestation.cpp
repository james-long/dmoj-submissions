#include <bits/stdc++.h>
using namespace std;
int main()
{
    int treenum,querynum,temp,val1,val2;
    scanf("%i",&treenum);
    int prefs[treenum+1];
    prefs[0]=0;
    for(int i=0;i<treenum;i++)
    {
        scanf("%i",&temp);
        prefs[i+1]=prefs[i]+temp;
    }
    scanf("%i",&querynum);
    for(int i=0;i<querynum;i++)
    {
        scanf("%i%i",&val1,&val2);
        printf("%i\n",prefs[val2+1]-prefs[val1]);
    }
}