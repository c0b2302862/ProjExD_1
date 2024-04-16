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
    bg_img2 = pg.transform.flip(bg_img2, True, False)#練習7
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = tmr%3200 #練習6 割る数は背景画像の長さによる
        screen.blit(bg_img, [-x, 0])#blitで貼り付け 練習3 #練習6
        
        screen.blit(bg_img2, [-x+1600, 0])#練習7
        screen.blit(bg_img2, [-x+3200, 0])#練習7
        screen.blit(bg_img2, [-x+4800, 0])#練習7
        screen.blit(kk_img, [300, 200])#練習4

        pg.display.update()
        tmr += 1        
        clock.tick(500)#練習5


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()