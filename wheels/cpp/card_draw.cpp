#include <cstdio>

/*
n:num of cards	
m:sum
k:list of cards
*/

const int MAX_N = 50;
int n, m, k[MAX_N];
int kk[MAX_N*MAX_N];

bool binary_search(int x){
	int l=0,r=n*n;

	while(r-l>=1){

		int i=(l+r)/2;
		if(kk[i]==x)return true;
		else if(kk[i]<x)l=i+1;
		else r=i;
	}
	return false;
}
int main(){
	

	int n, m, k[MAX_N];

	scanf("%d %d", &n, &m);

	for (int i=0; i<n; i++){
		scanf("%d", &k[i]);
	}

	bool f = false;

	for (int a=0; a<n; a++){
		for (int b=0; b<n; b++){
			for (int c=0; c<n; c++){
				for (int d=0; d<n; d++){
					if(k[a]+k[b]+k[c]+k[d]==m){
						f = true;
					}
				}
			}
		}
	}

	if (f) puts("yes\n");
	else  puts("no\n");
	
	return 0;

}
