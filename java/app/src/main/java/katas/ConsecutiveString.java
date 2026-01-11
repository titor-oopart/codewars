package katas;


public class ConsecutiveString {

    public static String longestConsec(String[] strarr, int k) {
        int n = strarr.length;
        if (n == 0 || k > n || k <= 0) return "";

        String longest = "";
        for (int i = 0; i <= n - k; i++) {
            StringBuilder sb = new StringBuilder();
            for (int j = 0; j < k; j++) {
                sb.append(strarr[i + j]);
            }
            String candidate = sb.toString();
            if (candidate.length() > longest.length()) {
                longest = candidate;
            }
        }
        return longest;
    }
}
