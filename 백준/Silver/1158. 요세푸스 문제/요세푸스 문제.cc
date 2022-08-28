#include<iostream>
#include<queue>

using namespace std;

void solution(int size,int num)
{
	queue<int> que;
	
	for(int i=1;i<=size;i++)
	{
		que.push(i);
	}
	
	cout<<"<";
	
	for(int i=1;i<size;i++)
	{
		for(int j=1;j<=num-1;j++)
		{
			que.push(que.front());
			que.pop();
		}
		cout<<que.front()<<", ";
		que.pop();
	}
	cout<<que.front()<<">";
	
}



int main()
{
	int size,num;
	cin>>size>>num;
	solution(size,num);
}