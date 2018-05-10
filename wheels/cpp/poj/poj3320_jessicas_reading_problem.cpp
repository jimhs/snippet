/*
 *	poj3320_jessicas_reading_problem.cpp
 */

#include <cstdio>
#include <algorithm>
#include <set>
#include <map>

using namespace std;

#define MAX_N 100

int L, x[MAX_N];

//use console values
void input(){
	printf("leading vals(L):");
	scanf("%d",&L);

	printf("array vals(x1 x2 ... xn 0):");
	for(int i=0;i<L;i++)
		scanf("%d",&x[i]);
}
	
void solve(){
	
	set<int> all;
	for(int i=0;i<L;i++)
		all.insert(x[i]);

	int n=all.size();

	int s=0, t=0, num=0;

	map<int,int> count;

	int res=L;

	for(;;){
		while(t<L && num<n)
			if(count[x[t++]]++ == 0)
				num++;

		if(num<n)
			break;

		res=min(res,t-s);

		if(--count[x[s++]] == 0)
			num--;
	}	
	printf("RES:%d\n",res);
}

int main(){
	//init();
	input();
	solve();
	return 0;
}
