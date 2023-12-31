import pygame 
import random
x="-1" 
puan=0
combo=0

pygame.init() #ekran yazı falan ayarları
background_colour = (200, 200, 200)
text_font = pygame.font.SysFont("Arial",50)
screen = pygame.display.set_mode((1200,800)) 
pygame.display.set_caption("Arz Arrow Game") 

arrow_type=['←','→','↑','↓'] #yönler
yonler=["a","d","w","s"]
def draw_text(text,font,text_col, x, y): #yazı yazdırma fonksiyonu
    img = font.render(text, True, text_col)  
    screen.blit(img, (x ,y))

def yenisayi(): #rastgele sayı üreten fonksiyon (bununla rastgele ok yönü de belirlicez)
    sayi=random.randint(0,3)
    while yonler[sayi]==x: #önceki gelen okla aynı ise değiştir 
        return yenisayi()
    return sayi
sayi= yenisayi() #rastgele bi sayı belirle

running = True 
while running: #çalışırken
    screen.fill(background_colour) 
    draw_text(arrow_type[sayi]+"     puan="+str(puan)+"  combo="+str(combo), text_font,(0, 0, 0),220,150) #ekrana ok puan ve comboyu yazdır
    pygame.display.flip()
    for event in pygame.event.get(): 
        if event.type == pygame.KEYUP: #tuşa basıldığında
            if event.key == pygame.K_LEFT:
                x = "a"
            elif event.key == pygame.K_RIGHT:
                x = "d"
            elif event.key == pygame.K_UP:
                x = "w"
            elif event.key == pygame.K_DOWN:
                x = "s"
            if x != "-1" and x == yonler[sayi]: #basılan yön tuşu okun yönüne eşitse
                print(x)
                sayi= yenisayi() #yeni ok yönü belirle
                combo+=1 
                puan+=1*combo #puanı ve comboyu arttır
            else: #yanlış bilirsen
                combo=0 #comboyu resetle
        if event.type == pygame.QUIT: #çıkış 
            running = False
pygame.quit()
