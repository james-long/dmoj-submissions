#include <cstdio>
int main()
{
    int combos=0,minprint,p,g,r,o;
    scanf("%i%i%i%i%i",&p,&g,&r,&o,&minprint);
    int total=minprint;
    for (int tp=0;tp<=total;tp+=p){
        for (int tg=0;tg<=total;tg+=g){
            for (int tr=0;tr<=total;tr+=r){
                for (int to=0;to<=total;to+=o){
                    if (tp+tg+tr+to==total){
                        combos+=1;
                        if (tp/p+tg/g+tr/r+to/o<minprint) minprint=tp/p+tg/g+tr/r+to/o;
                        printf("# of PINK is %i # of GREEN is %i # of RED is %i # of ORANGE is %i\n",tp/p,tg/g,tr/r,to/o);
                    }
                }
            }
        }
    }
    printf("Total combinations is %i.\nMinimum number of tickets to print is %i.",combos,minprint);
}