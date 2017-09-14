#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;
int isprime(int val){
    for (int x=2;x<val;x++) if (val%x==0) return 0;
    return val;
}
int main(){
    int tot,filler;
    vector<int>nums{},primes{2};
    cin>>tot;
    for (;tot>0;tot--) {cin>>filler;nums.push_back(filler);}
    double top=*max_element(nums.begin(),nums.end());
    for (int i=3;i<=sqrt(top);i++) if (isprime(i)!=0) primes.push_back(i);
    for (int num:nums){
        vector<int>facs{};
        while(num!=1){
            bool yn=true;
            for (int prime:primes){
                if (num%prime==0) {facs.push_back(prime);num/=prime;yn=false;}
            }
            if (yn==true) {facs.push_back(num);break;}
        }
        sort(facs.begin(),facs.end());
        for (int ans:facs) cout<<ans<<" ";
        cout<<"\n";
    }

}