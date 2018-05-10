#include <cstdio>
#include <algorithm>

#define INF 9999

using namespace std;

const int MAX_N=1000;

struct edge {int fr, to, cst;};

edge es[MAX_N];

int V,E;
int d[MAX_N];

void input(){
	printf(	"bellman-ford shortest path\n"
			"leading vals(V E):" );
	scanf("%d %d",&V,&E);

	printf("array vals(fr to cst):\n");
	for(int i=0;i<E;i++){
		printf("[%d]:",i);
		scanf("%d %d %d",&es[i].fr,&es[i].to,&es[i].cst);
	} printf("\n");
}
	
//shortest path
void solve(int s){
	//int res=0;
	for(int i=0;i<V;i++)d[i]=INF;
	d[s]=0;
	while(true){
		bool update = false;
		for(int i=0;i<E;i++){
			edge e=es[i];
			if(d[e.fr]!=INF && d[e.to]>d[e.fr]+e.cst){
				d[e.to]=d[e.fr]+e.cst;
				update=true;
			}
		}
		if(!update)break;
	}
	for(int i=0;i<V;i++) printf("d[%d]:%d\n",i,d[i]);
}

int main(){
	input();
	solve(0);
	return 0;
}
