public class IsPrime {
    public static boolean IsPrime(int num){
        if (num <= 1){
            return false;
        }
        else{
            int count = 2;
            while (count != num){
                if (num % count == 0){
                    return false;
                }
                count++;
            }
            return true;
        }
    }
}
