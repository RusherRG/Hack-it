package temp;
import java.util.*;
public class Weed {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		int c = sc.nextInt();
		int x = sc.nextInt();
		int sum = 0;
	    sum = c % x;
	    c = c / x;
	    sum = calc(c, x, sum);
	    System.out.println(sum);
		
	}
	static int calc(int c, int x, int sum)
	{
	    while(c > 0)
	    {
	        sum += c % x;
	        c = c / x;
	        sum = calc(c, x, sum);
	        return sum;
	    }
	    return sum;
	}
}
