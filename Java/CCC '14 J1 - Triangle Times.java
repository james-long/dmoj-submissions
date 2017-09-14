import java.io.BufferedReader;
import java.io.InputStreamReader;

public class DMOJ {
 
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int a = Integer.parseInt(in.readLine()), b = Integer.parseInt(in.readLine()), c = Integer.parseInt(in.readLine());
  if(a+b+c==180)
  {
   if(a==b && b==c) System.out.print("Equilateral");
   else if (a==b || b==c || a==c) System.out.print("Isosceles");
   else System.out.print("Scalene");
  }
  else System.out.print("Error");
 }
}