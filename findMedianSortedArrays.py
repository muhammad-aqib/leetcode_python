def findMedianSortedArrays(nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

        merged_list = sorted(nums1 + nums2)
        length_merged_list = len(merged_list)

        median_element=(length_merged_list+1)/2

        if str(median_element).endswith(".0"):
            median_element=int(median_element)

        if isinstance(median_element,float):
            sum_element=0
            str_median_element=str(median_element).split(".")
            sum_element=(merged_list[int(str_median_element[0])-1]+merged_list[int(str_median_element[0])])/2
            return sum_element

        if isinstance(median_element, int):
            return float(merged_list[median_element-1])

if __name__ == "__main__":
    nums1 = [1, 3]
    nums2 = [2]

    print(findMedianSortedArrays(nums1,nums2))