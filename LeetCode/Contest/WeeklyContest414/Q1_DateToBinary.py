'''

Date to Binary

level=easy



You are given a string date representing a Gregorian calendar date in the yyyy-mm-dd format.

date can be written in its binary representation obtained by converting year, month, and day to their binary representations without any leading zeroes and writing them down in year-month-day format.

Return the binary representation of date.

 

Example 1:

Input: date = "2080-02-29"

Output: "100000100000-10-11101"

Explanation:

100000100000, 10, and 11101 are the binary representations of 2080, 02, and 29 respectively.

Example 2:

Input: date = "1900-01-01"

Output: "11101101100-1-1"

Explanation:

11101101100, 1, and 1 are the binary representations of 1900, 1, and 1 respectively.
'''


class Solution:
    def convertDateToBinary(self, date: str) -> str:
        l=date.split("-")
        res=""
        count=0
        for i in l:
            b=str(bin(int(i)))[2:]
            res+=b
            if count<2:
                res+="-"
                count+=1
        return res