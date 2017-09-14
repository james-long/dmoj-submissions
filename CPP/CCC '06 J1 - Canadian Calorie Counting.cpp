#include <cstdio>
#include <vector>
int main(){
    std::vector<int>vals{0,461,431,420,0,100,57,70,0,130,160,118,0,167,266,75,0};
    int a,b,c,d;
    scanf("%i%i%i%i",&a,&b,&c,&d);
    printf("Your total Calorie count is %i.",vals[a]+vals[b+4]+vals[c+8]+vals[d+12]);
}