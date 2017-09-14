#include <bits/stdc++.h>
using namespace std;
int main()
{
    int totd,day,mass,temp;
    scanf("%i",&totd);
    for (int i=1;i<=totd;i++)
    {
        scanf("%i",&day);
        mass=0;
        for (int i=0;i<day;i++)
        {
            scanf("%i",&temp);
            mass+=temp;
        }
        if (mass==0) printf("Weekend\n");
        else printf("Day %i: %i\n",i,mass);
    }
}