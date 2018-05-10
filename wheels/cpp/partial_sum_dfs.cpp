#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_N=50;

int L,n;
int x[MAX_N];

void input(){
	printf("leading vals(L n):\n");
	scanf("%d %d",&L,&n);

	printf("array vals(x1 x2 ... xn 0):\n");
	for(int i=0;i<n;i++)
		scanf("%d ",&x[i]);
}
	
bool dfs(int i,int sum){
	
	if (i==n) return sum==L;

	//without x[i]
	if (dfs(i+1, sum)) return true;

	//with x[i]
	if (dfs(i+1,sum+x[i])) return true;

	return false;
}

void solve(){
	
	if (dfs(0,0)) printf("yes\n"); 
	else printf("no\n");
}

int main(){
	input();
	solve();
	return 0;
}
