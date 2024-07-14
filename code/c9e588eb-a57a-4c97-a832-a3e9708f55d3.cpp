#include <iostream>
#include <vector>

using namespace std;

void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
{
    int i = 0, j = 0, k = 0;
    vector<int> c(m + n);
    while (i < m && j < n)
    {
        if (nums1[i] < nums2[j])
        {
            c[k] = nums1[i];

            i++;
        }
        else
        {
            c[k] = nums2[j];

            j++;
        }
        k++;
    }
    while (i < m || j < n)
    {
        if (i < m)
        {
            c[k] = nums1[i];
            i++;
        }
        else
        {
            c[k] = nums2[j];
            j++;
        }
        k++;
    }
    for (int i = 0; i < m + n; i++)
    {
        nums1[i] = c[i];
    }
}

int main()
{

    int n, m;
    cin >> n >> m;

    vector<int> nums1(n + m, 0);
    vector<int> nums2(m);
    for (int i = 0; i < n + m; i++)
    {
        cin >> nums1[i];
    }

    for (int i = 0; i < m; i++)
    {
        cin >> nums2[i];
    }

    merge(nums1, n, nums2, m);
    if(n+m == 1)cout<<num1[0];
    for (int i = 0; i < n + m; i++)
    {
        cout << nums1[i] << ",";
    }
  
}