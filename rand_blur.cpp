#include<iostream>
#include<math.h>
using namespace std;


int main(){
    int height = 800, width = 1200;
    int arr[height][width];
    int i,j;

    int midx = width/2;
    int midy = height/2;

    int sig = 1;
    int r,s = 2*sig*sig;
    int x,y;
    cout<<1200;
    
    for(i=0;i<width;i++){
        for(j=0;j<height;j++){
                x = i-midx;
                y = j-midy;
                r = sqrt(x*x + y*y);
                arr[i][j] = (1/s*M_1_PI)*exp(r*r/s);
                //cout<<(arr[i][j]);
                
        }
    }
}
