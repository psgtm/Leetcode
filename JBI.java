import java.io.*;
import java.util.*;
import java.math.*;

public class Solution {

    public static void main(String[] args) {
        // Create a Scanner object to read input from STDIN
        Scanner scanner = new Scanner(System.in);
        
        // Read two large integers as strings
        String num1 = scanner.nextLine();
        String num2 = scanner.nextLine();
        
        // Close the scanner
        scanner.close();
        
        // Convert the input strings to BigInteger objects
        BigInteger bigInt1 = new BigInteger(num1);
        BigInteger bigInt2 = new BigInteger(num2);
        
        // Calculate the sum of the two BigIntegers
        BigInteger sum = bigInt1.add(bigInt2);
        
        // Calculate the product of the two BigIntegers
        BigInteger product = bigInt1.multiply(bigInt2);
        
        // Print the sum
        System.out.println(sum);
        
        // Print the product
        System.out.println(product);
    }
}
