import java.util.Scanner;
import java.util.stream.StreamSupport;

public class day5p1v2 {

    static Scanner input = new Scanner(System.in);
    static int[] computer = {3,225,1,225,6,6,1100,1,238,225,104,0,1101,86,8,225,1101,82,69,225,101,36,65,224,1001,224,-106,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,102,52,148,224,101,-1144,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1102,70,45,225,1002,143,48,224,1001,224,-1344,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1101,69,75,225,1001,18,85,224,1001,224,-154,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,15,59,225,1102,67,42,224,101,-2814,224,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,1101,28,63,225,1101,45,22,225,1101,90,16,225,2,152,92,224,1001,224,-1200,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1101,45,28,224,1001,224,-73,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1,14,118,224,101,-67,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,677,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,344,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,359,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,374,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,404,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,419,101,1,223,223,1108,226,677,224,102,2,223,223,1006,224,434,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,449,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,226,226,224,1002,223,2,223,1005,224,479,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,494,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,509,101,1,223,223,107,677,226,224,1002,223,2,223,1006,224,524,1001,223,1,223,108,677,677,224,102,2,223,223,1006,224,539,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,569,101,1,223,223,108,677,226,224,1002,223,2,223,1006,224,584,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,599,1001,223,1,223,1107,226,226,224,102,2,223,223,1006,224,614,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,629,1001,223,1,223,107,226,226,224,102,2,223,223,1005,224,644,101,1,223,223,8,226,226,224,102,2,223,223,1006,224,659,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226};
    // static int[] computer = {3,0,4,0,99};
    // static int[] computer = {1002,4,3,4,33};
    public static void main(String args[]){
        calculate();
    }

    public static void calculate(){
        for(int i = 0; i < computer.length - 3; i = i){ // computer.length - 3? doesnt really matter
            int opcode_raw = computer[i];
            String opcode_as_string = Integer.toString(opcode_raw);
            if(opcode_as_string.length() == 4){ opcode_as_string = "0" + opcode_as_string; }

//            int index_first_parameter = i + 1;
//            int index_second_parameter = i + 2;
//            int index_third_parameter = i + 3;

            System.out.println(opcode_as_string); // fuckkkk IT HAS TO CHECK FOR THE 3 or 4
            //use ternary operator
            int first_parameter_value = opcode_as_string.charAt(0) == 1 ? opcode_as_string.charAt(0) : computer[i + 1];
            int second_parameter_value = opcode_as_string.charAt(1) == 1 ? opcode_as_string.charAt(1) : computer[i + 2];
            // int third_parameter_value = opcode_as_string.charAt(2) == 1 ? opcode_as_string.charAt(2) : computer[opcode_as_string.charAt(2)];;
            int third_parameter_value = computer[i + 2];

            /*
            // >>> OPCODE FORMAT <<<
            // A B C D E
                A(0): mode of 3rd parameter
                B(1): mode of 2nd parameter
                C(2): mode of 1st parameter
                D(3): two digit OPCODE
                E(4): ^
            */

            int opcode_parsed = Integer.parseInt(opcode_as_string.substring(3)); // 5 - 2, gets last two chars of string

//            switch (opcode_parsed){
//                case 1: computer[computer[index_third_parameter]] = computer[computer[index_first_parameter]] + computer[computer[index_second_parameter]]; i += 4;
//                case 2: computer[computer[index_third_parameter]] = computer[computer[index_first_parameter]] * computer[computer[index_second_parameter]]; i += 4;
//                case 3: {
//                    System.out.print("input: ");
//                    computer[index_first_parameter] = input.nextInt();
//                    i += 2;
//                }
//                case 4: System.out.println("output: " + computer[index_first_parameter]); i += 2;
//            }

            switch (opcode_parsed){
                case 1: computer[third_parameter_value] = first_parameter_value + second_parameter_value;i += 4; // either first parameter value or computer[first parameter value]
                case 2: computer[third_parameter_value] = first_parameter_value * second_parameter_value; i += 4;
                case 3: {
                    System.out.print("input: ");
                    first_parameter_value = input.nextInt();
                    i += 2;
                }
                case 4: System.out.println("output: " + first_parameter_value); i += 2;
            }

        }
    }
}