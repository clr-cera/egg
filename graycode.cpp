#include <bits/stdc++.h>
using namespace std;

void generateGrayCode(int n, vector<int> &code, int actual) {
  if (actual == n) {
    for (int i = 0; i < n; i++) {
      cout << code[i];
    }
    cout << endl;
    return;
  }

  else {
    generateGrayCode(n, code, actual + 1);
    code[actual] = !code[actual];
    generateGrayCode(n, code, actual + 1);
  }
}

int main(void) {
  int n;
  cin >> n;

  vector<int> code(n);
  generateGrayCode(n, code, 0);
}
