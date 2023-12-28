#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int num1;
    int num2;
    int total=0;
    int min_val;
    
    cin >> num1;
    cin >> num2;

    for(int i=num1; i<=num2; i++){
        int sroot = sqrt(i);
        if ((sroot*sroot) == i){
            if (total == 0)
                min_val = i;
            total += i;
        }
    }
    if(total != 0){
        cout << total << endl;
        cout << min_val << endl;
    }
    else{
        cout << -1 << endl;
    }
}
