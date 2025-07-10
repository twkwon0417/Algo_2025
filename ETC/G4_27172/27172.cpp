#include <bits/stdc++.h>

using namespace std;

int N;
int ls[100004];
int exist[1000004];
int ans[100004];

int main() {
    cin.tie(NULL);
    cout.tie(NULL);
    ios::sync_with_stdio(false);
    memset(exist, -1, sizeof(exist));
    cin >> N;
    for(int i = 0; i < N; i++) {
        int temp;
        cin >> temp;
        ls[i] = temp;
        exist[temp] = i;
    }

    for(int i = 0; i < N; i++) {
        for (int j = ls[i] * 2; j <= 1000000; j += ls[i]) {
            if (exist[j] != -1) {
                ans[i] += 1;
                ans[exist[j]] -= 1;
            }
        }
    }

    for(int i = 0; i < N; i++) {
        cout << ans[i] << " ";
    }
}