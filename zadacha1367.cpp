#include <iostream>
#include <vector>
#include <queue>
#include <string>
#include <climits>
#include <cmath>
using namespace std;



bool sol(string s){
    int j = s.size() - 1;
    int ans = 0;
    for (int i = 0; i < s.size(); ++i){
        ans += (s[i] - '0') * pow(10, j);
        --j;
    }
    ++ans;
    return (ans < 256);
}
 
int main(){
    string x; cin >> x;
    string str;
    int c = 0;
    int count = 0;
    for (int i = 0; i < x.size(); ++i){
        if (x[i] == '.'){
            ++i; ++c;
            if (x[i] == '.'){
                cout << "Bad";
                return 0;
            }
            if (!sol(str)){
                cout << "Bad";
                return 0;
            }
            str = "";
        }
        str.push_back(x[i]);
    }
    if (x[x.size() - 1] == '.' || x[0] == '.'){
        cout << "Bad";
        return 0;
    }
    cout << (c == 3? "Good": "Bad");
    return 0;
}
