// 1915F - Greetings
#include <bits/stdc++.h>

using namespace std;

void merge_sort() {}

void solve() {
  int n;
  cin >> n;

  vector<pair<int, int>> people(n);

  for (int i = 0; i < n; i++) {
    int start, end;
    cin >> start;
    cin >> end;

    people[i] = {start, end};
  }

  sort(people.begin(), people.end());

  int sum = 0;

  for (int i = 0; i < n; i++) {
    int end = people[i].second;

    for (int j = i + 1; j < n; j++) {
      if (people[j].second <= end) {
        sum++;
      }
    }
  }
  cout << sum << endl;
}

int main(void) {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {
    solve();
  }
}
