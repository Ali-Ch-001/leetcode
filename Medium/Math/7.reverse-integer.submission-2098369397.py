class Solution:
    def reverse(self, x: int) -> int:
        INT_MAX = 2147483647  # 2^31 - 1
        INT_MIN = -2147483648 # -2^31
        
        # Max value divided by 10
        MAX_LIMIT = INT_MAX // 10 
        
        result = 0
        
        # Handle negative sign for Python's modulo behavior
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        while x != 0:
            digit = x % 10
            x //= 10
            
            # Check for potential overflow before updating result
            if result > MAX_LIMIT or (result == MAX_LIMIT and digit > 7):
                return 0
                
            result = result * 10 + digit
            
        return sign * result