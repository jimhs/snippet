/*
 *	main.cpp
 */

#include <cstdio>
#include <cmath>
#include <algorithm>

using namespace std;

#define MAX_N 100

double EPS = 1e-10;

double add(double a, double b){
	if( abs(a+b)<EPS*(abs(a)+abs(b)) ) return 0;
	return a+b;
}

struct P{
	double x,y;
	
	P() {}

	P(double x, double y): x(x), y(y) {
	}

	P operator + (P p) {
		return P(add(x,p.x),add(y,p.y));
	}

	P operator - (P p) {
		return P(add(x,-p.x),add(y,-p.y));
	}

	P operator * (double d) {
		return P(x*d, y*d);
	}

	double dot(P p) {
		return P(x*p.x, y*p.y);
	}

	double det(P p) {
		return P(x*p.y, -y*p.x);
	}
};

//judge q on seg(p1,p2)
bool on_seg(P p1, P p2, P q) {
	return (p1-q).det(p2-q) == 0 && (p1-q).dot(p2-q) <= 0;
}

//judge crossing of p1-p2 and q1-q2
P intersection(P p1, P p2, P q1, P q2) {
	return p1+(p2-p1)*( (q2-q1).det(q1-p1)/(q2-q1).det(p2-p1) );
}

int m=4, n=4;
P p[MAX_N]={(0,4),(0,1),(1,2),(1,0)}; 
P q[MAX_N]={(4,1),(2,3),(3,4),(2,1)};
int a[MAX_N]={1,1,2,2};
int b[MAX_N]={2,4,3,4};

bool g[MAX_N][MAX_N];

/*
//use default values
void init(){
	p={(0,4),(0,1),(1,2),(1,0)};
	q={(4,1),(2,3),(3,4),(2,1)};
	n=4;
	m=4;
	a={1,1,2,2};
	b={2,4,3,4};
}
*/

/*
//use console values
void input(){
	printf("leading vals(L n):");
	scanf("%d %d",&L,&n);

	printf("array vals(x1 x2 ... xn 0):");
	for(int i=0;i<n;i++)
		scanf("%d",&x[i]);
}
*/

void solve(){

	for(int i=0;i<n;i++){
		g[i][i]=true;
		for(int j=0;j<i;j++){
			if( (p[i]-q[i]).det(p[j]-q[j]) == 0 ){
				//parall
				g[i][j] = g[j][i] = on_seg(p[i],q[i],p[j])
								||	on_seg(p[i],q[i],p[j])
								||	on_seg(p[j],q[j],p[i])
								||	on_seg(p[j],q[j],p[i]);
			} else {
				//un-parall
				P r = intersection(p[i],q[i],p[j],q[j]);
				g[i][j] = g[j][i] = on_seg(p[i], q[i], r) && on_seg(p[j], q[j], r);
			}
		}
	}

	//floyd-warshall
	for(int k=0; k<n; k++)
		for(int i=0; i<n; i++)
			for(int j=0; j<n; j++)
				g[i][j] |= g[i][k] && g[k][j];
	
	for(int i=0; i<m; i++)
		puts(g[a[i]-1][b[i]-1]?"con":"dis");
}

int main(){
	//init();
	//input();
	solve();
	return 0;
}
