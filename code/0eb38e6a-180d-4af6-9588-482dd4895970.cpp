#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;

    vector<long long> arr(n);
    for (int i = 0; i < n; i++) {
        cin >> arr[i];
    }

    long long target;
    cin >> target;

    int left = 0, right = n - 1;

    while (left < right) {
        long long sum = arr[left] + arr[right];

        if (sum == target) {
            cout << left << " " << right << endl;
            return 0;
        }
        else if (sum < target) {
            left++;
        }
        else {
            right--;
        }
    }

    return 0;
}