#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_N = 50;

int n, a[MAX_N];

void solve(){
	int ans = 0;

	//let i<j<k
	for(int i=0;i<n;i++){
		for(int j=i+1;j<n;j++){
			for(int k=j+1;k<n;k++){
				int len=a[i]+a[j]+a[k];
				int ma=max(a[i],max(a[j],a[k]));
				int res=len-ma;

				if(ma<res){
					ans=max(ans,len);
				}
			}
		}
	}

	printf("%d\n",ans);
}

int main(){

	scanf("%d",&n);

	for(int i=0;i<n;i++)
	{
		scanf("%d",&a[i]);
	}

	solve();

	return 0;
}
