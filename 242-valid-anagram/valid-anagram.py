class Solution(object):
    def isAnagram(self, s, t):
        

        if len(s)!=len(t):
            return False
        freq={}

        for ch in s:
            if ch in freq:
                freq[ch]+=1
            else:
                freq[ch]=1
        
        freq1={}

        for ch in t:
            if ch in freq1:
                freq1[ch]+=1
            else:
                freq1[ch]=1
        
        return freq==freq1
