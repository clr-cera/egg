// Exercise 2123C Codeforces
#include <bits/stdc++.h>
#include <tuple>

using namespace std;

tuple<vector<int>, vector<int>> getminmax(const vector<int> &vec) {
  vector<int> minvec(vec.size());
  vector<int> maxvec(vec.size());

  minvec[0] = vec[0];
  maxvec[vec.size() - 1] = vec[vec.size() - 1];

  for (int i = 1; i < vec.size(); i++) {
    if (vec[i] < minvec[i - 1]) {
      minvec[i] = vec[i];
    } else {
      minvec[i] = minvec[i - 1];
    }
  }
  for (int i = vec.size() - 2; i >= 0; i--) {
    if (vec[i] > maxvec[i + 1]) {
      maxvec[i] = vec[i];
    } else {
      maxvec[i] = maxvec[i + 1];
    }
  }
  return make_tuple(minvec, maxvec);
}

int main(void) {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {
    int n;
    cin >> n;
    vector<int> vec(n);
    for (int j = 0; j < n; j++) {
      cin >> vec[j];
    }

    auto [min_vec, maxvec] = getminmax(vec);

    cout << true;

    for (int j = 1; j < n - 1; j++) {
      if (vec[j] < min_vec[j - 1]) {
        cout << true;
      } else if (vec[j] > maxvec[j + 1]) {
        cout << true;
      } else {
        cout << false;
      }
    }

    if (n > 1) {
      cout << true;
    }
    cout << '\n';
  }
}
