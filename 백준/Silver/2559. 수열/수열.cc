#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    ios::sync_with_stdio(false);  
    cin.tie(nullptr);  

    int N, K;
    cin >> N >> K;

    vector<int> temperatures(N);
    vector<int> prefix_sum(N + 1, 0);

    for (int i = 0; i < N; i++) {
        cin >> temperatures[i];
    }

    for (int i = 1; i <= N; i++) {
        prefix_sum[i] = prefix_sum[i - 1] + temperatures[i - 1];
    }

    int answer = prefix_sum[K];
    for (int i = K; i <= N; i++) {
        answer = max(answer, prefix_sum[i] - prefix_sum[i - K]);
    }

    cout << answer << '\n';

    return 0;
}