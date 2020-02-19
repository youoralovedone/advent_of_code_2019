public class day1p2 {
    public static void main(String args[]){
        System.out.println(total_fuel_req(100756));
        System.out.println(total_fuel_req(14));
        System.out.println(total_fuel_req(1969));
        System.out.println(total_fuel_req(15));
    }
    public static int total_fuel_req(int mass){
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
