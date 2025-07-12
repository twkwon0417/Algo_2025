#include <bits/stdc++.h>

using namespace std;

long N, ls[5004], a ,b , c;
long tmp = 4e18;

int main() {
    cin >> N;

    for (int i = 0; i < N; i++) {
        cin >> ls[i];
    }
    sort(ls, ls + N);

    for(int i = 0; i < N-2; i++) {
        int L = i + 1;
        int R = N - 1;
        long sum = ls[i] + ls[L] + ls[R];

        while(L != R) {
            if(abs(sum) < tmp) {
                a = i; b = L; c = R;
                tmp = abs(sum);
            }
            if(ls[i] + ls[L] + ls[R] > 0) {
                sum -= ls[R];
                R--;
                sum += ls[R];
            }
            else if(ls[i] + ls[L] + ls[R] < 0) {
                sum -= ls[L];
                L++;
                sum += ls[L];
            }
            else {
                a = i; b = L; c = R;
                break;
            }
        }
    }

    cout << ls[a] <<  " " << ls[b] << " " << ls[c];
}