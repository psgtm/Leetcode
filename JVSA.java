import java.io.*;
import java.util.*;

class Add {
    public void add(int... numbers) {
        int sum = 0;
        StringBuilder output = new StringBuilder();
        
        for (int i = 0; i < numbers.length; i++) {
            sum += numbers[i];
            output.append(numbers[i]);
            
            if (i < numbers.length - 1) {
                output.append("+");
            }
        }
        
        output.append("=").append(sum);
        System.out.println(output);
    }
}

public class Solution {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        // Read 6 integers from input
        int[] inputs = new int[6];
        for (int i = 0; i < 6; i++) {
            inputs[i] = scanner.nextInt();
        }

        // Create an instance of Add
        Add adder = new Add();

        // Call add method with increasing number of arguments
        adder.add(inputs[0], inputs[1]);
        adder.add(inputs[0], inputs[1], inputs[2]);
        adder.add(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4]);
        adder.add(inputs[0], inputs[1], inputs[2], inputs[3], inputs[4], inputs[5]);

        scanner.close();
    }
}
