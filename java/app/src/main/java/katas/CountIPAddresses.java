package katas;

public class CountIPAddresses {

  public static long ipToNumber(String ip) {

    String[] parts = ip.split("\\.");
    long[] numbers = new long[parts.length];

    for (int i = 0; i < parts.length; i++) {
        numbers[i] = Long.parseLong(parts[i]);
    }

    long[] numbersStart = new long[4];

    numbersStart[0] = numbers[0] * 16777216L;
    numbersStart[1] = numbers[1] * 65536L;
    numbersStart[2] = numbers[2] * 256L;
    numbersStart[3] = numbers[3];

    long sum = 0;

    for (int i = 0; i < numbersStart.length; i++) {
        sum += numbersStart[i];
    }

    return sum;
  }

  public static long ipsBetween(String start, String end) {

    long startNumber = ipToNumber(start);
    long endNumber = ipToNumber(end);

    long result = Math.abs(endNumber - startNumber);

    return result;
  }
}
