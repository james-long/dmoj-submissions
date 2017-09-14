import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class LongJ_ArrayListPractice{
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  char[] chars = in.readLine().toCharArray();
        Arrays.sort(chars);
  scramble("", new String(chars));
 }
 public static void scramble(String current, String word)
 {
  if(word.length()>1)
  {
   for(int i = 0; i < word.length(); i++)
   {
    scramble(current + word.charAt(i), word.substring(0, i) + word.substring(i+1, word.length()));
   }
  }
  else
  {
   System.out.println(current + word);
  }
 }
}