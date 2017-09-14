import java.io.BufferedReader;
import java.io.InputStreamReader;

public class DMOJ {
 
 public static void main (String[] arg) throws Exception
 { 
  BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
  int tot = Integer.parseInt(in.readLine()), posVow, posSpc;
  String [] lines = new String[4], endings = new String[4];
  for(;tot > 0; tot--)
  {
   for(int i = 0; i < 4; i++) lines[i]=in.readLine();
   for(int i = 0; i < 4; i++)
   {
    posVow = Math.max(lines[i].toLowerCase().lastIndexOf('a'), 
    Math.max(lines[i].toLowerCase().lastIndexOf('e'), 
    Math.max(lines[i].toLowerCase().lastIndexOf('i'), 
    Math.max(lines[i].toLowerCase().lastIndexOf('o'), 
    lines[i].toLowerCase().lastIndexOf('u')))));
    posSpc = lines[i].lastIndexOf(' ');
    if(posVow == posSpc) endings[i] = lines[i].toLowerCase();
    else endings[i] = lines[i].toLowerCase().substring(Math.max(posVow, posSpc+1));
   }
   if(endings[0].equals(endings[1]) && endings[1].equals(endings[2]) && endings[2].equals(endings[3])) System.out.println("perfect");
   else if (endings[0].equals(endings[1]) && endings[2].equals(endings[3])) System.out.println("even");
   else if (endings[0].equals(endings[2]) && endings[1].equals(endings[3])) System.out.println("cross");
   else if (endings[0].equals(endings[3]) && endings[1].equals(endings[2])) System.out.println("shell");
   else System.out.println("free");
  }
 }
}