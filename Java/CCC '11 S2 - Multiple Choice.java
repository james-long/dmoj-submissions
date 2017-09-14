import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Main {
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int tot = Integer.parseInt(in.readLine()), right = 0;
  char[] ans = new char[tot];
  for(int i = 0; i < tot; i++)
  {
   ans[i] = in.readLine().charAt(0);
  }
  for(int i = 0; i < tot; i++)
  {
   if(in.readLine().charAt(0) == ans[i])
    right++;
  }
  System.out.println(right);
 }
}