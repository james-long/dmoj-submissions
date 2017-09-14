import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
 static void generate(int n, int k, String current)
 {
  int oneCount = 0;
  for(int i = 0; i < current.length(); i++)
   if(current.charAt(i) == '1') oneCount++;
  if(current.length() == n)
  {
   if(oneCount == k)
    System.out.println(current);
   return;
  }
  if(oneCount < k)
   generate(n, k, current + "1");
  generate(n, k, current + "0");
 }
  
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int tot = Integer.parseInt(in.readLine()), all, one;
  String[] temp;
  for(;tot>0;tot--)
  {
   temp = in.readLine().split(" ");
   all = Integer.parseInt(temp[0]);
   one = Integer.parseInt(temp[1]);
   System.out.println("The bit patterns are");
   generate(all, one, "");
   System.out.println();
  }
 }
}