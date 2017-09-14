import java.io.BufferedReader;
import java.io.InputStreamReader;

public class DMOJ {
 
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  String[] bounds = in.readLine().split(" "), move;
  int xPos = 0, yPos = 0, xD, yD;
  int[] bnd = {Integer.parseInt(bounds[0]), Integer.parseInt(bounds[1])};
  do
  {
   move = in.readLine().split(" ");
   xD = Integer.parseInt(move[0]);
   yD = Integer.parseInt(move[1]);
   xPos += xD;
   yPos += yD;
   if(xPos < 0) xPos = 0;
   else if(xPos > bnd[0]) xPos = bnd[0];
   if(yPos < 0) yPos = 0;
   else if(yPos > bnd[1]) yPos = bnd[1];
   if(xD != 0 || yD != 0) System.out.format("%d %d\n", xPos, yPos);
  } while (xD != 0 || yD != 0);
  
 }
}