import java.util.Scanner;
//lowkey i gotta get these points onto this account
public class CCCEncode{
    public static void main (String[] arg)
 {
  Scanner in = new Scanner(System.in);
  int shift = 0;
  String inMsg, outMsg = "";
  char letter = ' ';
  
  shift = in.nextInt();
  shift %= 26;
  in.nextLine();
  inMsg = in.nextLine();
  
  for(int i = 0; i < inMsg.length(); i++)
  {
   letter = inMsg.charAt(i);
   if(letter >= 'A' && letter <= 'Z')
   {
    if((letter - shift) > 'Z')
     outMsg += (char)(letter - shift - 26);
    else if((letter - shift) < 'A')
     outMsg += (char)(letter - shift + 26);
    else
     outMsg += (char)(letter - shift);
   }
   else if (letter >= 'a' && letter <= 'z')
   {
    if((letter - shift) > 'z')
     outMsg += (char)(letter - shift - 26);
    else if((letter - shift) < 'a')
     outMsg += (char)(letter - shift + 26);
    else
     outMsg += (char)(letter - shift);
   }
   else
    outMsg += ' ';
  }
  System.out.println(outMsg);
  in.close();
 }
}