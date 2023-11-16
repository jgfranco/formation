'''
Given a numeric array, return the length of longest increasing subsequence.
E.g.:
[1, 5, 2, 7] => 3 (1,5,7) or (1,2,7)
[1, 10, 9, 2, 3, 4, 5]
[7,5,6,8,2, 1,2,3,4,5,6,7,8] => 8

2^N
globalMax
currentMax = 4
[1, 2, 2, 3, 3, 1, 4] DP
[1, 5, 2, 7, 3, 0, 4]
 i
 j
[1, 5, 2, 7, 3, 0, 4, 8, 9, 10]
 0. 1. 2. 3. 4. 5. 6. 7. 8. 9 (idx)
    0. 0. 1. 2. -1 4. 3. 7. 8
    j
        i

'''

'''
int longSubsequence(int[] arr) {
    int[] dp = new int[arr.length];
    Arrays.fill(arr, 1);
    int globalMax = 0;
    int globalMaxIdx = -1;
    for(int i = 1; i < arr.length; i++) {
        int currentMax = 1;
        for(int j = 0; j < i; j++) {
            if (arr[j] < arr[i]) {
                currentMax = Math.max(currentMax, dp[j] + 1);
            }
        }
        dp[i] = currentMax;
        globalMax = if (dp[i] > globalMax) {
            globalMax = dp[i];
            globalMaxIdx = i;
        }
    }
    List<Integer> maxSubPath = new ArrayList<>();
    int i = dp[globalMaxIdx];
    int lengthOfSubseq = dp[globalMaxIdx];
    maxSubPath.insert(0, dp[globalMaxIdx]);
    while (lengthOfSubseq < maxSubPath.size()) {
        int j = i - 1;
        while(dp[j] != dp[i] - 1 || arr[j] >= arr[i] && j > 0) j--;
        maxSubPath.insert(0, dp[j]);
        i = j;
    }
    return maxSubPath;
}
'''


def longSubsequence(arr):
    dp = [1] * len(arr) 
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[j]< arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    #print(dp)
    max_idx = dp.index(max(dp))
    result = []
    result.append(arr[max_idx])
    for i in range(max_idx -1, -1, -1):
        if dp[i] < dp[max_idx] and arr[i] < arr[max_idx]:
            result.append(arr[i])
            max_idx = i
    print(arr)
    print(dp)
    return result[::-1] # max(dp)


"""print(longSubsequence([1, 5, 2, 7]), "expect 3")

print(longSubsequence([7,5,6,8,2,1,2,3,4,5,6,7,8]), "expect 8")"""

print(longSubsequence([-3, -2, -1]), "expect 3")
