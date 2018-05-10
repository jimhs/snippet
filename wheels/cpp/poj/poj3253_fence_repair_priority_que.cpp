/*
 *	poj3253_fence_repair_priority_que.cpp
 */

#include <cstdio>
#include <queue>

using namespace std;

const int MAX_N=1000;

typedef long long ll;

int x[MAX_N];
int n=3;

//use console values
void input(){
	printf("leading vals(n):");
	scanf("%d",&n);

	printf("array vals(x1 x2 ... xn 0):");
	for(int i=0;i<n;i++)
		scanf("%d",&x[i]);
}

void solve(){
	ll res=0;

	priority_queue<int, vector<int>, greater<int>> que;

	for(int i=0;i<n;i++)que.push(x[i]);

	while(que.size()>1){
		//fetch shortest and less shorter ones
		int l1,l2;
		l1=que.top(); que.pop();
		l2=que.top(); que.pop();

		res+=l1+l2;
		que.push(l1+l2);
	}
	printf("RES:%lld\n",res);
}

int main(){
	input();
	solve();
	return 0;
}
