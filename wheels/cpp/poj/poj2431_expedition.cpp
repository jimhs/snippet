/*
 *	poj2431_expedition.cpp
 */

#include <cstdio>
//#include <algorithm>
#include <queue>

using namespace std;

const int MAX_N=1000;

int L,P,N;
//int A[MAX_N+1],B[MAX_N+1];

int	A[5]={10,14,20,21};
int	B[5]={10,5,2,4};

void init(){
	L=25;
	P=10;
	N=4;
}

void input(){
	printf("leading vals(L P N):");
	scanf("%d %d %d",&L,&P,&N);

	printf("array vals A(x1 x2 ... xn 0):\n");
	for(int i=0;i<N;i++)
		scanf("%d",&A[i]);
	
	printf("array vals B(x1 x2 ... xn 0):\n");
	for(int i=0;i<N;i++)
		scanf("%d",&B[i]);
}
	
void solve(){
	//consider dest as last oil station
	A[N]=L;
	B[N]=0;
	N++;

	//que to maintain oil station
	priority_queue<int> que;

	int res=0, pos=0, tank=P;

	for(int i=0;i<N;i++){
		//how far till next spot?
		int d=A[i]-pos;

		//keep filling till enough to next spot
		while(tank-d<0){
			if(que.empty()){puts("-1"); return;}
			tank+=que.top();
			que.pop();
			res++;
		}

		tank-=d;
		pos=A[i];
		que.push(B[i]);
	}
	printf("RES:%d\n",res);
}

int main(){
	init();
//	input();
	solve();
	return 0;
}
