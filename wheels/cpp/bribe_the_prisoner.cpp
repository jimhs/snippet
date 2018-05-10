/*
 *	bribe_the_prisoner.cpp
 */

#include <cstdio>
#include <algorithm>

#define INT_MAX 1000

using namespace std;

const int MAX_N=100;

int P,Q;
int x[MAX_N+2];

int dp[MAX_N+1][MAX_N+2];

void input(){
	printf("leading vals(P Q):");
	scanf("%d %d",&P,&Q);

	printf("array vals(x1 x2 ... xn 0):");

	for(int i=1;i<=Q;i++)
		scanf("%d",&x[i]);
}
	
void solve(){
	
	x[0]=0;
	x[Q+1]=P+1;

	for(int i=0;i<=Q;i++)
		dp[i][i+1]=0;

	for(int w=2;w<=Q+1;w++)
		for(int i=0;i+w<=Q+1;i++){
			//calc dp[i][j]
			int j=i+w, t=INT_MAX;
	
			//enum initial released prisoner, calc min cost
			for(int k=i+1;k<j;k++)
				t=min(t,dp[i][k]+dp[k][j]);

			//and plus additionally A[j]-A[i]-2
			dp[i][j]=t+x[j]-x[i]-2;
		}

	printf("RES:%d\n",dp[0][Q+1]);
}

int main(){
	//init();
	input();
	solve();
	return 0;
}
