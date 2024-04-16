import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")#figの下のpg_...
    kk_img = pg.image.load("fig/3.png")#練習2
    bg_img2 = pg.image.load("fig/pg_bg.jpg")#練習7
    kk_img = pg.transform.flip(kk_img, True, False)#練習2
    bg_img2 = pg.transform.flip(bg_img, True, False)#練習7
    kk_rct = kk_img.get_rect() #練習8-1
    kk_rct.center = 300, 200 #練習8-2
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        
        spx = -1
        spy = 0
        key_lst = pg.key.get_pressed()
        if key_lst[pg.K_UP]:
            spy = -1
            #print("上押された")
            #kk_rct.move_ip([0, -1])

        if key_lst[pg.K_DOWN]:
            spy = 1
            #kk_rct.move_ip([0, +1])
        if key_lst[pg.K_LEFT]:
            spx = -1
            #kk_rct.move_ip([-1, 0])
        if key_lst[pg.K_RIGHT]:
            spx = 2
            #kk_rct.move_ip([+2, 0])#演習課題1
        

        else:
            #kk_rct.move_ip([-1, 0])#演習課題1
            spx = -1

        kk_rct.move_ip(spx, spy)
            

        x = tmr%3200 #練習6 割る数は背景画像の長さによる
        screen.blit(bg_img, [-x, 0])#blitで貼り付け 練習3 #練習6
        
        screen.blit(bg_img2, [-x+1600, 0])#練習7
        screen.blit(bg_img2, [-x+3200, 0])#練習7
        screen.blit(bg_img2, [-x+4800, 0])#練習7
        # screen.blit(kk_img, [300, 200])#練習4

        
        
        screen.blit(kk_img, kk_rct)#練習8-5


        pg.display.update()
        tmr += 1        
        clock.tick(200)#練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()