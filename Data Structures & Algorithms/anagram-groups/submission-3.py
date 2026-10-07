class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        master = defaultdict(list)

        for i in strs:
            temp = list(i)
            temp.sort() 
            tot = str(temp)           
            if tot in master:
                master[tot].append(i)
            else:
                master[tot] = [i]
        
        res = []
        for i in master.values():
            i.sort()
            res.append(i)
        
        return res

        