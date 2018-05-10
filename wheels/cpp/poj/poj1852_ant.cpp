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
	
void solve(){
	int minT=0;
	for(int i=0;i<n;i++)
		minT = max(minT,min(x[i],L-x[i]));
	
	printf("%d\n",minT);
}

int main(){
	input();
	solve();
	return 0;
}
