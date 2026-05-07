class Solution:
    def fingerprint(self, s:str) -> tuple:
        myList = [0]*26
        for ch in s:
            index = ord(ch)-ord('a')
            myList[index] += 1
        myTuple = tuple(myList)
        return myTuple
        
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        myDict = defaultdict(list)
        for s in strs:
            key = self.fingerprint(s)
            myDict[key].append(s)
        return list(myDict.values())
        
        
    