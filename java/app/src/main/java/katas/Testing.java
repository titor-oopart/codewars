package katas;

import java.util.*;

public class Testing {
    public static List<String> number(List<String> lines) {
        List<String> result = new ArrayList<>();
        for (int i = 0; i < lines.size(); i++) {
          result.add(String.format("%s: %s", i + 1, lines.get(i)));
        }
        return result;
    }
}
