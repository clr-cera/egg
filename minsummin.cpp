// 2124B - Minimise Sum
#include <bits/stdc++.h>

using namespace std;

long long minsumin(vector<long long> v, int n) {
  if (v[0] == 0) {
    return 0;
  }

  if (v[1] == 0) {
    return v[0];
  }

  if (v[0] > v[1]) {
    return v[0] + v[1];
  } else {
    return v[0] * 2;
  }
}

int main(void) {
  int t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    int n;
    cin >> n;
    vector<long long> v(n);
    for (int j = 0; j < n; j++) {
      cin >> v[j];
    }

    cout << minsumin(v, n) << '\n';
  }
}
