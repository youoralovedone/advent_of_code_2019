import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;


public class day3p1 {

    static BufferedReader br;
    static String char_regex = "[A-Za-z]";

    /*
        - instead of using two loops use one loop
        - make the loop an int[][]
        - iterate through every
    */

    public static void main(String args[]) throws IOException {

        // sum all of the coordinates in one direction
        br = new BufferedReader(new FileReader("day3p1_line_1"));
        String line_1_raw = br.readLine();
        br = new BufferedReader(new FileReader("day3p1_line_2"));
        String line_2_raw = br.readLine();

        String[] line_1_cords_input = line_1_raw.split(",");
        String[] line_2_cords_input = line_2_raw.split(",");


        int horizontal_cord = 0;
        int vertical_cord = 0;
        int[][] line_1_cords = new int[300][300];



        // NESTED LOOP, ITERATE THROUGH EACH LINE IN LINE 1 PER SEGMENT IN LINE 2
        // check if x or y is between use || statement

        // POINTS NOT DEFINITE VALUES BUT RANGES!!!!!!!!!!

        for(int i = 0; i < line_1_cords.length; i++){
            String current_instruction = line_1_cords_input[i];
            int current_instruction_without_direction = Integer.parseInt(current_instruction.replaceAll(char_regex, ""));

            switch (current_instruction.charAt(0)){

                case 'U' : vertical_cord += current_instruction_without_direction;
                case 'D' : vertical_cord -= current_instruction_without_direction;
                case 'R' : horizontal_cord += current_instruction_without_direction;
                case 'L' : horizontal_cord -= current_instruction_without_direction;

            }
            line_1_cords[i][0] = horizontal_cord;
            line_1_cords[i][1] = vertical_cord;

        }
        // reset these vars
        // set old vars maybe? nahhhh this can be fixed in the loop later
        horizontal_cord = 0;
        vertical_cord = 0;
        int[][] line_2_cords = new int[300][300];

        for(int i = 0; i < line_2_cords.length; i++){
            String current_instruction = line_2_cords_input[i];
            int current_instruction_without_direction = Integer.parseInt(current_instruction.replaceAll(char_regex, ""));

            switch (current_instruction.charAt(0)){

                case 'U' : vertical_cord += current_instruction_without_direction;
                case 'D' : vertical_cord -= current_instruction_without_direction;
                case 'R' : horizontal_cord += current_instruction_without_direction;
                case 'L' : horizontal_cord -= current_instruction_without_direction;

            }
            line_2_cords[i][0] = horizontal_cord;
            line_2_cords[i][1] = vertical_cord;

        }
        // iter through all of cords and use find_intersection to find intersections
        /*

        int[][] intersections = new int[300][300]; // 300 max number of intersections, when iterating just while until null
        for(int i = 0; i < line_1_cords.length; i++){
            for(int j = 0; j < line_2_cords.length; j++){
                int[] line_1_cords_current = line_1_cords[i];
                int[] line_2_cords_current = line_2_cords[j];

                line_1_cords_current = sort(line_1_cords_current);
                line_2_cords_current = sort(line_2_cords_current);

                // write sort function that sorts tuple by size and use it on these

                boolean line_2_x_tween = line_2_cords_current[0] < line_1_cords_current[1] && line_2_cords_current[0] > line_1_cords_current[0];
                boolean line_2_y_tween =

                if( ){

                }
            }
        }
        */
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

    public static int[] find_intersection(int[][] first_line, int[][] second_line){

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

        // check if x cord of horizontal is line is between the limits of y cord

        /*
        for(int i = horizontal_line[0][0]; i < horizontal_line[1][0]; i++){ // horizontal lines first cord's x to horizontal lines second cord's x
            for(int j = vertical_line[0][1]; j < vertical_line[1][1]; j++){
                if() // if y ever cordinates match
            }
        }
         */
        // JUST CHECK X CORD AT Y, JUST CHECK THE X CORD AT THE Y




        return new int[]{1};
    }
}
