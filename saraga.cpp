#include <bits/stdc++.h>
#include <climits>

using namespace std;

int main(void) {
  string s, t;
  cin >> s;
  cin >> t;
  map<char, int> m;

  for (int i = t.size() - 2; i >= 0; i--) {
    if (m.find(t[i]) == m.end()) {
      m[t[i]] = t.size() - i;
    }
  }

  string cool;

  int minsize = INT_MAX;
  int idx = -1;
  for (int i = 1; i < s.size(); i++) {
    if (m.find(s[i]) != m.end()) {
      int cost = i + 1 + m[s[i]];
      if (cost < minsize) {
        minsize = cost;
        idx = i;
      }
    }
  }

  if (idx == -1) {
    cout << -1;
    return 0;
  }

  for (int i = 0; i <= idx; i++) {
    cool += s[i];
  }
  for (int i = t.size() - m[s[idx]] + 1; i < t.size(); i++) {
    cool += t[i];
  }

  cout << cool;
}
