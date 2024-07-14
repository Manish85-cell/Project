#include <bits/stdc++.h>
  using namespace std;

  int main() {

    int n;
    cin>>n;
    vector<vector<int>> edges(n, vector<int>(2));

    unordered_map<int, list<int>> adj;
    for(int i = 0; i<n-1; i++){
      int src;
      int dest;
      cin>>src>>dest;
      
      adj[src].push_back(dest);
      adj[dest].push_back(src);
    }
    int m;
    cin>>m;
    
    cout << adj[m].size();
    
    return 0;

  }