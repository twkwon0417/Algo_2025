#include <bits/stdc++.h>

using namespace std;

vector<int> adj[1004];
int ls[1004];
long long visited[1004];

long long dfs(int x) {
    if(visited[x] != -1) {
        return visited[x];
    }
    if(adj[x].empty()) {
        visited[x] = ls[x];
        return ls[x];
    }

    long long ret = 0;
    for(int nx : adj[x]) {
        ret = max(ret, ls[x] + dfs(nx));
    }

    return visited[x] = ret;
}

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);

    int N;
    cin >> N;

    while(N--) {
        int a, b;

        cin >> a >> b;

        for (int i = 0; i < 1004; i++) {
            adj[i].clear();
        }
        memset(visited, -1, sizeof(visited));
        memset(ls, 0, sizeof(ls));

        for(int i = 1; i <= a; i++) {
            cin >> ls[i];
        }
        for (int i = 1; i <= b; i++) {
            int x, y;
            cin >> x >> y;
            adj[y].push_back(x);
        }
        int k;
        cin >> k;
        cout << dfs(k) << "\n";
    }

}
