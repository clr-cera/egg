#include <bits/stdc++.h>

using namespace std;

void mysort(string &s, int init, int end) {}

int main(void) {
  int t;
  cin >> t;

  for (int i = 0; i < t; i++) {
    string s;
    cin >> s;
    mysort(s, 0, s.size() - 1);
  }
}
