class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        test_dict = {}
        for i in s:
            if i not in test_dict:
                test_dict[i] = 1
            else:
                test_dict[i] += 1
        
        for j in t:
            if j not in test_dict:
                return False
            else:
                test_dict[j] -= 1
                if test_dict[j] < 0:
                    return False
        
        for key, value in test_dict.items():
            if value > 0:
                return False
        
        return True
        