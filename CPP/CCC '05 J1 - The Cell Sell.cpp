#include <iostream>
double priceA(int d,int e,int w){
    if (d>=100) return (d-100)*.25+e*.15+w*.2;
    else return e*.15+w*.2;
}
double priceB(int d,int e,int w){
    if (d>=250) return (d-250)*.45+e*.35+w*.25;
    else return e*.35+w*.25;
}
int main(){
    int d,e,w;
    std::cin>>d>>e>>w;
    double a=priceA(d,e,w),b=priceB(d,e,w);
    std::cout<<"Plan A costs "<<a<<"\nPlan B costs "<<b;
    if(a==b)std::cout<<"\nPlan A and B are the same price.";
    else if(a>b)std::cout<<"\nPlan B is cheapest.";
    else std::cout<<"\nPlan A is cheapest.";
}