import java.util.Scanner;
import java.util.stream.StreamSupport;

public class day5p1v3 {

    static Scanner input = new Scanner(System.in);
    static int[] computer = {3,225,1,225,6,6,1100,1,238,225,104,0,1101,86,8,225,1101,82,69,225,101,36,65,224,1001,224,-106,224,4,224,1002,223,8,223,1001,224,5,224,1,223,224,223,102,52,148,224,101,-1144,224,224,4,224,1002,223,8,223,101,1,224,224,1,224,223,223,1102,70,45,225,1002,143,48,224,1001,224,-1344,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1101,69,75,225,1001,18,85,224,1001,224,-154,224,4,224,102,8,223,223,101,2,224,224,1,224,223,223,1101,15,59,225,1102,67,42,224,101,-2814,224,224,4,224,1002,223,8,223,101,3,224,224,1,223,224,223,1101,28,63,225,1101,45,22,225,1101,90,16,225,2,152,92,224,1001,224,-1200,224,4,224,102,8,223,223,101,7,224,224,1,223,224,223,1101,45,28,224,1001,224,-73,224,4,224,1002,223,8,223,101,7,224,224,1,224,223,223,1,14,118,224,101,-67,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,7,677,677,224,102,2,223,223,1005,224,329,1001,223,1,223,1008,226,226,224,1002,223,2,223,1005,224,344,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,359,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,374,101,1,223,223,1108,677,226,224,102,2,223,223,1005,224,389,1001,223,1,223,1007,677,677,224,1002,223,2,223,1005,224,404,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,419,101,1,223,223,1108,226,677,224,102,2,223,223,1006,224,434,1001,223,1,223,8,677,226,224,1002,223,2,223,1005,224,449,101,1,223,223,1008,677,677,224,1002,223,2,223,1006,224,464,1001,223,1,223,1108,226,226,224,1002,223,2,223,1005,224,479,1001,223,1,223,1007,226,677,224,102,2,223,223,1005,224,494,1001,223,1,223,1007,226,226,224,102,2,223,223,1005,224,509,101,1,223,223,107,677,226,224,1002,223,2,223,1006,224,524,1001,223,1,223,108,677,677,224,102,2,223,223,1006,224,539,101,1,223,223,7,677,226,224,102,2,223,223,1006,224,554,1001,223,1,223,1107,226,677,224,102,2,223,223,1005,224,569,101,1,223,223,108,677,226,224,1002,223,2,223,1006,224,584,101,1,223,223,108,226,226,224,102,2,223,223,1006,224,599,1001,223,1,223,1107,226,226,224,102,2,223,223,1006,224,614,1001,223,1,223,8,226,677,224,102,2,223,223,1006,224,629,1001,223,1,223,107,226,226,224,102,2,223,223,1005,224,644,101,1,223,223,8,226,226,224,102,2,223,223,1006,224,659,101,1,223,223,7,226,677,224,102,2,223,223,1005,224,674,101,1,223,223,4,223,99,226};
    // static int[] computer = {3,0,4,0,99};
    // static int[] computer = {1002,4,3,4,33};
    // static int[] computer = {1002,4,3,4,33};
    public static void main(String args[]){
        // System.out.println(computer.length);
        calculate();
        for(int value: computer){
            System.out.print(value + ", ");
        }
    }

    public static void calculate(){

        for(int i = 0; i < computer.length - 2; i = i){ // computer.length - 2
            int opcode_raw = computer[i];
            System.out.println(opcode_raw);
            // System.out.println("got here");

            if(opcode_raw != 99 && opcode_raw != 3 && opcode_raw != 4){
                String opcode_as_string = Integer.toString(opcode_raw);
                // f(opcode_as_string.length() == 4){ opcode_as_string = "0" + opcode_as_string; }
                // System.out.println(opcode_as_string); // fuckkkk IT HAS TO CHECK FOR THE 3 or 4

                // System.out.println(computer[i + 1]);
                System.out.println(opcode_as_string);
                int opcode_parsed = opcode_as_string.length() < 3 ? Integer.parseInt(opcode_as_string) : Integer.parseInt(opcode_as_string.substring(opcode_as_string.length() - 2)); // PROBLEM

                int first_parameter_value = (opcode_as_string.charAt(0) == '1') ? computer[i + 2] : computer[computer[i + 2]]; // cant compare ints with chars
                int second_parameter_value = (opcode_as_string.charAt(1) == '1') ? computer[i + 1] : computer[computer[i + 1]];
                // System.out.println(opcode_as_string.charAt(0) == '1');

                // first node is always going to be position based

                int third_parameter_value = computer[i + 3];
                // get rid of switch to limit overhead??
                switch (opcode_parsed){
                    case 1: {
                        computer[third_parameter_value] = first_parameter_value + second_parameter_value;
                        i += 4; // can move to end
                    }
                    case 2: {
//                        System.out.println(first_parameter_value);
//                        System.out.println(computer[i+2]);
//                        System.out.println(second_parameter_value); // 10 so 0 means it should be taking 3 literally

                        // System.out.println(third_parameter_value);
                        computer[third_parameter_value] = first_parameter_value * second_parameter_value;
                        i += 4;
                    }
                }
            }

            /*
            // >>> OPCODE FORMAT <<<
            // A(omitted) B C D E
                A(0): mode of 3rd parameter (always 0)
                B(1): mode of 2nd parameter
                C(2): mode of 1st parameter
                D(3): two digit OPCODE
                E(4): ^
            */

            else{
                int first_parameter_value = computer[i + 1];

                // ystem.out.println(first_parameter_value);
                // System.out.println(opcode_raw);
                if(opcode_raw == 4){
                    System.out.println("output: " + computer[first_parameter_value]);
                    i += 3;
                }
                else if(opcode_raw == 3){
                    System.out.print("input: ");
                    computer[first_parameter_value] = input.nextInt();
                    i += 3;
                }
//                else if(opcode_raw == 1){
//                    computer[computer[i + 3]] = computer[computer[i + 1]] + computer[computer[i + 2]];
//                    i += 4;
//                }
//                else if(opcode_raw == 2){
//                    computer[computer[i + 3]] = computer[computer[i + 1]] * computer[computer[i + 2]];
//                    i += 4;
//                }
                else if(opcode_raw == 99){
                    System.out.println("program terminated");
                    break;
                }
            }
        }
    }
}