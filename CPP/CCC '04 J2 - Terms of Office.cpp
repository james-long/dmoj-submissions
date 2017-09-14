#include <cstdio>
int main(){
    int bot,top;
    scanf("%i%i",&bot,&top);
    for(int i=0;bot+i<=top;bot+=60) printf("All positions change in year %i\n",bot+i);
}