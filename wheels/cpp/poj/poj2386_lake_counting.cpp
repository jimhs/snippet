#include <cstdio>
#include <algorithm>

using namespace std;

const int MAX_M=50, MAX_N=50;
const int N=10,M=12;

char field[N][M]={
	/*can't init like this
	"W........WW.",	
	".WWW.....WWW",	
	"....WW...WW.",	
	".........WW.",	
	".........W..",	
	"..W......W..",	
	".W.W.....WW.",	
	"W.W.W.....W.",	
	".W.W......W.",	
	"..W.......W."};
	*/
	{'W','.','.','.','.','.','.','.','.','W','W','.'},
	{'.','W','W','W','.','.','.','.','.','W','W','W'},
	{'.','.','.','.','W','W','.','.','.','W','W','.'},
	{'.','.','.','.','.','.','.','.','.','W','W','.'},
	{'.','.','.','.','.','.','.','.','.','W','.','.'},
	{'.','.','W','.','.','.','.','.','.','W','.','.'},
	{'.','W','.','W','.','.','.','.','.','W','W','.'},
	{'W','.','W','.','W','.','.','.','.','.','W','.'},
	{'.','W','.','W','.','.','.','.','.','.','W','.'},
	{'.','.','W','.','.','.','.','.','.','.','W','.'}};

void dfs(int x, int y){
	
	//replace current pos
	field[x][y]='.';

	//iter connected eight pos
	for (int dx=-1;dx<=1;dx++){
		for (int dy=-1;dy<=1;dy++){
			//move to
			int nx=x+dx,ny=y+dy;
			//creteria
			if(	nx>=0 && ny>=0 && nx<=N && ny<=M && field[nx][ny]=='W' )
				dfs(nx,ny);
		}
	}

	return;

}
	
void solve(){
	int res=0;
	for(int i=0;i<N;i++){
		for(int j=0;j<M;j++){
			if( field[i][j]=='W' ){
				//start where exist a 'W'
				dfs(i,j);
				res++;
			}
		}
	}
	printf("%d\n",res);
}

int main(){
	solve();
	return 0;
}
