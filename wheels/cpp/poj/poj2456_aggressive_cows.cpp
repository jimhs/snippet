/*
 *	poj2456_aggressive_cows.cpp
 */

#include <cstdio>
#include <algorithm>

using namespace std;

#define MAX_N 100
#define UB 999

int L, n, x[MAX_N];

//use console values
void input(){
	printf("poj2456_aggressive_cows\n");
	printf("leading vals(L n):");
	scanf("%d %d",&L,&n);

	printf("array vals(x1 x2 ... xn 0):");
	for(int i=0;i<n;i++)
		scanf("%d",&x[i]);
}
	
bool C(int d){
	int last=0;
	for(int i=1; i<L; i++){
		int crt = last + 1;
		while(crt<n && x[crt]-x[last]<d)
			crt++;

		if(crt==n) return false;
		last = crt;
	}
	return true;
}

void solve(){
	int lb=0, ub=UB;

	sort(x,x+n);

	while(ub-lb>1){
		int mid=(lb+ub)/2;
		if(C(mid))lb=mid;
		else ub=mid;
	}	
	printf("RES:%d\n",lb);
}

int main(){
	//init();
	input();
	solve();
	return 0;
}
