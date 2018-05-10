/*
 *	region_count.cpp
 */

#include <cstdio>
#include <algorithm>
#include <vector>
#include <queue>
#include <cstring>

using namespace std;

#define MAX_N 100

int w, h, n;

int	x[4][5]={{1,1,4,9,10},
			 {6,10,4,9,10},
			 {4,8,1,1,6},
			 {4,8,10,5,10}};

bool fld[MAX_N*6][MAX_N*6];

void init(){
	w=10,h=10,n=5;
}

//use console values
//void input(){
//	printf("leading vals(w h n):");
//	scanf("%d %d %d",&w,&h,&n);
//
//	for(int i=0;i<2;i++)
//		for(int j=0;j<2;j++){
//			printf("array vals %c%d :",'x'+i,j+1);
//			//input order: x1 x2 y1 y2
//			for(int k=0;k<n;k++)
//				scanf("%d",&x[i*2+j][k]);
//		}
//}
	
int compress(int *x1, int *x2, int w){
	vector<int> xs;

	for(int i=0;i<n;i++)
		for(int d=-1;d<2;d++){
			int tx1=x1[i]+d, tx2=x2[i]+d;
			if(1<=tx1 && tx1<=w)
					xs.push_back(tx1);
			if(1<=tx2 && tx2<=w)
					xs.push_back(tx2);
		}

	sort(xs.begin(),xs.end());

	xs.erase(unique(xs.begin(),xs.end()),xs.end());

	for(int i=0;i<n;i++){
		x1[i]=find(xs.begin(),xs.end(),x1[i])-xs.begin();
		x2[i]=find(xs.begin(),xs.end(),x2[i])-xs.begin();
	}

	return xs.size();
}

void solve(){
	
	w=compress(x[0],x[1],w);
	h=compress(x[2],x[3],h);

	memset(fld,0,sizeof(fld));

	for(int i=0;i<n;i++)
		for(int y=x[2][i];y<=x[3][i];y++)
			for(int x_=x[0][i];x_<=x[1][i];x_++)
				fld[y][x_]=true;

	int res=0;
	
	for(int y=0;y<h;y++)
		for(int x=0;x<w;x++){
			if(fld[y][x])
				continue;
			res++;

			//bfs
			queue<pair<int,int>> que;
			que.push(make_pair(x,y));

			while(!que.empty()){
				int sx=que.front().first, 
					sy=que.front().second;
				que.pop();

				int dx[4]={1,0,-1,0},
					dy[4]={0,1,0,-1};

				for(int i=0;i<4;i++){
					int tx=sx+dx[i],
						ty=sy+dy[i];

					if(fld[ty][tx] || tx<0 || w<=tx || ty<0 || h<=ty)
						continue;
					
					que.push(make_pair(tx,ty));

					fld[ty][tx]=true;
				}
			}
		}

	printf("RES:%d\n",res);
}

int main(){
	init();
	//input();
	solve();
	return 0;
}
