import java.util.*;

public class DMOJ {
 public static void main (String[] arg) throws Exception
 { 
  int tot, a, b;
  Scanner in = new Scanner(System.in);
  tot = in.nextInt();
  for(int i = 1; i <= tot; i++)
  {
   a = in.nextInt();
   b = in.nextInt();
   System.out.println(a+b);
  }
 }
}