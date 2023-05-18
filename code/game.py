import pygame#import thư viện pygame
from random import randint


pygame.init() #Khởi tạo tất cả các mô-đun Pygame đã được nhập

#Tạo một màn hình hiển thị trò chơi với kích thước chiều rộng là 1000 và chiều cao là 400
screen=pygame.display.set_mode((1000,400)) 

pygame.display.set_caption('Vượt chướng ngại vật để tìm kho báu') #Đặt tên tiêu đề cho màn hình 

clock = pygame.time.Clock()#tạo đối tượng Clock, được sử dụng để giới hạn số lần khung hình được vẽ trên màn hình trong một giây
FPS=120
start_time = pygame.time.get_ticks()

#Load hình ảnh và gán vào các biến:
bg1=pygame.image.load('img/bg1.png') #Background đầu game 
play=pygame.image.load('img/play.png') #ảnh nút play

bg2=pygame.image.load('img/bg2.png') #Background khi chơi game
mau=pygame.image.load('img/mau.png')
run1=pygame.image.load('img/run1.png')
run2=pygame.image.load('img/run2.png')
run3=pygame.image.load('img/run3.png')
run4=pygame.image.load('img/run4.png')
run5=pygame.image.load('img/run5.png')
run6=pygame.image.load('img/run6.png')
run7=pygame.image.load('img/run7.png')
run8=pygame.image.load('img/run8.png')

bom=pygame.image.load('img/bom.png')
noo=pygame.image.load('img/bom_no.png')
mb=pygame.image.load('img/mb.png')
qua=pygame.image.load('img/qua.png')
vang=pygame.image.load('img/vang.png')
khung=pygame.image.load('img/khung.png')
khung2=pygame.image.load('img/khung2.png')
icon_vang=pygame.image.load('img/icon_vang.png')
icon_khien=pygame.image.load('img/icon_khien.png')
nam_cham=pygame.image.load('img/nam_cham.png')
icon_thuoc=pygame.image.load('img/icon_thuoc.png')
icon_shop=pygame.image.load('img/icon_shop.png')
quit=pygame.image.load('img/quit.png')
buy=pygame.image.load('img/buy.png')
shop=pygame.image.load('img/shop.png')
khien_shop=pygame.image.load('img/khien_shop.png')
thuoc_shop=pygame.image.load('img/thuoc_shop.png')
khien2=pygame.image.load('img/khien2.png')
mau=pygame.image.load('img/mau.png')

lose=pygame.image.load('img/lose.png') #Background khi thua
yes=pygame.image.load('img/yes.png') #ảnh nút yes
no=pygame.image.load('img/no.png') #ảnh nút no
win=pygame.image.load('img/win.png')#Background  khi thắng
kho_bau=pygame.image.load('img/kho_bau.png')

#Tải âm thanh và gán vào biến
sound_an_vang = pygame.mixer.Sound("sound/sound_an_vang.mp3")
sound_no=pygame.mixer.Sound("sound/sound_no.mp3")
sound_thua=pygame.mixer.Sound("sound/sound_thua.mp3")
sound_thang=pygame.mixer.Sound("sound/sound_win.mp3")
sound_qua=pygame.mixer.Sound("sound/sound_qua.mp3")
sound_click=pygame.mixer.Sound("sound/sound_click.mp3")
sound_nen=pygame.mixer.Sound("sound//music.mp3")


class Button():# Tạo 1 class Button    
    #Hàm khởi tạo(__init__) được sử dụng để gán giá trị cho các thuộc tính của đối tượng 
    #hoặc thực hiện một số thao tác khi đối tượng đang được tạo ra.
    def __init__(self, x, y, image):  #Truyền các giá trị cho các đối tượng
        self.image = image
        self.rect = self.image.get_rect() # Tạo khung chữ nhật bao quanh ảnh
        self.rect.topleft = (x, y) # Tọa độ của button (khung bao quanh ảnh)
        self.clicked = False
    def draw(self):
        action = False
        pos = pygame.mouse.get_pos()#Lấy vị trí chuột
		#kiểm tra điều kiện di chuột qua và nhấp chuột
        if self.rect.collidepoint(pos):#Nếu chuột chạm vào hình chữ nhật bao quanh button
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
             #Nếu đã nhấp chuột trái và self.clicked == False
                self.clicked = True
                action = True
                sound_click.play() # phát sound click
        if pygame.mouse.get_pressed()[0] == 0:
         #Nếu chưa nhấp chuột trái 
            self.clicked = False
        screen.blit(self.image, (self.rect.x, self.rect.y))#Vẽ lên màn hình
        return action# action = True nếu đã nhấp chuột trái và ngược lại
		
