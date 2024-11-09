class Solution:
    def findComplement(self, num: int) -> int:
        def binary_to_decimal(binary_str):
            decimal_number = 0
            length=len(binary_str)
            for i in range(length):
                digit = int(binary_str[i])
                # Calculate the power of 2 based on the position 
                power = length - i - 1
                decimal_number += digit * (2 ** power)
            
            return decimal_number
        
        # to convert number into binary values
        x=bin(num)[2:]
        res=""

        # taking complement of each bit
        for i in str(x):
            if i=="0":
                res+="1"
            else:
                res+="0"
        #using our function 
        return binary_to_decimal(res)
    
        # using in built integer datatype with base parameter
        return int(res,2)
                