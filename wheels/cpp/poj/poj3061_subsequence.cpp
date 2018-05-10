/*
 *	poj3061_subsequence.cpp
 */

#include <cstdio>
#include <algorithm>

using namespace std;

#define MAX_N 100

int L, n, x[MAX_N];

//use console values
void input(){
	printf("leading vals(L n):");
	scanf("%d %d",&L,&n);

	printf("array vals(x1 x2 ... xn 0):");
	for(int i=0;i<n;i++)
		scanf("%d",&x[i]);
}
	
void solve(){
	int res=n+1;
	int s=0, t=0, sum=0;

	for(;;){
		while(t<n && sum<L)
			sum+=x[t++];

		if(sum<L)
			break;

		res=min(res,t-s);

		sum-=x[s++];
	}	

	if (res>n)
		res=0;

	printf("RES:%d\n",res);
}

int main(){
	//init();
	input();
	solve();
	return 0;
}
