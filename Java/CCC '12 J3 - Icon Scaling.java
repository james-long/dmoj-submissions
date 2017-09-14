import java.util.Scanner;

public class Main{
    public static void main (String[] arg)
 {
  Scanner in = new Scanner(System.in);
  int k = in.nextInt();
  in.close();
  
  String kx = "", kstar = "", kspace = "";
  for(int i = 0; i < k; i++)
  {
   kx += "x";
   kstar += "*";
   kspace += " ";
  }
  for(int i = 0; i < k; i++)
   System.out.println(kstar + kx + kstar);
  for(int i = 0; i < k; i++)
   System.out.println(kspace + kx + kx);
  for(int i = 0; i < k; i++)
   System.out.println(kstar + kspace + kstar);
 }
}