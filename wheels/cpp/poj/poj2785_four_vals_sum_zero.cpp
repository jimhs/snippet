/*
 *	poj2785_four_vals_sum_zero.cpp
 */

#include <cstdio>
#include <algorithm>

using namespace std;

#define MAX_N 100

int L, n, x[MAX_N][MAX_N];

/*
//use default values
void init(){
}
*/

//use console values
void input(){
	printf("leading vals(L):");
	scanf("%d",&L);

	for(int j=0;j<4;j++){
		printf("array vals %c[] :",'A'+j);
		for(int i=0;i<L;i++)
			scanf("%d",&x[j][i]);
	}
}
	
void solve(){
	
	int CD[MAX_N*MAX_N];

	for(int i=0;i<L;i++)
		for(int j=0;j<L;j++)
			CD[i*L+j]=x[2][i]+x[3][j];

	sort(CD,CD+L*L);
		
	long long res=0;

	for(int i=0;i<L;i++)
		for(int j=0;j<L;j++){
			int cd=-(x[0][i]+x[1][j]);
			res+=upper_bound(CD,CD+L*L,cd)-lower_bound(CD,CD+L*L,cd);
		}	

	printf("RES:%lld\n",res);
}

int main(){
	//init();
	input();
	solve();
	return 0;
}
