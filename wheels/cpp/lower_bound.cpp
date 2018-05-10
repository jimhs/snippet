/*
 *	lower_bound.cpp
 */

#include <cstdio>

using namespace std;

const int MAX_N=1000;

int L,n;
int x[MAX_N];

//use console values
void input(){
	printf("leading vals(L n):");
	scanf("%d %d",&L,&n);

	printf("array vals(x1 x2 ... xn 0):\n");
	for(int i=0;i<n;i++)
		scanf("%d",&x[i]);
}
	
void solve(){

	int lb=-1, ub=n;
	while(ub-lb>1){

		int mid = (lb+ub)/2;

		if(x[mid]>L)
			ub=mid;
		else
			lb=mid;
	}

	//ub=lb+1 when loop quit
	printf("RES:%d\n",ub);
}

int main(){
	input();
	solve();
	return 0;
}
