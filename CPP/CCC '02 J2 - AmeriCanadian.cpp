#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;
vector<string> vowels={"a","e","i","o","u","y"};
int main(){
string word;
cin>>word;
while(word!="quit!"){
    int len=word.length();
    if (len>4 && word.substr(len-2,2)=="or" && find(vowels.begin(), vowels.end(), word.substr(len-3,1))==vowels.end())
        cout<<word.replace(len-2,3,"our")<<"\n";
    else cout<<word<<"\n";
    cin>>word;
}}