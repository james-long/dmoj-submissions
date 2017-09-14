import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
 static boolean bananas(String word)
 {
  if(word.length()<=1) 
  {
   if(word.equals("A"))
    return true;
   return false;
  }
  if(word.charAt(0) == 'B' && word.charAt(word.length()-1) == 'S')
   if(bananas(word.substring(1, word.length()-1)))
    return bananas(word.substring(1, word.length()-1));
  for(int i = 0; i < word.length(); i++)
   if(word.charAt(i) == 'N')
    if(bananas(word.substring(0, i)) && bananas(word.substring(i+1, word.length())))
     return(bananas(word.substring(0, i)) && bananas(word.substring(i+1, word.length())));
  return false;
 }
  
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  String word;
  boolean yn;
  do{
   word = in.readLine();
   if(!word.equals("X"))
   {
    yn = bananas(word);
    System.out.println(yn?"YES":"NO");
   }
  }while(!word.equals("X"));
 }
}