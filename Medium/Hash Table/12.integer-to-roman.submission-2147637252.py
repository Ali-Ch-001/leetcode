class Solution:
    def intToRoman(self, num: int) -> str:
        # Precomputed mappings for each decimal place
        thousands = ("", "M", "MM", "MMM")
        hundreds  = ("", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM")
        tens      = ("", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC")
        ones      = ("", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX")

        # Direct O(1) index lookup and C-level string concatenation
        return (
            thousands[num // 1000] +
            hundreds[(num % 1000) // 100] +
            tens[(num % 100) // 10] +
            ones[num % 10]
        )