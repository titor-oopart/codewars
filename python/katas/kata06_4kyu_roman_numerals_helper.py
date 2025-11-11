"""
Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be tested for each function.

Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping any digit with a value of zero. In Roman numerals:

1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC
2008 is written as 2000=MM, 8=VIII; or MMVIII
1666 uses each Roman symbol in descending order: MDCLXVI.
Input range : 1 <= n < 4000

In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").

Examples
to roman:
2000 -> "MM"
1666 -> "MDCLXVI"
  86 -> "LXXXVI"
   1 -> "I"

from roman:
"MM"      -> 2000
"MDCLXVI" -> 1666
"LXXXVI"  ->   86
"I"       ->    1
Help
+--------+-------+
| Symbol | Value |
+--------+-------+
|    M   |  1000 |
|   CM   |   900 |
|    D   |   500 |
|   CD   |   400 |
|    C   |   100 |
|   XC   |    90 |
|    L   |    50 |
|   XL   |    40 |
|    X   |    10 |
|   IX   |     9 |
|    V   |     5 |
|   IV   |     4 |
|    I   |     1 |
+--------+-------+
"""


class RomanNumerals:
    roman_values = [
        ("M", 1000),
        ("CM", 900),
        ("D", 500),
        ("CD", 400),
        ("C", 100),
        ("XC", 90),
        ("L", 50),
        ("XL", 40),
        ("X", 10),
        ("IX", 9),
        ("V", 5),
        ("IV", 4),
        ("I", 1),
    ]

    @staticmethod
    def to_roman(val: int) -> str:
        solution = ""
        i = 0
        while val > 0:
            num = RomanNumerals.roman_values[i][1]
            letter = RomanNumerals.roman_values[i][0]
            roman = letter * int(val / num) if val % num > -1 else ""
            solution = solution + roman
            i = i + 1
            val = val - (num * int(val / num))

        return solution

    @staticmethod
    def from_roman(roman_num: str) -> int:
        solution = []
        for letter, item in RomanNumerals.roman_values:
            if roman_num.startswith(letter):
                new_roman_num = roman_num.lstrip(letter)
                index_end = len(roman_num) - len(new_roman_num)
                num_tripped = roman_num[0:index_end]
                number = num_tripped.count(letter)
                roman_num = new_roman_num
                solution.append(item * number)
        return sum(solution)
