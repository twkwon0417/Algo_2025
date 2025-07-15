#include <bits/stdc++.h>

using namespace std;

int T, cnt;
vector<int> v[100004];
int visited[100004];

int dfs(int x) {
    visited[x] = 1;
    for(int nx : v[x]) {
        if(visited[nx] == 0) {
            int ret = dfs(nx);

            if(ret != -1 && ret != nx) {
                visited[nx] = 2;
                cnt++;
                return ret;
            }
            return -1;
        }
        else if(visited[nx] == 1) {
            visited[nx] = 2;
            cnt++;
            return nx;
        }
    }
    return -1;
}
int main() {
    cin >> T;

    while (T--) {
        cnt = 0;
        memset(visited, 0, sizeof(visited));
        for (int i = 0; i < 100004; i++) {
            v[i].clear();
        }
        int N;
        cin >> N;

        for (int i = 1; i <= N; i++) {
            int temp;
            cin >> temp;
            v[i].push_back(temp);
        }

        for (int i = 1; i <= N; i++) {
            if(visited[i] == 0) {
                dfs(i);
                cout << "\n visited";
                for (int j = 1; j <= N; j++) {
                    cout << visited[j];
                }
            }
            cout << "\n cnt" << cnt << " ";
        }
        cout << "\nans: " << cnt;
    }
}