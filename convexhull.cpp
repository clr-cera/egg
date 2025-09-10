#include <algorithm>
#include <bits/stdc++.h>

using namespace std;

typedef long long ll;

int main(void) {
  ll n;
  cin >> n;

  vector<pair<ll, ll>> polls(n);
  for (ll i = 0; i < n; i++) {
    ll x, y;
    cin >> x >> y;
    polls[i] = {x, y};
  }

  sort(polls.begin(), polls.end());

  if (n <= 2) {
    cout << n << endl;
    for (auto p : polls) {
      cout << p.first << " " << p.second << endl;
    }
    return 0;
  }

  vector<pair<ll, ll>> upper;
  vector<pair<ll, ll>> lower;

  for (auto p : polls) {
    while (lower.size() >= 2) {
      auto q = lower[lower.size() - 1];
      auto r = lower[lower.size() - 2];
      if ((q.first - r.first) * (p.second - r.second) -
              (q.second - r.second) * (p.first - r.first) >=
          0) {
        break;
      }
      lower.pop_back();
    }
    lower.push_back(p);
  }

  reverse(polls.begin(), polls.end());

  for (auto p : polls) {
    while (upper.size() >= 2) {
      auto q = upper[upper.size() - 1];
      auto r = upper[upper.size() - 2];
      if ((q.first - r.first) * (p.second - r.second) -
              (q.second - r.second) * (p.first - r.first) >=
          0) {
        break;
      }
      upper.pop_back();
    }
    upper.push_back(p);
  }

  lower.pop_back();
  upper.pop_back();

  // cout << "Lower" << endl;
  // for (auto p : lower) {
  //   cout << p.first << " " << p.second << endl;
  // }
  // cout << "Upper" << endl;
  // for (auto p : upper) {
  //   cout << p.first << " " << p.second << endl;
  // }
  //
  cout << lower.size() + upper.size() << endl;

  for (auto p : lower) {
    cout << p.first << " " << p.second << endl;
  }
  for (auto p : upper) {
    cout << p.first << " " << p.second << endl;
  }
}
