import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Collections;

public class Main {
 
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int[] freq =  new int[1000];
  int tot = Integer.parseInt(in.readLine()), maxFreq = 0, secondMaxFreq = 0, maxDelta = 0;
  ArrayList<Integer> positions = new ArrayList<Integer>();
  for(;tot>0;tot--)
  {
   freq[Integer.parseInt(in.readLine()) - 1]++;
  }
  for(int fr:freq)
   if(fr > maxFreq) maxFreq = fr;
  for(int i = 0; i < freq.length; i++)
   if(freq[i] == maxFreq)
   {
    positions.add(i);
    freq[i] = 0;
   }
  if(positions.size() > 1)
  {
   Collections.sort(positions);
   System.out.print(positions.get(positions.size()-1) - positions.get(0));
  }
  else
  {
   for(int fr:freq)
    if(fr > secondMaxFreq) secondMaxFreq = fr;
   for(int i = 0; i < freq.length; i++)
    if(freq[i] == secondMaxFreq && Math.abs(positions.get(0) - i) > maxDelta)
     maxDelta = Math.abs(positions.get(0) - i);
   System.out.print(maxDelta);
  }
 }
}