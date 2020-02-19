import java.awt.desktop.SystemSleepEvent;
import java.io.*;

public class day1p1 {
    public static void main(String args[]) throws IOException {

        int total_fuel = 0;
        BufferedReader br = new BufferedReader(new FileReader("day1p1_input.txt"));

        for (String line = br.readLine(); line != null; line = br.readLine()) { // check logic of this line
            // per module
            int current_mass = Integer.parseInt(line); // mass of current module
            int current_fuel_req = fuel_req(current_mass);

            total_fuel += current_fuel_req;
            // current = (current/3) - 2;
            // sum += fuel_req(current);
            // sum += current;
        }
        System.out.println(total_fuel);
        // System.out.println(fuel_req(1969));
        // System.out.println(fuel_req(100756));
    }
    public static int fuel_req(int mass){
        int fuel;
        if(mass % 2 == 0){
            fuel = 2; // WHY DOES IT START WITH 2 WHY WHAT
        }
        else{
            fuel = 1; // WHY DOES IT START WITH 2 WHY WHAT
        }
        for(int m = mass; m >= 0; m = m){
            m = (m/3) - 2;
            fuel += m;
        }
        return fuel;

    }
}
