#include <iostream>
#include <stdio.h>
#include <math.h>
#include <cstring>
#include <vector>
#include <queue>
#include <algorithm>
#define MAX 31
#define INF 987654321
using namespace std;

struct node {
    int x,y,z;
    node() {}
    node(int _x,int _y,int _z) :x(_x),y(_y),z(_z) {}
};

int l,r,c;
node s,e;

char map[MAX][MAX][MAX];
bool chk[MAX][MAX][MAX];
int dist[MAX][MAX][MAX];

int dx[6] = {1,-1,0,0,0,0}; // 상,하
int dy[6] = {0,0,1,-1,0,0}; // 남,북
int dz[6] = {0,0,0,0,1,-1}; // 동,서

void bfs(){
    queue<node> q;
    q.push(s);
    chk[s.x][s.y][s.z] = true;
    dist[s.z][s.y][s.z] = 0;
    
    while(!q.empty()){
        int x = q.front().x;
        int y = q.front().y;
        int z = q.front().z;
        q.pop();
        
        if(x==e.x && y==e.y && z==e.z){
            cout << "Escaped in " << dist[x][y][z] << " minute(s)." << "\n";
            return;
        }
        
        for(int i=0; i<6; i++){
            int nx = x + dx[i];
            int ny = y + dy[i];
            int nz = z + dz[i];
            
            if(nx<0 || nx>=l || ny<0 || ny>=r || nz<0 || nz>=c) continue;
            
            if(!chk[nx][ny][nz] && map[nx][ny][nz] != '#'){
                chk[nx][ny][nz] = true;
                dist[nx][ny][nz] = dist[x][y][z] + 1;
                q.push(node(nx,ny,nz));
            }
        }
    }
    cout << "Trapped!" << "\n";
}

int main(int argc, const char * argv[]) {
    // cin,cout 속도향상
    // ios_base::sync_with_stdio(false);
    cin.tie(NULL); cout.tie(NULL);
    
    while(1){
        cin >> l >> r >> c;
        if(l==0 && r==0 && c==0) break;
        
        memset(chk, false, sizeof(chk));
        memset(dist, 0, sizeof(dist));
        memset(map, 0, sizeof(map));
        
        for(int i=0; i<l; i++){
            // 각 층의 정보를 입력
            for(int j=0; j<r; j++){
                for(int k=0; k<c; k++){
                    cin >> map[i][j][k];
                    
                    if(map[i][j][k] == 'S'){
                        s.x = i; s.y = j; s.z = k;
                    }else if(map[i][j][k] == 'E'){
                        e.x = i; e.y = j; e.z = k;
                    }
                }
            }
            getchar();
        }
        bfs();
    }
}