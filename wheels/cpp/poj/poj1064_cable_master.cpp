/*
 *	poj1064_cable_master.cpp
 */

#include <cstdio>
#include <cmath>

using namespace std;

#define MAX_N 100
#define UB 999.99

int L, n;
float x[MAX_N];

/*
//use default values
void init(){
}
*/

//use console values
void input(){
	printf("leading vals(L n):");
	scanf("%d %d",&L,&n);

	printf("array vals(x1 x2 ... xn 0):");
	for(int i=0;i<n;i++)
		scanf("%f",&x[i]);
}
	
bool C(double l){
	int num=0, i=0;
	for(;i<n;i++)
		num+=(int)(x[i]/l);

	return num>=L;
}

void solve(){
	double lb=0, ub=UB;

	for(int i=0;i<100;i++){
		double mid=(lb+ub)/2;
		if(C(mid))lb=mid;
		else ub=mid;
	}	
	printf("RES:%.2f\n",floor(ub*100)/100);
}

int main(){
	//init();
	input();
	solve();
	return 0;
}
