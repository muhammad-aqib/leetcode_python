class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
            
        if len(needle) > len(haystack):
            return -1

        if len(needle) == 0:
            return 0
        temp=""
        
        needle_len=len(needle)

        for i in range(len(haystack)):
            counter=0
            index=i
            
            while(counter < needle_len):
                if index < len(haystack):
                    temp=temp+haystack[index]
                    index=index+1
                    counter=counter+1
                else:
                    break
            if temp == needle:
                return i
            temp=""
    
        return -1



if __name__ == "__main__":
    solution = Solution()
    print(solution.strStr("hello","ll"))