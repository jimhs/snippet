#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_N=1000;

int n;
char x[MAX_N+1];

void input(){
	printf("leading vals(n):\n");
	scanf("%d",&n);

	printf("array vals(x1 x2 ... xn 0):\n");
	for(int i=0;i<=n;i++)
		scanf("%c",&x[i]);

	printf("array:");
	for(int i=0;i<=n;i++)
		printf("%c",x[i]);
	printf("\n\n");
}
	
void solve(){
	int a=0, b=n;

	while(a<=b){
		
		bool left=false;

		for(int i=0;a+i<=b;i++){
			if(x[a+i]<x[b-i]){
				left=true;
				break;
			}
			else if(x[a+i]>x[b-i]){
				left=false;
				break;
			}
		}	
		if(left)putchar(x[a++]);
		else putchar(x[b--]);
	}
	putchar('\n');
}

int main(){
	input();
	solve();
	return 0;
}
