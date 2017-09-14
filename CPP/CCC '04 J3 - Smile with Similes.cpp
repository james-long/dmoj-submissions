#include <iostream>
#include <vector>
#include <string>
using namespace std;
int main(){
    int adj,noun;
    vector<string> adjs,nouns;
    cin>>adj>>noun;
    for(string word;adj>0;adj--){cin>>word;adjs.push_back(word);}
    for(string word;noun>0;noun--){cin>>word;nouns.push_back(word);}
    for(string a:adjs){
        for(string n:nouns){
            cout<<a<<" as "<<n<<"\n";
        }
    }
}