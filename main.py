stlist=['J','j','B','b','SA','H','h','SH','sh','WC','D']
def comfirm(n):
  if n=="1":
    return 1
  else:
    return 0
hint='0'
while hint=='0':
  print('歡迎使用accountant 1.0\n')
  print("使用規則:")
  print('1.順序就是玩家代號!')
  print("2.火車站,私人住宅,書店 不可使用此系統!")
  print('3.飲料店、麵包店、民宿、溫泉旅館\n  營業前皆須做好事前準備，')
  print('4.火車站,私人住宅,書店外的物業\n  需於本系統登記才算開始營業\n')
  hint=input("輸入1開始遊戲\n")
print('\n遊戲開始!!\n')
flag=0
while 1:
  playern=input("輸入玩家人數(不超過9人， 不少於2人)\n")
  if playern=='' or not(2<=int(playern)<=9):
    print('玩家人數不超過9人，不少於2人\n')
  else:
    break
playern=int(playern)
Bill=[[0,0]for i in range(playern)] 
  ##[回合記帳,回合後統整]
WC=[[0,0,1]for i in range(6)] 
  ##[持有玩家代號, , ]
D=[[0,0,1]for i in range(3)]
for j in range(60):
  if flag:
    break
  print("\n--------------------")
  print('第'+str(j+1)+'回合\n')
  while 1:
    player=input("填入玩家代號(n)\n停止此輪(0)\n結束遊戲(-1)\n")
    if player=='' or (not(1<=int(player)<=playern)) and (int(player)!=0) and (int(player)!=-1):
      print('非法字元\n')
    elif int(player)==0:
      n=input("取消(0)  [確定停止此輪](1)\n")
      if comfirm(n):
        break
    elif int(player)==-1:
      n=input("取消(0)  [確定結束遊戲](1)\n")
      if comfirm(n):
        flag=1
        break
    else:
      store=input("登記營業(0)\n再加蓋(1)\n賣出物業(2)\n使用技能書(3)\n提款(4)\n接管線或購買貨運服務(5)\n查看帳戶金額(6)\n")
      if store=='0':
        store=input("輸入要登記營業的事業代號(J,j,B,b,SA,H,h,SH,sh,WC,D)\n")
        n=input("取消(0)  確定(1)\n")
        if not(comfirm(n)):
          pass
        elif store in stlist:
          if store=='J':
            Bill[int(player)-1][0]+=0.45
          elif store=='j':
            Bill[int(player)-1][0]+=0.35
          elif store=='B':
            Bill[int(player)-1][0]+=0.52
          elif store=='b':
            Bill[int(player)-1][0]+=0.37
          elif store=='SA':
            Bill[int(player)-1][0]+=1
          elif store=='H':
            Bill[int(player)-1][0]+=1.35
          elif store=='h':
            Bill[int(player)-1][0]+=1.3
          elif store=='SH':
            Bill[int(player)-1][0]+=1.8
          elif store=='sh':
            Bill[int(player)-1][0]+=1.4
          elif store=='WC':
            WC_n=int(input('輸入公司編號(1~6)\n'))
            if WC_n in [1,2,3,4,5,6]:
              WC[WC_n-1][0]=int(player)
            else:
              print('非法字元\n')
          else:
            D_n=int(input('輸入公司編號(1~3)\n'))
            if D_n in [1,2,3]:
              D[D_n-1][0]=int(player)
        else:
          print("火車站,私人住宅,書店 不可使用此系統!\n")
        
      elif store=='1':
        store=input("請輸入要加蓋第2棟房屋的事業代號 (SH,sh)\n" ) ###
        if store!='SH'and'sh':
          print('除溫泉旅館不可蓋第二座木屋\n')
        elif store=='SH':
          Bill[int(player)-1][0]+=1
        else:
          Bill[int(player)-1][0]+=1  
      elif store=='2':
        store=input("請輸入[要賣出的]事業代號 (J,j,B,b,SA,H,h,SH,sh,WC,D)\n")
        if store in stlist:
          book=int(input('請輸入技能書倍數(2,3), 沒有則填1\n'))
          house=int(input('房屋數量, 沒有則填1\n'))
          if book not in [1,2,3]:
            print('非法字元\n')
          elif house not in [1,2]:
            print('非法字元\n')
          elif store=='J':
            Bill[int(player)-1][0]-=0.45*book
          elif store=='j':
            Bill[int(player)-1][0]-=0.35*book
          elif store=='B':
            Bill[int(player)-1][0]-=0.52*book
          elif store=='b':
            Bill[int(player)-1][0]-=0.37*book
          elif store=='SA':
            Bill[int(player)-1][0]-=1*book
          elif store=='H':
            Bill[int(player)-1][0]-=1.35*book
          elif store=='h':
            Bill[int(player)-1][0]-=1.3*book
          elif store=='SH':
            Bill[int(player)-1][0]-=(1.8+1*(house-1))*book
          elif store=='sh':
            Bill[int(player)-1][0]-=(1.4+1*(house-1))*book
          elif store=='WC':
            WC_n=input('請輸入公司編號(1~6)\n')
            if WC_n in ['1','2','3','4','5','6']:
              if WC[int(WC_n)-1][0]!=int(player):
                print('玩家不持有該公司\n')
              else:
                WC[int(WC_n)-1][0]=0 #0是銀行的
            else:
              print('非法字元\n')
            
          else:
            D_n=input('請輸入公司編號(1~3)\n')
            if D_n in ['1','2','3']:
              if D[int(D_n)-1][0]!=int(player):
                print('玩家不持有該公司\n')
              else:
                D[int(D_n)-1][0]=0#0是銀行的
            else:
              print('非法字元\n')
        else:
          print("火車站, 私人住宅, 書店 不可使用此系統\n")
      elif store=='3':
        store=input("請輸入要使用的事業代號(J,j,B,b,SA,H,h,SH,sh,WC,D)\n")
        time=input("請輸入技能書收入倍數(2,3)\n" )
        if store in stlist:
          if store=='J':
            Bill[int(player)-1][0]+=0.45*(float(time)-1)
          elif store=='j':
            Bill[int(player)-1][0]+=0.35*(float(time)-1)
          elif store=='B':
            Bill[int(player)-1][0]+=0.52*(float(time)-1)
          elif store=='b':
            Bill[int(player)-1][0]+=0.37*(float(time)-1)
          elif store=='SA':
            Bill[int(player)-1][0]+=1*(float(time)-1)
          elif store=='H':
            Bill[int(player)-1][0]+=1.35*(float(time)-1)
          elif store=='h':
            Bill[int(player)-1][0]+=1.3*(float(time)-1)
          elif store=='SH':
            Bill[int(player)-1][0]+=1.8*(float(time)-1)
          elif store=='sh':
            Bill[int(player)-1][0]+=1.4*(float(time)-1)
          elif store=='WC':
            WC_n=input('輸入公司編號(1~6)\n')
            if WC_n in ['1','2','3','4','5','6']:
              WC[int(WC_n)-1][2]+=1*(float(time)-1)
            else:
              print('非法字元\n')
          elif store=='D':
            D_n=input('輸入公司編號(1~3)\n')
            if D_n in ['1','2','3']:
              D[int(D_n)-1][2]+=1*(float(time)-1)
            else:
              print('非法字元\n')
        else:
          print("火車站, 私人住宅, 書店 不可使用此系統\n")
      elif store=='4':
        store=input("輸入提款金額(M),現有金額:"+str(Bill[int(player)-1][1])+'M\n')
        hint=int(input("若[確定提款"+store+"M]填1\n取消填0\n"))
        if hint==1:  
          if Bill[int(player)-1][1]-float(store)>=0:  
            Bill[int(player)-1][1]-=float(store)
            print('領取'+store+'M')
          else:
            print('金額不足')
      elif store=='5':
        store=input('接自來水管線(0)\n購買貨運服務線(1)')
        if store=='0':
          WC_n=input('請輸入公司編號(1~6)\n')
          if WC_n in ['1','2','3','4','5','6']:
            WC[int(WC_n)-1][1]+=1
          else:
            print('非法字元')
        elif store=='1':
          D_n=input('請輸入公司編號(1~3)\n')
          if D_n in ['1','2','3']:
            D[int(D_n)-1][1]+=1
          else:
            print('非法字元')
        else:
          print('非法字元')
      elif store=='6':
        print('玩家'+player+' 帳戶金額'+str(Bill[int(player)-1][1])+'\n')## 錯誤 帳戶金額顯示未增加
      else:
        print("非法字元\n")
  for k in range(playern):
    Bill[k][1]+=Bill[k][0]
  for l in range(6):
    if WC[l][0]!=0:
      Bill[WC[l][0]-1][1]+=WC[l][1]*WC[l][2]
  for m in range(3):
    if D[m][0]!=0:
      Bill[D[m][0]-1][1]+=D[m][1]*D[m][2]
print('遊戲結束!!\n--------------------\n')
for n in range(playern):
  print('玩家'+str(n+1)+' 帳戶金額'+str(Bill[n-1][1])+'M')
      
