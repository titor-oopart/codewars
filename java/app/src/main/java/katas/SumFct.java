package katas;

import java.math.BigInteger;

public class SumFct {

	public static BigInteger perimeter(BigInteger n) {
    BigInteger faces = BigInteger.valueOf(4);
    BigInteger a = BigInteger.valueOf(0);
    BigInteger b = BigInteger.valueOf(1);
    BigInteger sum = BigInteger.valueOf(1);
    BigInteger iterator = BigInteger.valueOf(0); 
    while (iterator.compareTo(n) < 0) {
      BigInteger next = a.add(b);
      a = b;
      b = next;
      sum = sum.add(b);
      iterator = iterator.add(BigInteger.ONE);
    }
    return sum.multiply(faces);
	}
}
