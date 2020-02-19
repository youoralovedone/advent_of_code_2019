import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class day1p1v2 {
    public static void main(String args[]) throws IOException {

        int total_fuel = 0;
        BufferedReader br = new BufferedReader(new FileReader("day1p1_input.txt"));

        for (String line = br.readLine(); line != null; line = br.readLine()) { // check logic of this line
            // per module
            int current_mass = Integer.parseInt(line); // mass of current module
            // int current_fuel_req = fuel_req(current_mass);

            // total_fuel += current_fuel_req;
            current_mass = (current_mass/3) - 2;
            // sum += fuel_req(current);
            total_fuel += current_mass;
        }
        System.out.println(total_fuel);
    }
}
