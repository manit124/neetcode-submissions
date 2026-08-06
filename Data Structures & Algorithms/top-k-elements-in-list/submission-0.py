class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        j={}
        for i in nums:
            if i in j:
                j[i]+=1
            else:
                j[i]=1
        vals=sorted(list(j.values()))
        L=vals[-k:]
        r=list(j.keys())
        result=[]
        for i in r:
            if(j[i] in L):
                result.append(i)
        return result


        
        

        