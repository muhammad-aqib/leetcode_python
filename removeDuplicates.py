class Solution(object):
    def removeDuplicates(self, nums):
        check_del=False
        run=0
        
        while run < len(nums):
            if check_del==True:
                run=run-1
        
            if run+1 < len(nums):
                if nums[run] == nums[run+1]:
                    nums.pop(run+1)
                    check_del=True
                else:
                    check_del=False

            run=run+1
        
        return len(nums)

        # while run < len(nums):
        #     if check_del==True:
        #         run=run-1
        #     try:
        #         if nums[run] == nums[run+1]:
        #             del nums[run+1]
        #             check_del=True
        #         else:
        #             check_del=False
        #     except:
        #         pass

        #     run=run+1
        
        # return len(nums)
                


        # for i in range(len(nums)):
        #     try:
        #         while nums[i] == nums[i+1]:
        #             del nums[i+1]
        #     except:
        #         pass
        # return len(nums)


if __name__ == "__main__":
    nums = [1,1,2]
    print(len(nums))
    solution = Solution()
    print(solution.removeDuplicates(nums))