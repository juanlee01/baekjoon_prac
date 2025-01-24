#include <iostream>
#include <string>
#include <vector>
#include <sstream>

using namespace std;

vector<string> split(string input, char dlim)
{
	vector<string> result;	// 분리한 문자열들을 저장하는 vector

	stringstream ss;		// stringstream 객체인 ss 선언
	string stringBuffer;	// stringstream에서 문자열 자를 때마다 임시로 저장하는 변수
	ss.str(input);			// ss에 문자열 삽입
	
    // ss에서 dlim 직전까지의 문자열을 잘라서 stringBuffer에 저장. ss가 빌 때까지 실행
	while (getline(ss, stringBuffer, dlim))	
	{
		result.push_back(stringBuffer);	// stringBuffer에 저장된 값을 result에 push_back
	}

	return result;
}

vector<int> intsplit(string input, char dlim)
{
    vector<int> returnint;
    stringstream ss(input);  // stringstream 객체 생성 및 초기화
    string stringBuffer;

    // ss에서 dlim 직전까지의 문자열을 잘라서 stringBuffer에 저장. ss가 빌 때까지 실행
    while (getline(ss, stringBuffer, dlim)) 
    {
        returnint.push_back(stoi(stringBuffer));  // vector에 정수 추가
    }

    return returnint;
}

int main(){
    string input;
    cin >> input;
    
    vector<int>nm = intsplit(input, ' ');

    vector<vector<int>> matrix1;
    for (int i = 0; i < nm[0]; i++)
    {
        cin >> input;
    
        matrix1.push_back(intsplit(input, ' '));
    }
    vector<vector<int>> matrix2;
    for (int i = 0; i < nm[0]; i++)
    {
        cin >> input;
    
        matrix2.push_back(intsplit(input, ' '));
    }

    for (int i = 0; i < nm[0]; i++)
    {
        for (int j = 0; j < nm[1]; j++)
        {

        }
        
    }
    
    
    return 0;
}