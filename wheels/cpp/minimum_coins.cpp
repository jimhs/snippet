#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_N=50;
const int V[6]={1,5,10,50,100,500};

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
	int res=0;
	for(int i=5;i>=0;i--){
		int t=min(L/V[i],x[i]);
		L-=t*V[i];
		res+=t;
	}	
	printf("%d\n",res);
}

int main(){
	input();
	solve();
	return 0;
}