#Gán các button với tọa độ và hình ảnh button mình mong muốn vào các biến
play_button = Button(740, 240, play)
yes_button = Button(400, 277, yes)
no_button = Button(525, 280, no)
shop_button = Button(930,0,icon_shop)
quit_button=Button(455,290,quit)
buy_button1=Button(380,220,buy)
buy_button2=Button(550,220,buy)
khien_button=Button(400,2,icon_khien)
nc_button=Button(600,5,nam_cham)
thuoc_button=Button(750,6,icon_thuoc)

def draw_sl_vang():#Vẽ số lượng còn lại của vàng
    score_vang = font.render(str(sl_vang), True, (192,192,192)) 
    screen.blit(khung,(37,40))
    screen.blit(score_vang,(45,40))

def draw_sl_thuoc():#Vẽ số lượng còn lại của thuốc
    score_thuoc = font.render(str(sl_thuoc), True, (192,192,192))
    screen.blit(khung2,(800,1))
    screen.blit(score_thuoc,(810,0))

def draw_sl_khien():#Vẽ số lượng còn lại của khiên
    score_khien = font.render(str(sl_khien), True, (192,192,192))
    screen.blit(khung2,(440,1))
    screen.blit(score_khien,(450,0))

def draw_sl_nc():#Vẽ số lượng còn lại của nam châm
    score_nc = font.render(str(sl_nam_cham), True, (192,192,192))
    screen.blit(khung2,(630,1))
    screen.blit(score_nc,(640,0))

def draw_sl_mau():#Vẽ số lượng còn lại của máu
    score_mau = font.render(str(sl_mau), True, (192,192,192))
    screen.blit(khung,(37,0))
    screen.blit(score_mau,(45,0))

#Vẽ màn hình game
def draw_bg():
    screen.blit(bg2,(bg2_x,0))
    screen.blit(bg2,(bg2_x+1000,0))

list_vang1=[vang,vang,vang,vang,vang]# vàng trên trời
list_vang2=[vang,vang,vang,vang,vang]# vàng dưới đất
list_bom=[bom,bom]
list_run=[run1,run2,run3,run4,run5,run6,run7,run8]

run_index=0
dem=0
jump=False 
Shop=False
start_shop=0
time_khien=0
time_nc=0
sd_nc=False
sd_khien=False
nv_y=230
nv_x=100
vang1_x=[0]*5
vang2_x=[0]*5
for i in range(5):
    vang1_x[i]=randint(400,1000)
    vang2_x[i]=randint(400,1000)
mb_x=-100
qua_x=-50
bom_x=[0]*2
bom_x[0]=randint(500,1000)
bom_x[1]=-100
bg2_x = 0
sl_vang=0
sl_khien=0
sl_thuoc=0
sl_nam_cham=0
sl_mau=100
k=3
kt_music=False

font = pygame.font.SysFont('forte', 30)#Phông chữ 
menu='trangChu' # Tạo biến menu để chuyển đổi các giao diện trong game và khởi tạo menu='trangChu'
running=True # Tạo biến running = True để chạy vòng lặp

