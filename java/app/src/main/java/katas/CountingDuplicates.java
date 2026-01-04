
/*
Count the number of Duplicates
Write a function that will return the count of distinct case-insensitive alphabetic characters and numeric digits that occur more than once in the input string. The input string can be assumed to contain only alphabets (both uppercase and lowercase) and numeric digits.

Example
"abcde" -> 0 # no characters repeats more than once
"aabbcde" -> 2 # 'a' and 'b'
"aabBcde" -> 2 # 'a' occurs twice and 'b' twice (`b` and `B`)
"indivisibility" -> 1 # 'i' occurs six times
"Indivisibilities" -> 2 # 'i' occurs seven times and 's' occurs twice
"aA11" -> 2 # 'a' and '1'
"ABBA" -> 2 # 'A' and 'B' each occur twice
 */

package katas;

public class CountingDuplicates {

    public static int duplicateCount(String text) {
        String str = text.toLowerCase();
        int countDuplicate = 0;
        int originalSize = str.length();
        while (str.length() > 1){
          char firstChar = str.charAt(0);
          str = str.replace(String.valueOf(firstChar), "");
          int newSize = str.length();
          if ((originalSize - newSize) > 1) {
            countDuplicate = countDuplicate + 1;
          }
          originalSize = newSize;
        }
        return countDuplicate;
    }
}

