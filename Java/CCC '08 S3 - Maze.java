import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
 static class Coord
 {
  int row, col, dist = 1;
  public Coord(int x, int y, int dist)
  {
   this.row = x;
   this.col = y;
   if(this.dist == 1)
    this.dist += dist;
   else if(dist < this.dist - 1)
    this.dist = dist + 1;
  }
 }
 
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int cases = Integer.parseInt(in.readLine()), rows, cols;
  Queue<Coord> q = new LinkedList<Coord>();
  Coord currCoord;
  for(;cases>0;cases--)
  {
   rows = Integer.parseInt(in.readLine());
   cols = Integer.parseInt(in.readLine());
   char[][] city = new char[rows][];
   int[][] visited = new int[rows][cols];
   for(int i = 0; i < rows; i++)
    city[i] = in.readLine().toCharArray();
   q.add(new Coord(0, 0, 0));
   while(q.peek() != null)
   {
    currCoord = q.remove();
    if(visited[currCoord.row][currCoord.col] == 0)
    {
     visited[currCoord.row][currCoord.col] = currCoord.dist;
     if(currCoord.row > 0) 
      if(visited[currCoord.row-1][currCoord.col] == 0 && (city[currCoord.row][currCoord.col] == '|' ||
      city[currCoord.row][currCoord.col] == '+') && city[currCoord.row-1][currCoord.col] != '*')
       q.add(new Coord(currCoord.row-1, currCoord.col, currCoord.dist));
     if(currCoord.row < rows - 1) 
      if(visited[currCoord.row+1][currCoord.col] == 0 && (city[currCoord.row][currCoord.col] == '|' ||
      city[currCoord.row][currCoord.col] == '+') && city[currCoord.row+1][currCoord.col] != '*') 
       q.add(new Coord(currCoord.row+1, currCoord.col, currCoord.dist));
     if(currCoord.col > 0) 
      if(visited[currCoord.row][currCoord.col-1] == 0 && (city[currCoord.row][currCoord.col] == '-' || 
      city[currCoord.row][currCoord.col] == '+') && city[currCoord.row][currCoord.col-1] != '*') 
       q.add(new Coord(currCoord.row, currCoord.col-1, currCoord.dist));
     if(currCoord.col < cols - 1) 
      if(visited[currCoord.row][currCoord.col+1] == 0 && (city[currCoord.row][currCoord.col] == '-' || 
      city[currCoord.row][currCoord.col] == '+') && city[currCoord.row][currCoord.col+1] != '*') 
       q.add(new Coord(currCoord.row, currCoord.col+1, currCoord.dist));
    }
   }
   System.out.println(visited[rows-1][cols-1]>0?visited[rows-1][cols-1]:-1);
  }
 }
}