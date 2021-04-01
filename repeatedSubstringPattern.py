class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        count=0
        pattern_list=[]
        for i in range(len(s)):
            temp_string=s[:i]
            print(temp_string)

            # for j in range(s):
            #     if temp_string == 





        

if __name__ == "__main__":
    solution=Solution()
    print(solution.repeatedSubstringPattern("abab"))