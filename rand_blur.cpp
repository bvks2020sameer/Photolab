#include<iostream>
#include<math.h>
using namespace std;


int main(){
    int height = 800, width = 1200;
    int arr[height][width];
    int i,j;

 

    int sig = 1;
    int r,s = 2*sig*sig;
    int midx = width/2,midy=height/2;        
    
    for(i=0;i<width;i++){
        for(j=0;j<height;j++){
                r = sqrt((i-midx)*(i-midx) + (j-midy)*(j-midy));
                arr[i][j] = (float)(sqrt(1/(s*3.414)))*(float)exp((double)r/s);
                cout<<(arr[i][j])<<" ";
                
        }
        cout<<'\n';
    }
}
