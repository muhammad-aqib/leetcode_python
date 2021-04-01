class Solution:
    def myAtoi(self, my_str: str) -> int:
        final_string=""
        striped_string=my_str.strip()
        count=0
        
        for i in striped_string:
            if count == 0:
                if i == '-' or i == '+':
                    final_string+=i
                    continue
                if not i.isdigit():
                    return 0
                count+=1
            try:
                if int(i):
                    final_string+=i
            except:
                pass
            if i == ' ' or i == '.':
                break
            
        int_min=-2147483648
        int_max=2147483647

        if int(final_string) > int_max:
            return int_max
        if int(final_string) < int_min:
            return int_min

        return final_string
            
if __name__ == "__main__":
    solution = Solution()
    print(solution.myAtoi("123123123123123123"))