import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

public class Main {
 static int[][] floor;
 static int rows, cols;
 
 static void fill(int value, int i, int j)
 {
  floor[i][j] = value;
  if(i+1 < rows) if(floor[i+1][j] == 0) fill(value, i+1, j);
  if(i-1 > -1) if(floor[i-1][j] == 0) fill(value, i-1, j);
  if(j+1 < cols) if(floor[i][j+1] == 0) fill(value, i, j+1);
  if(j-1 > -1) if(floor[i][j-1] == 0) fill(value, i, j-1);
  return;
 }
 
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int area = Integer.parseInt(in.readLine()), currentRoom = 0;
  rows = Integer.parseInt(in.readLine());
  cols = Integer.parseInt(in.readLine());
  String temp;
  floor = new int[rows][cols];
  for(int i = 0; i < rows; i++)
  { 
   temp = in.readLine();
   for(int j = 0; j < cols; j++)
    if(temp.charAt(j) == 'I') 
     floor[i][j] = -1;
  }
  for(int i = 0; i < rows; i++)
  { 
   for(int j = 0; j < cols; j++)
   {
    if(floor[i][j] == 0)
    {
     currentRoom++;
     fill(currentRoom, i, j);
    }
   }
  }
  int[] floorVals = new int[currentRoom];
  for(int i = 0; i < rows; i++)
   for(int j = 0; j < cols; j++)
    if(floor[i][j] > 0) floorVals[floor[i][j]-1]++;
  Arrays.sort(floorVals);
  int rooms = 0;
  for(int i = floorVals.length - 1; i>=0; i--)
  {
   if(area - floorVals[i] >= 0)
   {
    area -= floorVals[i];
    rooms++;
   }
   else
    break;
  }
  System.out.print(rooms + " room" + (rooms==1?"":"s") + ", " + area + " square metre(s) left over");
 }
}