''' class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
'''        

# def containsDuplicate(nums):
#     # Return true if any value appears more thatn 2x in the array
#     # otherwise return false if every element is distinctive

#     # Would be great try to create a hashmap to show what numbers have appeared

#     # Create a hashmap to take down the frequency of the values that are in the array
#     # loop through the array and add to in the values
#     # if the value is more than 2 we can short circuit and return true


#     hashmap = {}

#     for num in nums:
#         if num in hashmap:          # If the element is already in the hashmap, increment its frequency
#             hashmap[num] += 1
#         else:                       # If the element is not in the hashmap, add it with a frequency of 1
#             hashmap[num] = 1 


#     # It iterates over each value in the hashmap.values() and checks if the value is greater than or equal to 2. It produces a sequence of True or False values for each element.
#     return any(value >= 2 for value in hashmap.values()) 


# HashSet solution : o(n) solution --------------------------------------------------
def containsDuplicate(nums) -> bool:
        seen = set()

        for num in nums:
            print(num, ' : num of nums')

            if num in seen:
                print(num in seen, ':num in seen')
                return True
            
            print(seen, ': seen set before seen.add(num)')
            seen.add(num)

            print(seen, ': seen outside')
        return False


# Hashmap solution : o(n) solution --------------------------------------------------
def containsDuplicate(nums) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            # seen[num] = seen.get(num, 0) + 1 - Option if this makes sense
            
            elif num in seen:
                 seen[num] += 1
            else:
                 seen[num] = 1

        return False


# Example usage:
nums = [1,2,3,1]
# nums = [1,2,3,4]
# nums = [1,1,1,3,3,4,3,2,4,2]
result = containsDuplicate(nums)