#include <cstdio>  
//https://jksk0115.tistory.com/204

int Solve(int N); 
int firmcode_solve(int N);

  
int main(void)  
{  
    int T,N;  
    //scanf("%d", &T);  
  
    /*
    for (int i = 0; i < 100000; i++)  
    {  
        N=i;
        if(Solve(N) !=firmcode_solve(N))
        {
            printf("Error!! : %d",N);
        }
    }  
    */
    N=92683;
    printf("sovle : %d firmcode_solve : %d",Solve(N) ,firmcode_solve(N));
  
    return 0;  
}  


int firmcode_solve(int N)
{
    int T,Num;
    int cnt=0;
    int n,min_n,b,i,formula;

    cnt = 0;
    //cin>>Num;
    Num=N;
    //get min n
    for(i=0;i<Num;i++)
    {
        if(Num<(i*(i+1)/2))
        {
            break;
        }
    }
    min_n = i-1;
    //cout<<"min_n : "<<min_n<<endl;
    for(n=Num/2+1;n>=min_n-1;n--)
    {
        for(b=n-1;b>=0;b--)
        {
            //cout<<"n, b : "<<n<<" "<<b<<endl;
            formula=((n*(n+1)/2) - b*(b+1)/2);
            if(formula== Num)
            {
                //cout<<"cnt++"<<endl;
                cnt++;
            }
            else if(formula > Num)
            {
                break;
            }
        }
    }
    if(Num>2)
    {
        cnt++;
    }

    return cnt;
    //cout<<"#"<<t<<" "<<cnt<<endl;

}


  
int Solve(int N)  
{  
    int count = 0;  
  
    for (int y = 0; y <= N; y++)  
    {  
        int A = 2 * N - y * y - y; 
        int B = 2 * y + 2; 
  
        if (A <= 0)  
            break;  
  
        if (A % B == 0)  
            count++;  
    }  
  
    return count;  
}  