import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class day1p2v2 {
    public static void main(String args[]) throws IOException {
        System.out.println(fuel_req(1969));
        BufferedReader br = new BufferedReader(new FileReader("day1p1_input.txt"));

        int total_fuel_req = 0;

        for (String line = br.readLine(); line != null; line = br.readLine()) { // check logic of this line
            int current_module_mass = Integer.parseInt(line);
            total_fuel_req += fuel_req(current_module_mass);
        }

        System.out.println(total_fuel_req);
    }

    public static int fuel_req(int mass) {
        int total_fuel = 0;
        while(mass >= 0){
            mass = mass/3 -2;
            if(mass >= 0){ // why need this line
                total_fuel += mass;
            }
        }
        return total_fuel;
    }
}