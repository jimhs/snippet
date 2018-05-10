#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_N=100;

int n,s[MAX_N],t[MAX_N];

pair<int,int> itv[MAX_N];

void input(){
	printf("leading vals(n):\n");
	scanf("%d",&n);

	printf("array vals [s](x1 x2 ... xn 0):\n");
	for(int i=0;i<n;i++)
		scanf("%d",&s[i]);

	printf("array vals [t](x1 x2 ... xn 0):\n");
	for(int i=0;i<n;i++)
		scanf("%d",&t[i]);

	printf("\n");
}
	
void solve(){
	//r is end time of last chosed job
	int res=0, r=0;

	for(int i=0;i<n;i++){
		itv[i].first=t[i];
		itv[i].second=s[i];
	}

	printf("unsorted: \n");
	for(int i=0;i<n;i++)
		printf("(%d,%d) ",itv[i].first,itv[i].second);
	printf("\n\n");

	sort(itv,itv+n);
	
	printf("sorted: \n");
	for(int i=0;i<n;i++)
		printf("(%d,%d) ",itv[i].first,itv[i].second);
	printf("\n\n");
	
	for(int i=0;i<n;i++){
		printf("iter:%d r:%d res:%d\n",i,r,res);	
		if(r<itv[i].second){
			res++;
			r=itv[i].first;
		}
	}
	printf("RES:%d\n",res);
}

int main(){
	input();
	solve();
	return 0;
}
