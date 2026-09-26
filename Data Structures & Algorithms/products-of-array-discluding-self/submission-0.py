class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        zero_flag = False
        double_zero_flag = False

        for num in nums:
            if num == 0:
                if zero_flag == True:
                    double_zero_flag = True
                    break
                zero_flag = True
                continue

            product *= num
            
        if double_zero_flag:
            return [0] * len(nums)

        res = []
        for num in nums:
            if zero_flag and num != 0:
                res.append(0)
            elif zero_flag and num == 0:
                res.append(product)
            else: # no zero
                res.append(int(product / num))

        return res