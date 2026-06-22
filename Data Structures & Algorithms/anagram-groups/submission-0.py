class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        test_groups = {}
        
        for string in strs:
            count = [0] * 26
            for c in string:
                count[ord(c) - ord('a')] += 1
            count = str(count)

            if count in test_groups:
                test_groups[count].append(string)
            else:
                test_groups[count] = [string]
        
        ret_list = []
        for stored_list in test_groups.values():
            print(stored_list)
            ret_list.append(stored_list)

        return ret_list