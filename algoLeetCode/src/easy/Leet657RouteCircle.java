package easy;

/**
 * Created by Gavia on 2018/3/31.
 */
public class Leet657RouteCircle {
    public boolean judgeCircle(String moves) {
        int x = 0;
        int y = 0;
        for(char letter : moves.toCharArray()){
            if(letter == 'U'){
                y++;
            }
            else if (letter == 'D'){
                y--;
            }
            else if (letter == 'L'){
                x--;
            }else if (letter == 'R'){
                x++;
            }
        }
        if (x==0 && y==0){
            return true;
        }

        return false;
    }

    public static void main(String[] args) {
         Leet657RouteCircle solution = new Leet657RouteCircle();

         String moves = "LRRL";
        System.out.println(solution.judgeCircle(moves));
    }
}
