import java.io.*;
import java.math.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(System.in));
        
        // Read the input number as a string
        String n = bufferedReader.readLine();
        
        // Close the bufferedReader
        bufferedReader.close();
        
        // Convert the input string to a BigInteger
        BigInteger number = new BigInteger(n);
        
        // Use isProbablePrime with a certainty of 1 (guaranteed primality)
        if (number.isProbablePrime(1)) {
            System.out.println("prime");
        } else {
            System.out.println("not prime");
        }
    }
}
