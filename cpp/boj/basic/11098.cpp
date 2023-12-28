#include <iostream>
#include <string>

using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int n;

    cin >> n; 

    for(int i=0; i<n; i++){
        int p;
        cin >> p;

        int top_price=0;
        string name;

        for(int j=0; j<p; j++){
            int cur_price;
            string cur_name;
            cin >> cur_price >> cur_name;

            if(cur_price > top_price){
                top_price = cur_price;
                name = cur_name;
            }
        }

        cout << name << endl;
    }
}