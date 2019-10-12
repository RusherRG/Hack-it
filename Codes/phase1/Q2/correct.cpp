#include <iostream>
#include <math.h>
#include <stdio.h>

using namespace std;

int main()
{
	int tc,x1,y1,x2,y2,x,y;
	cin>>tc;
	while(tc--){
		cin>>x1>>y1>>x2>>y2;
        x = 2*x2 - x1;
        y = 2*y2 - y1;
        cout<<x<<" "<<y<<endl;
	}
	return 0;
}