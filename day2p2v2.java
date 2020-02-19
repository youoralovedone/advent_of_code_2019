public class day2p2v2 {

    static int upper_bound = 99;
    static int[] computer;
    public static void main(String args[]){
        // iter through all verbs and nouns in a nested for loop
        for(int noun = 0; noun <= upper_bound; noun++){
            for(int verb = 0; verb <= upper_bound; verb++){
                // check address 0
                // System.out.println(compute(noun,verb));

                if(compute(noun,verb) == 19690720){
                    System.out.println(noun*100 + verb);
                }
            }
        }

    }

    public static void calculate(int operation_index){
        int index_first = operation_index + 1;
        int index_second = operation_index + 2;
        int index_output = operation_index + 3;
        int operation = computer[operation_index];

        if(operation == 1){
            computer[computer[index_output]] = computer[computer[index_first]] + computer[computer[index_second]];
        }
        else if(operation == 2){
            computer[computer[index_output]] = computer[computer[index_first]] * computer[computer[index_second]];
        }
    }
    public static int compute(int noun, int verb){
        computer = new int[]{1,noun,verb,3,1,1,2,3,1,3,4,3,1,5,0,3,2,13,1,19,1,10,19,23,1,23,9,27,1,5,27,31,2,31,13,35,1,35,5,39,1,39,5,43,2,13,43,47,2,47,10,51,1,51,6,55,2,55,9,59,1,59,5,63,1,63,13,67,2,67,6,71,1,71,5,75,1,75,5,79,1,79,9,83,1,10,83,87,1,87,10,91,1,91,9,95,1,10,95,99,1,10,99,103,2,103,10,107,1,107,9,111,2,6,111,115,1,5,115,119,2,119,13,123,1,6,123,127,2,9,127,131,1,131,5,135,1,135,13,139,1,139,10,143,1,2,143,147,1,147,10,0,99,2,0,14,0};
        for(int i = 0; i < computer.length; i+=4){
            calculate(i);
        }
        return computer[0];
    }
}
