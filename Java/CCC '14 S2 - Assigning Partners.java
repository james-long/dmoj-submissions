import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.*;

public class Main {
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int index, index2;
  boolean yn = true;
  in.readLine();
  ArrayList<String> a = new ArrayList<String>(Arrays.asList(in.readLine().split(" "))), b = new ArrayList<String>(Arrays.asList(in.readLine().split(" ")));
  for(int i = 0; i < a.size(); i++) 
  {
   index = b.indexOf(a.get(i)); 
   index2 = a.indexOf(b.get(i)); 
   if(!(index == index2) || index == i || index2 == i)
    yn = false;
  }
  System.out.print(yn?"good":"bad");
 }
}