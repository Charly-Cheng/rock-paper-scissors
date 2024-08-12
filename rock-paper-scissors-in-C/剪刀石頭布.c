#include <stdio.h>
#include <windows.h>
#include <stdlib.h>
#include <time.h>
int main()
{
  //宣告使用UTF-8編碼,字串,隨機起始值 
  SetConsoleOutputCP(65001);
  int usario,pc,control= 0;
  int st=5;
  char lista [4][10] = {"離開","石頭✊","剪刀✌","布🤚"};
  srand(time(NULL));
  void sleeptime (int);
  //開始進入
  do{
  control=0;   
  // 控制用戶輸入的數值是 1,2,3
  while (control!=1){
      system("cls");
      printf ( " 這是與電腦玩%s、%s、%s的遊戲 \n",lista[1],lista[2],lista[3]);
      printf ( "\n 1. %s \n 2. %s \n 3. %s \n 0. %s\n\n 請選擇：",lista[1],lista[2],lista[3],lista[0]);
      fflush(stdin); //避免用戶輸入格式錯誤,清除緩存
      usario=5; // 常態錯誤,只有用戶輸入正確的值,避免上輪正確下輪輸入格式錯誤
      scanf ("%d", &usario);
      if (!((usario == 1)||(usario == 2)||(usario == 3)||(usario == 0))){
        printf("\n 請輸入正確的數值\n\n");
        //等待st秒後繼續
        sleeptime (2);
        }
      else{control=1;}
  }
 //用戶輸入的數值是 1,2,3, 開始進程
  if ((usario == 1)||(usario == 2)||(usario == 3)){
        printf ( "\n 您選擇：%s\n", lista[usario]);
        pc = (rand()%3)+1 ; //電腦隨機生成1-3的值
        printf ( "\n 電腦選擇 ：%s \n",lista[pc]);
        if (usario == pc){
            printf ("\n 平手\n\n" ); 
            sleeptime (st);}
        else{
            if ((usario == 1 && pc == 2) ||(usario == 2 && pc == 3) ||(usario == 3 && pc == 1)){
                printf ("\n 玩家贏了\n\n");sleeptime (st);;}
            else {printf ("\n 電腦贏了\n\n" );sleeptime (st);;}
            }
            }
    }while(usario!=0);
    printf ( "\n 您選擇：%s\n", lista[usario]);
    printf ("\n祝您玩得愉快 , 歡迎再來玩\n\n");
    system("pause");
   return 0;
}
 // 延遲函數,等待%d秒後繼續
 void sleeptime (int controltime){
          while (controltime!=0)
        {
          printf(" 等待%d秒後繼續\r", controltime);Sleep(1000); controltime--;
        }
 }
