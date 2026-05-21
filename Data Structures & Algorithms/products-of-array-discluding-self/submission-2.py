class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # output = [0]*len(nums)
        # prefix = 1
        # for i in range(0,len(nums)):
        #     output[i] = prefix
        #     prefix *= nums[i]

        # postfix = 1
        # for i in range(len(nums)-1,-1,-1):
        #     output[i] *= postfix
        #     postfix *= nums[i]
        # return output


# ========================================================
        # n=len(nums)
        # left_product = [0]*n
        # right_product = [0]*n
        # result = [0]*n
        # left_product[0] = 1
        # for i in range(1,n):
        #     left_product[i] = left_product[i-1] * nums[i-1]
        # right_product[n-1] = 1
        # for i in range(n-2,-1,-1):
        #     right_product[i] = right_product[i+1]*nums[i+1]

        # for i in range(0,n):
        #     result[i] = left_product[i] * right_product[i]
        
        # return result
# ===========================================================
        n=len(nums)
        result = [0]*n
        result[0] = 1
        for i in range(1,n):
            result[i] = result[i-1] * nums[i-1]

        R = 1
        for i in range(n-1, -1, -1):
            result[i] *= R
            R*=nums[i]

        return result