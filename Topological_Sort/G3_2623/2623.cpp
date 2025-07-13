#include <bits/stdc++.h>

using namespace std;

vector<int> v[1004];
int visited[1004], flag;
vector<int> stk;

int dfs(int x) {
    visited[x] = 1;
    for(int nx : v[x]) {
        if(visited[nx] == 1) {
            auto  tmp = find(stk.begin(), stk.end(), nx);
            if(tmp == stk.end()) {
                return -1;
            }
        }
        else {
            stk.push_back(dfs(nx));
        }
    }
    return x;
}

int main(){
    int N, M;
    cin >> N >> M;

    while(M--) {
        int iter, prev;
        cin >> iter;
        cin >> prev;
        while (--iter) {
            int cur;
            cin >> cur;
            if(find(v[prev].begin(), v[prev].end(), cur) == v[prev].end()) {
                v[prev].push_back(cur);
            }
            prev = cur;
        }
    }

    for(int i = 1; i <= N; i++)  {
        if(visited[i] == 0) {
            stk.push_back(dfs(i));
        }
    }

    reverse(stk.begin(), stk.end());
    for(int x : stk) {
        if(x == -1) {
            cout << 0;
            flag = -1;
        }
    }
    if(flag != -1) {
        for(int x : stk) {
            cout << x << "\n";
        }
    }
}