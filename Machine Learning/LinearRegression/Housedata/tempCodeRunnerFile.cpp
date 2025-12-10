#include<iostream>
using namespace std;
int i = 0;
void abc(){
    if(i==10){return;}
    cout<<"Good Evening Suraj";
    abc();
    i++;
}
int main(){
    abc();
}