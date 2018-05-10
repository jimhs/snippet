#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_N=1000;

int L,n;
int x[MAX_N];

void input(){
	printf("leading vals(L n):\n");
	scanf("%d %d",&L,&n);

	printf("array vals(x1 x2 ... xn 0):\n");
	for(int i=0;i<n;i++)
		scanf("%d",&x[i]);

	printf("\n");
}
	
void solve(){
	int i=0,res=0;

	sort(x,x+n);

	while(i<n){
		//s is most left pos not covered
		int s=x[i++];

		//march right till reach pos >s+L
		while(i<n && x[i]<=s+L) i++;

		//note p as newly marked pos
		int p=x[i-1];

		while(i<n && x[i]<=p+L) i++;

		res++;
	}
	printf("%d\n\n",res);
}

int main(){
	input();
	solve();
	return 0;
}
