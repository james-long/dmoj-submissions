#include <bits/stdc++.h>
using namespace std;
int main()
{
    int temptot;
    scanf("%i",&temptot);
    for(int x=0;x<temptot;x++)
    {
        stack<int>top,bot,q;
        bot.push(0);
        int tot,temp;
        scanf("%i",&tot);
        for (int i=0;i<tot;i++)
        {
            scanf("%i",&temp);
            top.push(temp);
        }
        while (!top.empty())
        {
            while (q.top()==bot.top()+1)
            {
                bot.push(q.top());
                q.pop();
            }
            int val=top.top();
            top.pop();
            if (val==bot.top()+1) bot.push(val);
            else q.push(val);
        }
        while (q.top()==bot.top()+1)
        {
            bot.push(q.top());
            q.pop();
        }
        if (q.empty()) printf("Y\n");
        else printf("N\n");
    }
    return 0;
}