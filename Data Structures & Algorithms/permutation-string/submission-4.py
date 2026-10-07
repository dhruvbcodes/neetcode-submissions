class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count = {}
        counter = Counter(s1)
        i = 0
        j = 0

        while j < len(s2):

            if s2[j] not in counter:
                count = {}
                j += 1
                i = j
                continue
                
            if s2[j] in count:
                count[s2[j]] += 1
                if count[s2[j]] > counter[s2[j]]:
                    count[s2[i]] -= 1
                    if count[s2[i]] == 0:
                        count.pop(s2[i])
                    i += 1
                    j += 1
                    continue
            else:
                count[s2[j]] = 1
            
            print(count)
            if counter == count:
                return True
            elif (j - i) > len(s1):
                count[s2[i]] -= 1
                if count[s2[i]] == 0:
                    count.pop(s2[i])
                i += 1
            
            j += 1

        return False


            







        