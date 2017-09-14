import java.util.Scanner;
 
public class CCCQuestion{

    public static void main (String[] arg)
 {
  Scanner in = new Scanner(System.in);
  
  int subtractNum = 0;
  int totNum = 0;
  int lastIndex = 0;
  int firstIndex = 0;
  
  String inAsStr = "";
  
  totNum = in.nextInt();
  in.nextLine();
  
  for(int z = 0; z < totNum; z++)
  {
   inAsStr = in.nextLine();
   System.out.println(inAsStr);
   int[] numbers = new int[inAsStr.length()];
   for(int i = 0; i < inAsStr.length(); i++)
    numbers[i] = inAsStr.charAt(i) - '0';
   firstIndex = 0;
   lastIndex = numbers.length;
   
   while((lastIndex - firstIndex) > 2)
   {
    lastIndex--;
    subtractNum = numbers[lastIndex];
    
    for(int i = lastIndex - 1; i >= firstIndex; i--)
    {
     if(numbers[i] >= subtractNum)
     {
      numbers[i] -= subtractNum;
      break;
     }
     else
     {
      numbers[i] = (numbers[i] + 10 - subtractNum);
      subtractNum = 1;
     }
    }
    while(numbers[firstIndex] == 0 && firstIndex < lastIndex)
     firstIndex++;
    for(int i = firstIndex; i < lastIndex; i++)
     System.out.print(numbers[i]);
    System.out.println();
   }
   if(numbers[lastIndex - 1] == numbers[firstIndex] && lastIndex - firstIndex == 2)
    System.out.println("The number " + inAsStr + " is divisible by 11.");
   else
    System.out.println("The number " + inAsStr + " is not divisible by 11.");
  }
 }
}