#include <cstdio>
int main(){
    int f,l,ctr=0;
    scanf("%i%i",&f,&l);
    for (int x=1;x<=f;x++) for (int y=1;y<=l;y++) if (x+y==10) ctr+=1;
    switch(ctr){
    case(1): printf("There is 1 way to get the sum 10.");break;
    default: printf("There are %i ways to get the sum 10.",ctr);
    }
}