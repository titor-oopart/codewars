package katas;

public class BinaryAddition {

  public static String binaryAddition(int a, int b){
        int c = a + b;
        String result = "";
        while (c > 0) {
            int mod = c % 2;
            result = mod + result;
            c = c / 2;
        }
        return result;
  }
}
