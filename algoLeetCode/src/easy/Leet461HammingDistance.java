package easy;

/**
 * Created by Gavia on 2018/3/31.
 */
public class Leet461HammingDistance {

    public int hammingDistance(int x, int y) {
        Integer binaryX = x;
        Integer binaryY = y;
        int result = 0;

        Integer compResult = binaryX ^ binaryY;
        String binaryResult = Integer.toBinaryString(compResult);

        for (char letter : binaryResult.toCharArray()){
            if(letter=='1'){
                result++;
            }
        }

        return result;
    }

    public static void main(String[] args) {
        Leet461HammingDistance solution = new Leet461HammingDistance();
        System.out.println(solution.hammingDistance(4, 1));
    }
}
