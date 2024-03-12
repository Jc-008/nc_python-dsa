def isPalindrome(s) -> bool:
    # Return true if it is a plaindrome, otherwise false
    # This can use a two pointer strategy
    
    # convert all uppercase letters to lowercase
    # remove all spaces
    # Using 2 pointers, traverse the string making sure each pointer is pointing to the same letter, if not return false
   
   
   lower_cased = s.lower()
   print(lower_cased)

   noSpacingWords = lower_cased.replace(" ", "").replace(",", "").replace(":", "")
   print(len(noSpacingWords), "length")
   left, right = 0, len(noSpacingWords ) - 1
#    or 
#    noSpacingWords = ''.join(char for char in lower_cased if char.isalnum())
   print(noSpacingWords, 'nospacing')

   while left < right:
      leftLetter = noSpacingWords[left]
      rightLetter = noSpacingWords[right]
      print(left, leftLetter)
      print(right, rightLetter)


      if leftLetter == rightLetter:
         left += 1
         right -= 1
      else: 
        return False 
   
   return True
    


# Example usage:
s = "A man, a plan, a canal: Panama"
# s = "race a car"
# s = " "
result = isPalindrome(s)