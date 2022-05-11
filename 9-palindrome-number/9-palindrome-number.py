class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(map(str, str(x)))

        x_reverse_list = list(reversed(x_list))
        
        if x_list == x_reverse_list:
            return True
        else:
            return False