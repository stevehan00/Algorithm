# include <iostream>
# include <string>
#include <vector>
# include <algorithm>
using namespace std;

bool cmp(vector<int> &v1, vector<int> &v2){
    if(v1[2]==v2[2]){
        if(v1[1]==v2[1]){
            return v1[0] < v2[0];
        }
        else{
            return v1[1] < v2[1];
        }
    }
    else{
        return v1[2] < v2[2];
    }
}

int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    string name;
    vector<int> l(4);
    int num;
    cin >> num;

    vector<vector<int>> v;
    vector<string> name_vec;

    for(int i = 0; i < num; i++){
        cin >> name >> l[0] >> l[1] >> l[2];
        l[3] = i;
        name_vec.push_back(name);
        v.push_back(l);
    }

    sort(v.begin(), v.end(), cmp);
    cout << name_vec[v[num-1][3]] << endl;
    cout << name_vec[v[0][3]] << endl;

    return 0;
}
