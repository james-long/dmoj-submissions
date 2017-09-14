import java.io.BufferedReader;
import java.io.InputStreamReader;

public class DMOJ {
 
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int tot = Integer.parseInt(in.readLine()), cA = 0, cB = 0;
  String b = in.readLine();
  for(int i = 0; i < b.length(); i++)
  {
   if(b.charAt(i) == 'A') cA++;
   else cB++;
  }
  if(cA == cB) System.out.print("Tie");
  else System.out.print((cA>cB)?'A':'B');
 }
}