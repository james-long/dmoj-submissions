#include <cstdio>
#include <vector>
#include <algorithm>
int main(){
    int a,b,c;
    scanf("%i%i%i",&a,&b,&c);
    std::vector<int>v{a,b,c};
    std::sort(v.begin(),v.end());
    printf("%i",v[1]);
}