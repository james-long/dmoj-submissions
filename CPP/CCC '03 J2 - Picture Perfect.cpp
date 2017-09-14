#include <cstdio>
#include <cmath>
using namespace std;
int main(){
    int pics;
    for(;;){
        scanf("%i",&pics);
        if (pics!=0){
            int sqrtpics;
            sqrtpics=sqrt(pics);
            int second=pics%sqrtpics;
            while(second!=0){
                sqrtpics-=1;
                second=pics%sqrtpics;
            }
            int fin=pics/sqrtpics;
            printf("Minimum perimeter is %i with dimensions %i x %i\n",sqrtpics*2+fin*2,sqrtpics,fin);
        }
        else break;
    }
}