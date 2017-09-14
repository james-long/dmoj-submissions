import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

public class DMOJ {
 
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int a = Integer.parseInt(in.readLine()), b = 0, total = 0;
  Stack<Integer> nums = new Stack<Integer>();
  for(;a > 0; a--)
  {
   b = Integer.parseInt(in.readLine());
   if(b!=0) nums.push(b);
   else nums.pop();
  }
  while(!nums.empty())
   total+=nums.pop();
  System.out.print(total);
 }
}