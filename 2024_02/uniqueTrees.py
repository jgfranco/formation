"""
public int numTrees(int n) {
  int [] G = new int[n+1];
  G[0] = G[1] = 1;
    
  for(int i=2; i<=n; ++i) {
    for(int j=1; j<=i; ++j) {
      G[i] += G[j-1] * G[i-j];
    }
  }
  return G[n];
}
"""

def numTrees(n):
  dp= [0] * (n+1)
  dp[0] = 1
  dp[1] = 1

  for i in range (2, n+1):
    for j in range(1, i+1):
      dp[i] += dp[j-1] * dp[i-j]
  
  return dp[n]