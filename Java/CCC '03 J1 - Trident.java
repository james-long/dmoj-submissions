import java.util.Scanner;
 
public class Main{
    public static void main (String[] arg)
 {
  Scanner in = new Scanner(System.in);
  int t = in.nextInt(), s = in.nextInt(), h = in.nextInt();
  in.close();
  String sep = "";
  for(int i = 0; i < s; i++)
   sep += " ";
  for(int i = 0; i < t; i++)
  {
   System.out.println("*" + sep + "*" + sep + "*");
  }
  for(int i = 0; i < s*2+3; i++)
   System.out.print("*");
  System.out.println();
  sep += " ";
  for(int i = 0; i < h; i++)
   System.out.println(sep + "*");
 }
}