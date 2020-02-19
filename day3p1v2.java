import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class day3p1v2 {

    static BufferedReader br;
    static String char_regex = "[A-Za-z]";

    /*
        - use two [x,y] as cords for points
        - rewrite all of this shit
        - fix all of this logic during study hall
    */

    public static void main(String args[]) throws IOException {

        // instruction parsing, all of this shit is instruction parsing
        br = new BufferedReader(new FileReader("day3p1_line_1"));
        String line_1_raw = br.readLine();
        br = new BufferedReader(new FileReader("day3p1_line_2"));
        String line_2_raw = br.readLine();

        String[] line_1_cords_input = line_1_raw.split(",");
        String[] line_2_cords_input = line_2_raw.split(",");

        int horizontal_cord_line_1 = 0;
        int vertical_cord_line_1 = 0;
        int horizontal_cord_line_2 = 0;
        int vertical_cord_line_2 = 0;

        int[][] line_1_cords = new int[300][300];
        int[][] line_2_cords = new int[300][300];

        for(int i = 0; i < line_1_cords.length; i++){
            String current_instruction = line_1_cords_input[i];
            int current_instruction_without_direction = Integer.parseInt(current_instruction.replaceAll(char_regex, ""));

            switch (current_instruction.charAt(0)){

                case 'U' : vertical_cord_line_1 += current_instruction_without_direction;
                case 'D' : vertical_cord_line_1 -= current_instruction_without_direction;
                case 'R' : horizontal_cord_line_1 += current_instruction_without_direction;
                case 'L' : horizontal_cord_line_1 -= current_instruction_without_direction;

            }
            line_1_cords[i][0] = horizontal_cord_line_1;
            line_1_cords[i][1] = vertical_cord_line_1;

            current_instruction = line_2_cords_input[i];
            current_instruction_without_direction = Integer.parseInt(current_instruction.replaceAll(char_regex, ""));

            switch (current_instruction.charAt(0)){

                case 'U' : vertical_cord_line_2 += current_instruction_without_direction;
                case 'D' : vertical_cord_line_2 -= current_instruction_without_direction;
                case 'R' : horizontal_cord_line_2 += current_instruction_without_direction;
                case 'L' : horizontal_cord_line_2 -= current_instruction_without_direction;

            }
            line_2_cords[i][0] = horizontal_cord_line_2;
            line_2_cords[i][1] = vertical_cord_line_2;

        }
    }

    public static int[] sort(int[] input_array){
        // sorts smaller cord and larger cord
        if(input_array[1] < input_array[0]){
            int temp = input_array[0];
            input_array[0] = input_array[1];
            input_array[1] = temp;
        }
        return input_array;
    }

    public static int find_distance_to_nearest_intersection(int[][] first_line, int[][] second_line){

        int sum = 100000000; // some crazy number

        // next few lines sort lines into horizontal and vertical
        int[][] horizontal_line;
        int[][] vertical_line;

        if(first_line[0][0] == first_line[1][0]){
            horizontal_line = first_line;
            vertical_line = second_line;
        }
        else{
            horizontal_line = second_line;
            vertical_line = first_line;
        }

        sort(horizontal_line[0]);
        sort(horizontal_line[1]); // <-- not req
        sort(vertical_line[0]);
        sort(vertical_line[1]);

        int horizontal_x_cord = horizontal_line[0][1];

        if(horizontal_x_cord >= vertical_line[0][0] && horizontal_x_cord <= vertical_line[0][1]){ // logic is wrong
            sum = horizontal_x_cord + vertical_line[0][1];
        }

        return sum;
    }
}
