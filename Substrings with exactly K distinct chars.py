'''
Given a string s and an int k, return an int representing the number of substrings (not unique) of s with exactly k distinct characters. If the given string doesn't have k distinct characters, return 0.
https://leetcode.com/problems/subarrays-with-k-different-integers

Example 1:

Input: s = "pqpqs", k = 2
Output: 7
Explanation: ["pq", "pqp", "pqpq", "qp", "qpq", "pq", "qs"]
Example 2:

Input: s = "aabab", k = 3
Output: 0
Constraints:

The input string consists of only lowercase English letters [a-z]
0 ≤ k ≤ 26
'''

def KDistinct(s, k):
    if not s or k == 0: return 0
    def AtMostK(K):
        hash_map = {}
        count = 0
        i = 0
        for j in range(len(s)):
            if s[j] not in hash_map:
                hash_map[s[j]] = 0
            hash_map[s[j]] += 1
            while len(hash_map) > K:
                hash_map[s[i]] -= 1
                if hash_map[s[i]] == 0:
                    hash_map.pop(s[i])
                i += 1
            count += j - i + 1
        return count
    return AtMostK(k) - AtMostK(k-1)

##test cases
print(KDistinct(s = "pqpqs", k = 2))
print(KDistinct(s = "aabab", k = 3))