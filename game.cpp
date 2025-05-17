#include <iostream>
#include <cstdio>
#include <random>
#include <chrono>
using namespace std;
mt19937 rnd(19491001);
int N=11;
struct node{
    double r;
    int K,p;
    void evolve(){
        if (r<0)p+=(int)(r*p);
        else p+=(int)(r*p*(1.0-1.0*p/K));
        p=max(p,0);
        return;
    }
}a[11][11];
int mv[4][2]={{0,1},{0,-1},{1,0},{-1,0}};
bool cmp(node a,node b){ // 比较两个国家的“移居程度”
    return (a.r*(1.0-1.0*a.p/a.K)>b.r*(1.0-1.0*b.p/b.K));
}
void evolve(){
    for (int i=0;i<N;i++)
        for (int j=0;j<N;j++){
            int o;
            o=rnd()%10;
            if (o==0)a[i][j].r+=0.01;
            if (o==1)a[i][j].r-=0.01;
            o=rnd()%10;
            if (o==0)a[i][j].K+=200000;
            if (o==1)a[i][j].K-=200000;
            a[i][j].r=max(a[i][j].r,-0.05);
            a[i][j].r=min(a[i][j].r,0.1);
            a[i][j].K=max(a[i][j].K,1000000);
            a[i][j].K=min(a[i][j].K,20000000);
            // 此处为增长率、上限的随机变化
        }
    for (int i=0;i<N;i++)
        for (int j=0;j<N;j++){
            for (int k=0;k<4;k++){
                int x=i+mv[k][0],y=i+mv[k][1];
                if (x>=0&&x<N&&y>=0&&y<N&&cmp(a[x][y],a[i][j])){
                    int c=a[i][j].p*0.002;
                    a[i][j].p-=c,a[x][y].p+=c;
                    // 此处考虑移民影响
                }
            }
        }
    for (int i=0;i<N;i++)
        for (int j=0;j<N;j++)
            a[i][j].evolve();
    return;
}
int main(){
    freopen("data100000.out","w",stdout);
    for (int i=0;i<N;i++)
        for (int j=0;j<N;j++)
            a[i][j].r=0,a[i][j].K=10000000,a[i][j].p=5000000; // 初始增长率、上限、人口
    for (int i=1;i<=100000;i++)evolve();// 随机演化100000年，打乱初始分布
    int T=0;
    int B=100000; // 观察的时间尺度
    long long sum=0;
    while(T<300*B){
        evolve();
        for (int i=0;i<N;i++)
            for (int j=0;j<N;j++)
                sum+=a[i][j].p;
        if (T%B==0){
            if (T>0)cout<<sum/B<<endl;
            sum=0;
        }
        T++;

    }
    return 0;
}