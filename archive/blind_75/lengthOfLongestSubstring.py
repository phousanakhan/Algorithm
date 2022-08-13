class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        intuition --> sliding window
        
        increment end if letter in unique
        else --> increment start
        return longest window length
        
        input => pwwkew
        
        state of dict:
        {} ()pwwkew
        {'p': 1} (p)wwkew
        {'p': 1, 'w': 1} p(w)wkew
        {'w': 1} w(w)kew *remove p
        {} (w)kew *remove w, as w is still in dict^
        {'w': 1} (w)kew, add w back as w is now not in dict^
        {'w': 1, 'k': 1}, w(k)ew
        {'w': 1, 'k': 1, 'e': 1}, wk(e)w
        {'k': 1, 'e': 1},  ke(w) *remove w
        {'k': 1, 'e': 1, 'w': 1}, ke(w)
        '''
        
        start = 0
        end = 0
        longest = 0
        hashSet = {}
        
        while end < len(s):
            if s[end] not in hashSet: #unique char
                hashSet[s[end]] = 1 #add to hashSet
                longest = max(longest, len(hashSet))
                end += 1
            else:
                del hashSet[s[start]]
                start += 1
        return longest
