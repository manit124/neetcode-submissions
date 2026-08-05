class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        word1={}
        word2={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in word1:
                word1[i]+=1
            else:
                word1[i]=1
        for j in t:
            if j in word2:
                word2[j]+=1
            else:
                word2[j]=1
        for k in word1:
            if k in word2 and word1[k]==word2[k]:
                continue
            else:
                return False
        return True

        