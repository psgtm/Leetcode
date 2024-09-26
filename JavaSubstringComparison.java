import java.io.*;
import java.util.*;

public class Solution {

    public static String getSmallestAndLargest(String s, int k) {
        String smallest = s.substring(0, k);
        String largest = s.substring(0, k);
        
        // Iterate over all substrings of length k
        for (int i = 1; i <= s.length() - k; i++) {
            String substring = s.substring(i, i + k);
            
            // Compare lexicographically to find smallest and largest
            if (substring.compareTo(smallest) < 0) {
                smallest = substring;
            }
            if (substring.compareTo(largest) > 0) {
                largest = substring;
            }
        }
        
        return smallest + "\n" + largest;
    }

    public static void main(String[] args) {
        // Scanner to read input from STDIN
        Scanner sc = new Scanner(System.in);
        String s = sc.next();
        int k = sc.nextInt();
        
        // Call the function and print the result
        System.out.println(getSmallestAndLargest(s, k));
    }
}