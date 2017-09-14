import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class DMOJ {
 
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int tot = Integer.parseInt(in.readLine());
  int [][] boxSizes = new int[tot][3];
  int [] nowBox = new int[3];
  long[] vols = new long[tot];
  long minvol = 8000000001L;
  String[] temp;
  for(int i = 0; i < tot; i++)
  {
   temp = in.readLine().split(" ");
   for(int j = 0; j < 3; j++) boxSizes[i][j] = Integer.parseInt(temp[j]);
   Arrays.sort(boxSizes[i]);
   vols[i] = boxSizes[i][0]*boxSizes[i][1]*boxSizes[i][2];
  }
  int tot2 = Integer.parseInt(in.readLine());
  for(int k = 0; k < tot2; k++)
  {
   temp = in.readLine().split(" ");
   for(int j = 0; j < 3; j++) nowBox[j] = Integer.parseInt(temp[j]);
   Arrays.sort(nowBox);
   for(int i = 0; i < tot; i++)
   {
    if(minvol > vols[i] && boxSizes[i][0] >= nowBox[0] && boxSizes[i][1] >= nowBox[1] && boxSizes[i][2] >= nowBox[2])
     minvol = vols[i];
   }
   System.out.println(minvol<8000000001L?minvol:"Item does not fit.");
   minvol = 8000000001L;
  }
 }
}