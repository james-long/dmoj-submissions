#include <bits/stdc++.h>
using namespace std;
int main()
{
    string word;
    bool yn=true;
    string accept="IOSHZXN";
    cin>>word;
    for(char &c:word)
    {
        if (accept.find(c)==string::npos)
        {
            cout<<"NO";
            yn=false;
            break;
        }
    }
    if(yn)cout<<"YES";
}