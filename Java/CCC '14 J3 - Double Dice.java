import java.io.BufferedReader;
import java.io.InputStreamReader;

public class DMOJ {
 
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int tot = Integer.parseInt(in.readLine()), a=100, b=100, aR, bR;
  for(;tot>0;tot--)
  {
   String[] inAr = in.readLine().split(" ");
   aR = Integer.parseInt(inAr[0]);
   bR = Integer.parseInt(inAr[1]);
   if(aR>bR) b-=aR;
   else if (bR>aR) a-=bR;
  }
  System.out.print(a+"\n"+b);
 }
}