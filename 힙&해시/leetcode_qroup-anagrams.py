class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        output = []
        sorted_arr = ["".join(sorted(i)) for i in strs]
        str_sets = set(sorted_arr)
        
        for i in str_sets:
            target_arr = []
            for index, sorted_str in enumerate(sorted_arr):
                if sorted_arr[index] == i:
                    target_arr.append(strs[index])
                    
            output.append(target_arr)
            
        return output
            