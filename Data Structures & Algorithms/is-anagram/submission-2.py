class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1={}
        t1={}
        if len(s)!=len(t):
            return False
        for i in s:
            if i in s1:
                s1[i]+=1
            else:
                s1[i]=1
        for i in t:
            if i in t1:
                t1[i]+=1
            else:
                t1[i]=1
        for i in s1:
            if i in t1:
                if t1[i]!=s1[i]:
                    return False
            else:
                return False
        return True
          

        