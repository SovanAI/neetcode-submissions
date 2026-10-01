class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = s.lower()

        # removing all special charecters and keeping only the alphabetic values
        cleaned_text = "".join(char for char in string if char.isalnum()) 

        # removing all spaces
        cleaned_text = cleaned_text.replace(" ", "") 

        left , right = 0 , len(cleaned_text) - 1
        
        # logic for the program
        while left < right :
            if  cleaned_text[left] != cleaned_text[right] :
                return False
            
            left += 1
            right -= 1
        
        return True