while running:
    #check menu:
    if menu == "trangChu": #Nếu menu='trangChu' thì:
        screen.blit(bg1,(0,0)) #hiển thị giao diện đầu game
        if play_button.draw():#nếu kích chuột vào button play
            menu = 'main'# để chuyển sang giao diện chính của game để chơi game
            start_time=pygame.time.get_ticks()#Thời gian dư thừa
    
    if menu == "main": #Nếu menu='main' thì:
        if kt_music==False:
            sound_nen.play(-1)
           #sử dụng để phát nhạc nền của game và lặp lại nó liên tục
            kt_music=True
        if Shop==False:
            draw_bg()
            if(time_elapsed>110000): 
                kb_rect=screen.blit(kho_bau,(870,225))
                if nv_rect.colliderect(kb_rect):
                    sound_nen.stop() #dừng phát nhạc nền
                    menu="win"
                    sound_thang.play()
                if nv_x<950:nv_x+=k
            else: 
                bg2_x -=k
                qua_x -=k
                mb_x -=k
                for i in range(2):
                    bom_x[i] -=k
                for i in range(5):
                    vang1_x[i] -=k
                    vang2_x[i] -=k
        
            if bg2_x <= -1000:
                bg2_x=0
            if mb_x<=-100:
                mb_x=randint(2000,3000)
            if qua_x<=-50:
                qua_x=randint(3000,4000)
            for i in range(2):
                if bom_x[i] <= -100:
                    bom_x[i]=randint(1000,2000)
            for i in range(5):
                if vang1_x[i] <= -50:
                    vang1_x[i]=randint(1000,2000)
                if vang2_x[i] <= -50:
                    vang2_x[i]=randint(1000,2000)

            #Vẽ lượng máu còn lại
            screen.blit(mau,(0,0))
            draw_sl_mau()

            #Vẽ số lượng vàng đã ăn được còn lại
            screen.blit(icon_vang,(0,40))
            draw_sl_vang()

           # Sử dụng các chức năng nam cham, hoi mau, khien
            if(khien_button.draw()):
                 if(sl_khien>0):
                    sl_khien-=1
                    time_khien=pygame.time.get_ticks()
                    sd_khien=True
            if(pygame.time.get_ticks()-time_khien>=5000):
                 sd_khien=False
            draw_sl_khien()
            if sd_khien:
                khien2_x=nv_rect.centerx - khien2.get_width() // 2 
                khien2_y=nv_rect.centery - khien2.get_width() // 2 
                screen.blit(khien2,(khien2_x,khien2_y))
                
            if(nc_button.draw()):
                 if(sl_nam_cham>0):
                    sl_nam_cham-=1
                    time_nc=pygame.time.get_ticks()
                    sd_nc=True
            if(pygame.time.get_ticks()-time_nc>=5000):
                  sd_nc=False
            draw_sl_nc()
            if sd_nc:
                for i in range(5):
                    if nv_x-50<=vang1_x[i]<=nv_x+50:
                        sound_an_vang.play()
                        sl_vang+=5
                        draw_sl_vang()
                        vang1_x[i]=-50
                    if nv_x-50<=vang2_x[i]<=nv_x+50:
                        sound_an_vang.play()
                        sl_vang+=5
                        draw_sl_vang()
                        vang2_x[i]=-50
            if(thuoc_button.draw()):
                if(sl_thuoc>0 and sl_mau<100):
                    sl_thuoc-=1
                    sl_mau+=20
                    draw_sl_mau()
            draw_sl_thuoc()

            if shop_button.draw(): # Khi nhấp chuột vào shop thi mở shop nên Shop=True
                Shop=True
                time_start=start_time#Thời gian thừa tại thời điểm hiển thị shop
                start_shop=pygame.time.get_ticks() #Thời gian lúc bắt đầu mở shop là start_shop

            if 230>=nv_y>=80:
                if jump==True:
                    nv_y-=k
                    nv_rect=screen.blit(run4,(nv_x,nv_y))
                   
            else:
                    jump=False
            if nv_y < 230:
                if jump==False:
                    nv_y+=k
                    nv_rect=screen.blit(run8,(nv_x,nv_y))
                    
            if nv_y==230:
                if jump==False:
                    if run_index==8:run_index=0
                    nv_rect=screen.blit(list_run[run_index],(nv_x,nv_y))
                    if(dem==10):
                        run_index+=1
                        dem=0
                    dem+=1

            #Xử lý va cham
            
            for i in range(2):
                bom_rect=screen.blit(list_bom[i],(bom_x[i],290)) #gán giá trị hình chữ nhật bao quanh bom1 vào bom_rect để xử lý va chạm 
                bom_no_x=bom_rect.centerx - noo.get_width() // 2 
                if nv_rect.colliderect(bom_rect):
                    screen.blit(noo,(bom_no_x,240))
                    sound_no.play()
                    if sd_khien==0:
                        sl_mau=sl_mau-50
                        draw_sl_mau()
                    bom_x[i]=-100
                
            for i in range(5):
                vang1_rect=screen.blit(list_vang1[i],(vang1_x[i],165))
                vang2_rect=screen.blit(list_vang2[i],(vang2_x[i],280))  
                if nv_rect.colliderect(vang1_rect):
                    sound_an_vang.play()
                    sl_vang+=5  
                    draw_sl_vang()
                    vang1_x[i]=-50
                if nv_rect.colliderect(vang2_rect):
                    sound_an_vang.play()
                    sl_vang+=5  
                    draw_sl_vang()
                    vang2_x[i]=-50
            mb_rect=screen.blit(mb,(mb_x,90))
            mb_no_x=mb_rect.centerx - noo.get_width() // 2
            if nv_rect.colliderect(mb_rect):
                sound_no.play()
                screen.blit(noo,(mb_no_x,60))
                if sd_khien==0:
                    sl_mau=sl_mau-50
                    draw_sl_mau()
                mb_x=-100
            qua_rect=screen.blit(qua,(qua_x,150))
            if nv_rect.colliderect(qua_rect):
                i=randint(1,4)
                if i!=4: sound_qua.play()
                if i==1:
                    sl_khien+=1
                    draw_sl_khien()
                elif i==2:
                    sl_nam_cham+=1
                    draw_sl_nc()
                elif i==3:
                    sl_thuoc+=1
                    draw_sl_thuoc()
                else: 
                    sound_no.play()
                    qua_no_x=qua_rect.centerx - noo.get_width() // 2
                    screen.blit(noo,(qua_no_x,150))
                    sl_mau-=20
                    draw_sl_mau()
                qua_x=-50
                     
                 

        else: # Shop==True (mở shop)
            start_time=time_start+(pygame.time.get_ticks()-start_shop)
            screen.blit(shop,(300,0)) # Vẽ background shop
            if quit_button.draw(): # Khi nhấp vao nút quit thì đóng shop nên Shop=False
                Shop=False
                    
            screen.blit(khien_shop,(390,110))
            screen.blit(icon_vang,(385,190))
            gia_nc = font.render('50', True, (255,223,0))
            screen.blit(gia_nc,(420,190))
            if buy_button1.draw():
                if sl_vang>=50:
                    sl_khien+=1
                    sl_vang-=50
                    draw_sl_vang()

            screen.blit(thuoc_shop,(550,120))
            screen.blit(icon_vang,(555,190))
            gia_thuoc = font.render('50', True, (255,223,0))
            screen.blit(gia_thuoc,(590,190))
            if buy_button2.draw():
                if sl_vang>=50:
                    sl_thuoc+=1
                    draw_sl_thuoc()
                    sl_vang-=50 
                    draw_sl_vang() 
            
        if(sl_mau<=0): 
            sound_nen.stop() #dừng phát nhạc nền
            sound_thua.play()
            menu="lose"
    if menu == "lose": #Nếu menu='lose' thì:
        screen.blit(lose,(0,0)) #hiển thị giao diện khi thua sẽ có câu hỏi muốn chơi lại không
        if yes_button.draw(): #nếu kích chuột vào button yes là chơi lại
            menu = 'main' # để chuyển sang giao diện chính của game để chơi game
            run_index=0
            dem=0
            jump=False 
            Shop=False
            start_shop=0
            time_khien=0
            time_nc=0
            time_thuoc=0
            sd_nc=False
            sd_khien=False
            nv_y=230
            nv_x=100
            for i in range(5):
                vang1_x[i]=randint(400,1000)
                vang2_x[i]=randint(400,1000)
            mb_x=-100
            qua_x=-50
            bom_x[0]=randint(500,1000)
            bom_x[1]=-100
            bg2_x = 0
            sl_vang=0
            sl_khien=0
            sl_thuoc=0
            sl_nam_cham=0
            sl_mau=100
            k=3
            kt_music=False
            start_time=pygame.time.get_ticks()
        if no_button.draw(): #nếu kích chuột vào button no là thoát game
            running=False # Dừng vòng lặp, thoát game
    if menu=='win': #Nếu menu='win' thì:
        screen.blit(win,(0,0)) #hiển thị giao diện khi thắng
    for event in pygame.event.get():
        if event.type==pygame.QUIT: # nếu ta click chữ X  ở góc trên cùng khung hình
            running=False # Dừng vòng lặp
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if nv_y==230:
                    jump = True

    pygame.display.flip() #cập nhật nội dung của toàn bộ màn hình

     # Tính toán thời gian đã trôi qua
    time_elapsed = pygame.time.get_ticks() - start_time

    if(time_elapsed>20000):  k = 4
    if(time_elapsed>50000):  k = 5
    if(time_elapsed>80000):  k = 6
    if(time_elapsed>100000):  k = 7
    clock.tick(60) #số lần khung hình được vẽ trong một giây là FPS
pygame.quit() #thoát khỏi chương trình hoàn toàn.