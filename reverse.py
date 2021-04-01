class Solution:
    def reverse(self, x: int) -> int:
        conv_num = str(x)
        conv_num = conv_num[::-1]

        if conv_num[-1] == '-':
            conv_num = conv_num.replace('-','')
            conv_num='-'+conv_num
        
        conv_num_int=int(conv_num)
        
        if conv_num_int < -2**31 or conv_num_int > (2**31 - 1):
            return 0
        return conv_num_int

if __name__ == "__main__":
    solution = Solution()
    print(solution.reverse('000'))