// CSES
#include <bits/stdc++.h>
using namespace std;

typedef long long ll;

int main(void) {
  int n;
  cin >> n;

  ll diff = 0;
  ll multiplier = 0;
  for (int k = 1; k <= n; k++) {
    if (k == 1) {
      printf("0\n");
      continue;
    }
    multiplier += diff;
    ll combinations = (k * k) * ((k * k) - 1) / 2;
    ll bad_combinations = 8 * multiplier;
    diff++;
    ll result = combinations - bad_combinations;

    printf("%lld\n", result);
  }
}
