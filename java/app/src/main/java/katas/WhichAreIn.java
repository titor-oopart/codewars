/*
 Implement a function that computes the difference between two lists. The function should remove all occurrences of elements from the first list (a) that are present in the second list (b). The order of elements in the first list should be preserved in the result.

Examples
If a = [1, 2] and b = [1], the result should be [2].

If a = [1, 2, 2, 2, 3] and b = [2], the result should be [1, 3].
 */
package katas;
import java.util.*;

public class WhichAreIn {

    public static String[] inArray(String[] a1, String[] a2) {
        Set<String> result = new TreeSet<>();

        for (String s1 : a1) {
            for (String s2 : a2) {
                if (s2.contains(s1)) {
                    result.add(s1);
                    break;
                }
            }
        }

        return result.toArray(new String[0]);
    }
}

