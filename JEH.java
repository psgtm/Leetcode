import java.io.*;
import java.util.*;

class MyCalculator {
    public long power(int n, int p) throws Exception {
        if (n == 0 && p == 0) {
            throw new Exception("n and p should not be zero.");
        }
        if (n < 0 || p < 0) {
            throw new Exception("n or p should not be negative.");
        }
        
        return (long) Math.pow(n, p); // Casting result to long
    }
}

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        MyCalculator myCalculator = new MyCalculator();

        while (scanner.hasNextInt()) {
            int n = scanner.nextInt();
            int p = scanner.nextInt();
            
            try {
                System.out.println(myCalculator.power(n, p));
            } catch (Exception e) {
                System.out.println(e);
            }
        }
        
        scanner.close();
    }
}
