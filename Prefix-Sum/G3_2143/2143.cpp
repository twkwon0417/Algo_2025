#include <bits/stdc++.h>

using namespace std;

long T, pre_A[1001];
long long ans;
map<long, int> mp_A;
map<long, int> mp_B;

int main() {
    cin >> T;

    int temp;
    cin >> temp;
    for (int i = 1; i <= temp; i++) {
        int tmp_val;
        cin >> tmp_val;
        pre_A[i] = pre_A[i - 1] + tmp_val;
    }
    for(int i = 1; i <= temp; i++) {
        for (int j = i; j <= temp; j++) {
            mp_A[pre_A[j] - pre_A[i - 1]] += 1;
        }
    }

    memset(pre_A, 0, sizeof(pre_A));

    cin >> temp;
    for (int i = 1; i <= temp; i++) {
        int tmp_val;
        cin >> tmp_val;
        pre_A[i] = pre_A[i - 1] + tmp_val;
    }
    for(int i = 1; i <= temp; i++) {
        for (int j = i; j <= temp; j++) {
            mp_B[pre_A[j] - pre_A[i - 1]] += 1;
        }
    }

    for(auto x: mp_A) {
        auto it = mp_B.find(T - x.first);
        if(it != mp_B.end()) {
            ans += (long) mp_B[T - x.first] * (long) x.second;
        }
    }

    cout << ans;
}