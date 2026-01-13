package katas;

import java.util.*;

public class ProdFib { // must be public for codewars	
	
	public static long[] productFib(long prod) {
    long a = 0;
    long b = 1;
    while (a*b < prod) {
      long next = a + b;
      a = b;
      b = next;
    }
    return new long[]{a, b, a*b == prod ? 1:0};
   }
}
