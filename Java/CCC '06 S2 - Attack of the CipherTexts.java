import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class DMOJ {
 
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  char[] key = new char[27];
  Arrays.fill(key, '.');
  String plain = in.readLine(), cypher = in.readLine(), code = in.readLine();
  for(int i = 0; i < plain.length(); i++)
  {
   if(cypher.charAt(i) != ' ') key[(int)cypher.charAt(i)-65] = plain.charAt(i);
   else key[26] = plain.charAt(i);
  }
  for(int i = 0; i < code.length(); i++)
  {
   if(code.charAt(i) != ' ') System.out.print(key[(int)code.charAt(i)-65]);
   else System.out.print(key[26]);
  }
 }
}