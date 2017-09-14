import java.io.*;

public class DMOJ {
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int valA = Integer.parseInt(in.readLine());
  int valB = Integer.parseInt(in.readLine());
  
  int b=1, h=1;
  while(valB-valA+1 > b*h)
  {
   if(b==h) h++;
   else b++;
  }
  int[][] finArr = new int[h][b]; 
  int posy = (h-1)/2, posx = (b-1)/2, dir = -1;
  for(int i = 1; valA <= valB; i++)
  {
   dir = -dir;
   for(int j = 0; j < i && valA <= valB; j++)
   {
    finArr[posy][posx] = valA;
    valA++;
    posy+=dir;
   }

   for(int j = 0; j < i && valA <= valB; j++)
   {
    finArr[posy][posx] = valA;
    valA++;
    posx+=dir;
   }
  }
  
  for(int i = 0; i < finArr.length; i++)
  {
   for(int j = 0; j < finArr[0].length; j++)
   {
    if(finArr[i][j] == 0)
     System.out.print("   ");
    else if (finArr[i][j] < 10)
     System.out.print(" " + finArr[i][j] + " ");
    else
     System.out.print(finArr[i][j] + " ");
   }
   System.out.println();
  }
 }
}