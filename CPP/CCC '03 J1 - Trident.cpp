#include <iostream>
#include <string>
using namespace std;
int main(){
int t,s,h;
cin>>t>>s>>h;
string spc1=string(s,' '),spc2=string(s+1,' '),line=string(s*2+3,'*')+"\n";
for (;t>0;t--) cout<<'*'<<spc1<<'*'<<spc1<<'*'<<"\n";
cout<<line;
for (;h>0;h--) cout<<spc2<<'*'<<"\n";}