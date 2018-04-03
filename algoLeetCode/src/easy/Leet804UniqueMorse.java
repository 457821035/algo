package easy;

import java.util.HashSet;
import java.util.Set;

/**
 * Created by Gavia on 2018/3/31.
 *
 *
 * Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter. For example,
 * "cab" can be written as "-.-.-....-", (which is the concatenation "-.-." + "-..." + ".-"). We'll call such a concatenation,
 * the transformation of a word.
 * Return the number of different transformations among all words we have.
 */
public class Leet804UniqueMorse {

    public int uniqueMorseRepresentations(String[] words) {
        String[] morseCodeArgs = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};

        Set<String> translateSet = new HashSet<String>();
        for(String word : words){
            char[] chars = word.toCharArray();
            String translate = "";
            for(char singleChar : chars){
                int index = (int)singleChar - 97;
                translate = translate + morseCodeArgs[index];
            }
            translateSet.add(translate);
        }

        return translateSet.size();
    }

    public static void main(String[] args) {
        Leet804UniqueMorse solution = new Leet804UniqueMorse();
        String[] test = {"gin", "zen", "gig", "msg"};
        System.out.println(solution.uniqueMorseRepresentations(test));
    }
}
