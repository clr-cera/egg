// 2111C - Equal Values
#include <bits/stdc++.h>

using namespace std;

long long mincost(vector<long long> &v, long long n) {
  long long mincost = LONG_LONG_MAX;
  for (int i = 0; i < n;) {
    int j = i;
    for (; j < n && v[i] == v[j]; j++)
      ;
    mincost = min(mincost, (i + n - j) * v[i]);
    i = j;
  }
  return mincost;
}

int main(void) {
  long long t;
  cin >> t;
  for (int i = 0; i < t; i++) {
    long long n;
    cin >> n;
    vector<long long> v(n);

    for (int j = 0; j < n; j++) {
      cin >> v[j];
    }

    cout << mincost(v, n) << '\n';
  }
}
