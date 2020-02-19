import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class day3p1v3 {

    static BufferedReader br;
    static String alpha_regex = "[A-Za-z]";

    public static void main(String args[]) throws IOException {

        // >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> TRY NOT TO DO ARRAY LOGIC <<<<<<<<<<<<<<<<<< <<<<<<<<<<<<<<<<<<

        // TODO: PARSE INSTRUCTIONS FROM TEXT FILE
        br = new BufferedReader(new FileReader("day3p1_line_1"));
        String line_1_raw = br.readLine();
        br = new BufferedReader(new FileReader("day3p1_line_2"));
        String line_2_raw = br.readLine();

        String[] line_1_cords = line_1_raw.split(",");
        String[] line_2_cords = line_2_raw.split(",");

        // TODO: GENERATE ARRAY OF COORDINATES FOR LINE 1 AND 2
        //      - should be int[][] where the sub-array is each coordinate


    }

    public int find_intersection(int[] line_1_cord_1, int[] line_1_cord_2, int[] line_2_cord_1, int[] line_2_cord_2){

        // TODO: FIND INTERSECTION FUNCTION
        //      - returns the distance to the intersection
        //      - takes four int[] as parameters
        //      - returns -1 if there isnt an intersection

        int[] horizontal_line_cord_1;
        int[] horizontal_line_cord_2;
        int[] vertical_line_cord_1;
        int[] vertical_line_cord_2;

        // TODO: find which line is the horizontal line
        if(line_1_cord_1[0] == line_1_cord_2[0]){
            horizontal_line_cord_1 = line_1_cord_1;
            horizontal_line_cord_2 = line_1_cord_2;
            vertical_line_cord_1 = line_2_cord_1;
            vertical_line_cord_2 = line_2_cord_2;
        }
        else{
            horizontal_line_cord_1 = line_2_cord_1;
            horizontal_line_cord_2 = line_2_cord_2;
            vertical_line_cord_1 = line_1_cord_1;
            vertical_line_cord_2 = line_1_cord_2;
        }


        return 1;


    }
}