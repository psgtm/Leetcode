import java.util.Scanner;

public class Solution {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("================================");
        
        // Loop for 3 lines of input
        for (int i = 0; i < 3; i++) {
            String s = scanner.next();  // Read string
            int x = scanner.nextInt();  // Read integer
            
            // Output with formatting: %-15s pads string to 15 chars, %03d ensures integer is 3 digits
            System.out.printf("%-15s%03d%n", s, x);
        }
        
        System.out.println("================================");
        
        scanner.close();
    }
}
