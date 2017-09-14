import java.io.*;

public class DMOJ {
 
 static int gcf(int num, int den)
 {
  if(num == 0) return 0;
  if(den%num == 0) return num;
  for(int i = num/2; i > 1; i--)
   if(num%i == 0 && den%i == 0) return i;
  return 1;
 }
 
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int n = Integer.parseInt(in.readLine());
  int d = Integer.parseInt(in.readLine());
  if(n > d || n==0) 
  {
   System.out.print(n/d + " ");
   n%=d;
  }
  int gcf = gcf(n, d);
  if(gcf > 0)
   System.out.format("%d/%d", n/gcf, d/gcf);
 }
}