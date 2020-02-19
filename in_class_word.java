public class in_class_word {
    public static double add(double[] data){
        double sum = 0;
        for (double value:data) {
            sum += value;
        }
        return sum;
    }
    public static double add_postion(double[] data){
        double sum = 0;
        for(int i = 0; i < data.length; i++){
            sum += data[i];
        }
        return sum;
    }
}