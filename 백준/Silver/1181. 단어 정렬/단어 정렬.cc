#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

bool sex(string str1 , string str2)
{
    if(str1.size()== str2.size()){
        return str1<str2;
    }
    else
        return str1.length() < str2.length();
}
	
int main()
{
	int num;
	cin >> num;
	string str[20000];
	for(int i=0;i<num;i++)
	{
		cin >> str[i];
	}
	sort(str,str+num,sex);
	for(int i =0; i<num;i++)
	{
		if( str[i] != str[i+1])
		{
			cout<<str[i]<<endl;	
		}
		else
		{
			continue;
		}
	}
}