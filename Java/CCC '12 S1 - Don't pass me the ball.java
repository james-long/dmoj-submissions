import java.io.*;

public class DMOJ {
 
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int a = Integer.parseInt(in.readLine()), add = 1, fin = 0;
  for(int i = a-3; i > 0; i--)
  {
   fin+=i*add;
   add++;
  }
  System.out.println(fin);
 }
}