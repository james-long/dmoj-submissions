import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class DMOJ {
 
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int rad, tot = 0;
  do{
   rad = Integer.parseInt(in.readLine());
   if(rad > 0)
   {
    for(int i = 0; i <= rad; i++)
    {
     tot+=Math.sqrt(rad*rad-i*i);
    }
    System.out.println(tot*4+1);
    tot = 0;
   }
  }while(rad > 0);
 }
}