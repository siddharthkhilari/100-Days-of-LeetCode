class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        freq={}
        string=""
        

        for ch in magazine :
            if ch in freq :
                freq[ch] += 1
            else:
                freq[ch]=1

        for ch in ransomNote:
            if ch in freq:
                if freq[ch]==0:
                    return False
                else:
                    string+=(ch)
                    freq[ch]-=1
            else:
                return False

        if string==ransomNote:
            return True