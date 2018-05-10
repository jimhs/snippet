#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_N=1000;

typedef long long ll;

int n;
int x[MAX_N];

void input(){
	printf("leading vals(n):");
	scanf("%d",&n);

	printf("array vals(x1 x2 ... xn 0):");
	for(int i=0;i<n;i++)
		scanf("%d",&x[i]);
}
	
void solve(){
	ll res=0;

	while(n>1){
		//most and less short
		int mii1=0,mii2=1;
		if(x[mii1]>x[mii2])swap(mii1,mii2);

		for(int i=2;i<n;i++){
			if(x[i]<x[mii1]){
				mii2=mii1;
				mii1=i;
			}
			else if(x[i]<x[mii2])
				mii2=i;
		}
	
		int t=x[mii1]+x[mii2];
		res+=t;

		if(mii1==n-1)swap(mii1,mii2);
		x[mii1]=t;
		x[mii2]=x[n-1];
		n--;
	}

	printf("RES:%lld\n",res);
}

int main(){
	input();
	solve();
	return 0;
}
