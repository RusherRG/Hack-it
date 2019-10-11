import java.util.*;
import java.io.*;
class friendsol
{
    public static void main(String args[])throws IOException
    {
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int t,n,i,j,ans;
        long init;
        String p;
        String s[];
        t=Integer.parseInt(br.readLine());
        init=System.currentTimeMillis();
        for(int q2=1;q2<=t;q2++)
        {
            n=Integer.parseInt(br.readLine());
            s=new String[n];
            ans=0;
            p=br.readLine();
            s=p.split(" ");
            
            for(j=0;j<n;j++)
            {
                i=Integer.parseInt(s[j]);
                ans=ans^i;
            }

            if(ans==0)
            System.out.println("-1");
            else
            System.out.println(ans);
        }
        System.out.println("time is "+(System.currentTimeMillis()-init));
    }
}

/*
t=int(input())
for i in range(t):
    n=int(input())
    s1=input()
    s=s1.split()
    ans=0

    for p in s:
        a=int(p)
        ans=ans^a

    if ans==0:
        print("-1")
    
    else:
        print(ans)
*/