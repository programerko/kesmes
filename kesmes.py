import pygame, sys
from pygame.locals import *
import pyganim
import random


if __name__ == "__main__":

    pygame.init()
    

    #boje
    BLACK  = (  0,   0,   0)
    WHITE  = (255, 255, 255)
    RED    = (255,   0,   0)
    DRED   = (150,   0,   0)
    GREEN  = (  0, 255,   0)
    BLUE   = (  0,   0, 255)
    DGREEN = (  0, 200, 120)
    YELLOW = (200, 200,   0)
    DYELLOW= (100, 100,   0)

    #prozor
    w=1200 #sirina
    h=650 #visina
    
    PROZOR = pygame.display.set_mode((w,h),pygame.FULLSCREEN)
    back = pygame.image.load('back.jpg').convert()
    pygame.display.set_caption('KE$-ME$')
    

    #KPS
    sat = pygame.time.Clock()
    #FPS = 30

    #ZVUK
   

    #   PROMENLJIVE

    
    
    #   KLASE

    class Var(object):

        FPS = 30
        nivo = 1


        VREME = 0
        pare = 60
        spec_poeni = 0
        vreme = 0
        klik1 = pygame.mixer.Sound('kupi.wav')
        hit = pygame.mixer.Sound('swish_4.wav')
        hit1 = pygame.mixer.Sound('swish_2.wav')

        vreme2 = 0
        cekanje_para = 100
        plata = 1
        
        lista_ljudi = []
        vreme3 = 0
        nbr = 0

        #VREME
        sekunda = 0
        msekund = 0
        vsekund = 0
        mminut = 0
        vminut= 0
        
        def konvrt(slika):
            slika_covek = pygame.image.load(slika)
            TR = slika_covek.get_at((0, 0))
            slika_covek.set_colorkey(TR,RLEACCEL)
            return slika_covek.convert()
        
    class Baza(pygame.sprite.Sprite):

        def __init__(self,x,slika):
            super(Baza, self).__init__()

            slika_baze = pygame.image.load('baza1.png')
            slika_baze.set_colorkey(WHITE,RLEACCEL)
            self.image = slika_baze.convert()
            self.image = slika
            self.rect = self.image.get_rect()

            self.rect.x = x
            self.rect.bottom = h-100
            self.php = 1450
            self.hp = 1450

        def update(self):

            self.bar = pygame.draw.rect(PROZOR,RED,(self.rect.x +5,h-20,145,15))
            self.dbar = pygame.draw.rect(PROZOR,GREEN,(self.rect.x+5,h-20,self.hp/10,15))

        def promena_hp(self,hp):

            self.hp -= hp
                
    class Pod(pygame.sprite.Sprite):

        def __init__(self,y,slika,visina = 25):
            super(Pod, self).__init__()

            self.visina = visina
            self.image = pygame.Surface((w,self.visina))
            
            self.image = slika

            self.rect = self.image.get_rect()
            self.visina = visina
            self.y = y
            self.rect.x = 0
            self.rect.y = self.y

    class Zgrade(pygame.sprite.Sprite):

        x = 155
        y = h-130
        def __init__(self,slika):
            super(Zgrade,self).__init__()

            self.image = pygame.Surface((150,100))
            self.rect = self.image.get_rect()
            self.rect.x = Zgrade.x
            self.rect.bottom = h-70
            
            self.image = Var.konvrt(slika)
            Zgrade.x +=65
                                        
        def stvaranje_banke():
            
            if Var.pare >= 55 and Var.vreme > 10:
                Var.vreme = 0
                Var.pare -= 50
                Var.plata += 1
                banka = str(Var.nbr)
                banka = Zgrade('bank.png')
                Var.nbr += 1
                zgrade.add(banka)

        def stvaranje_kuce():
            
            if Var.pare >= 25 and Var.vreme > 10:
                Var.vreme = 0
                Var.pare -= 25
                Ljudi.dozvoljen_broj += 5
                kuca = str(Var.nbr)
                kuca = Zgrade('bank.png')
                Var.nbr += 1
                zgrade.add(kuca) 

        
    class Ljudi(pygame.sprite.Sprite):
        
        hover_tekst = 'BRZINA - ;NAPAD - ;'
        hover_tekst2 =  'BRZ.NAPADA + ;'
        hover_tekst3 = 'HP - ;'

        ahover_tekst = 'BRZINA -- ;NAPAD + ;'
        ahover_tekst2 =  'BRZINA NAPADA --;'
        ahover_tekst3 = 'HP ++ ;'

        bhover_tekst = 'BRZINA + ;NAPAD + ;'
        bhover_tekst2 =  'BRZ.NAPADA - ;'
        bhover_tekst3 = 'HP + ;'

        vhover_tekst = 'BRZINA - ;NAPAD ++ ;'
        vhover_tekst2 =  'BRZ.NAPADA - ;'
        vhover_tekst3 = 'HP ++ ;'

        broj = 0
        dozvoljen_broj = 5
        def __init__(self,slika_hod,slika_udarac,brzina,napad,brzina_napada,hp,w,s):

            super(Ljudi, self).__init__()
            self.slika_hod = Var.konvrt(slika_hod)
            self.slika_udarac = Var.konvrt(slika_udarac)
            self.brzina = brzina
            self.napad = napad
            self.brzina_napada = brzina_napada
            self.hpp = hp
            self.hp = hp
            self.w = w
            self.h = s

            self.image = pygame.Surface((self.w,self.h))
            self.image = self.slika_hod

            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(-110,-70)
            self.rect.bottom = random.randrange(h-90,h-65)

            self.time_to_hit = 10
            
            
        def update(self):

            self.lista = pygame.sprite.spritecollide(self,nefigure,0)
            self.lista2 = pygame.sprite.spritecollide(self,baza2,0)

            
            self.time_to_hit += 1
            if pygame.sprite.spritecollideany(self,nefigure):
                if self.time_to_hit > self.brzina_napada:
                    Var.hit.play()
                    self.lista[0].promena_hp(self.napad)
                    self.time_to_hit = 0
                if self.time_to_hit <10:
                    self.image = self.slika_udarac
                else:
                    self.image = self.slika_hod
            elif pygame.sprite.spritecollideany(self,baza2):
                if self.time_to_hit > self.brzina_napada:
                    Var.hit.play()
                    self.lista2[0].promena_hp(self.napad)
                    self.time_to_hit = 0
                if self.time_to_hit <10:
                    self.image = self.slika_udarac
                else:
                    self.image = self.slika_hod
            else:
                
                self.rect.x += self.brzina
                self.image = self.slika_hod

        def promena_hp(self,hp):

            self.hp -= hp
            if self.hp < 1 :
                Ljudi.broj -=1
                if Ljudi.broj < 0:
                    Ljudi.broj = 0
                self.kill()

        def spec_jedinica(izbor):

            cena = 100
            if Var.vreme > 20 and Var.spec_poeni >= cena:
                for i in range(6):
                    covek = str(Var.nbr)
                    covek = Ljudi('3072.png','3072a.png',2,5,30,30,65,138)
                    figure.add(covek)
                    Var.nbr += 1
                Var.vreme = 0
                Var.spec_poeni -= cena
                Var.klik1.play()
                Var.nbr += 1
    
        def stvaranje_coveka(izbor):

            if izbor == 1:
                cena = 5
                if Var.vreme > 12 and Var.pare >= cena and Ljudi.dozvoljen_broj > Ljudi.broj:
                    covek = str(Var.nbr)
                    covek = Ljudi('3072.png','3072a.png',2,5,30,30,65,138)
                    figure.add(covek)
                        
                    Var.vreme = 0
                    Var.pare -= cena
                    Var.klik1.play()
                    Var.nbr += 1
                    Ljudi.broj += 1

            elif izbor == 2:
                cena = 15
                if Var.vreme > 45 and Var.pare >= cena and Ljudi.dozvoljen_broj > Ljudi.broj:
                    covek = str(Var.nbr)
                    covek = Ljudi('3072.png','3072a.png',1,5,75,100,65,138)
                    figure.add(covek)
                        
                    Var.vreme = 0
                    Var.pare -= cena
                    Var.klik1.play()
                    Var.nbr += 1
                    Ljudi.broj += 1

            elif izbor == 3:
                cena = 15
                if Var.vreme > 45 and Var.pare >= cena and Ljudi.dozvoljen_broj > Ljudi.broj:
                    covek = str(Var.nbr)
                    covek = Ljudi('3072.png','3072a.png',3,7,50,50,65,138)
                    figure.add(covek)
                        
                    Var.vreme = 0
                    Var.pare -= cena
                    Var.klik1.play()
                    Var.nbr += 1
                    Ljudi.broj += 1

            elif izbor == 4:
                cena = 25
                if Var.vreme > 45 and Var.pare >= cena and Ljudi.dozvoljen_broj > Ljudi.broj:
                    covek = str(Var.nbr)
                    covek = Ljudi('3072.png','3072a.png',1,15,50,100,65,138)
                    figure.add(covek)
                        
                    Var.vreme = 0
                    Var.pare -= cena
                    Var.klik1.play()
                    Var.nbr += 1
                    Ljudi.broj += 1
                
    class Neljudi(pygame.sprite.Sprite):

        
        def __init__(self,slika_hod,slika_udarac,brzina,napad,brzina_napada,hp,v,s):
            super(Neljudi,self).__init__()
            self.slika_hod = Var.konvrt(slika_hod)
            self.slika_udarac = Var.konvrt(slika_udarac)
            self.brzina = brzina
            self.napad = napad
            self.brzina_napada = brzina_napada
            self.hp = hp
            self.w = v
            self.h = s

            self.image = pygame.Surface((self.w,self.h))
            self.image = self.slika_hod

            self.rect = self.image.get_rect()
            self.rect.x = random.randrange(w,w+100)
            self.rect.bottom = random.randrange(h-90,h-65)

            self.time_to_hit = 10
           
        def update(self):

            self.lista = pygame.sprite.spritecollide(self,figure,0)
            self.lista2 = pygame.sprite.spritecollide(self,baza1,0)
            self.time_to_hit += 1
            if pygame.sprite.spritecollideany(self,figure):
                if self.time_to_hit > self.brzina_napada:
                    Var.hit1.play()
                    self.lista[0].promena_hp(self.napad)
                    self.time_to_hit = 0
                if self.time_to_hit <10:
                    self.image = self.slika_udarac
                else:
                    self.image = self.slika_hod
            elif pygame.sprite.spritecollideany(self,baza1):
                if self.time_to_hit > self.brzina_napada:
                    Var.hit1.play()
                    self.lista2[0].promena_hp(self.napad)
                    self.time_to_hit = 0
                if self.time_to_hit <10:
                    self.image = self.slika_udarac
                else:
                    self.image = self.slika_hod
            else:
                self.rect.x -= self.brzina
                self.image = self.slika_hod
                
        def promena_hp(self,hp):

            self.hp -= hp
            if self.hp < 1 :
                self.kill()
                Var.spec_poeni += 10
                
        def napad_necoveka(nivo):

            if nivo == 1:
                
                while Var.vminut == 0 and Var.mminut == 0 and Var.vsekund < 5 and (Var.msekund == 2 or Var.msekund == 8) and Var.vreme3 > 30:
                    Neljudi.stvaranje_necoveka(1)
                    Var.vreme3 = 0
                
                if Var.vminut == 0 and Var.mminut == 0 and Var.vsekund == 5 and Var.msekund == 0 and Var.vreme3 > 30:
                    for i in range(5):
                        Neljudi.stvaranje_necoveka(1)
                    Var.vreme3 = 0

                if Var.vminut == 0 and Var.mminut == 1 and Var.vsekund == 2 and Var.msekund == 0 and Var.vreme3 > 30:
                    for i in range(5):
                        Neljudi.stvaranje_necoveka(1)
                    Var.vreme3 = 0

                while Var.vminut == 0 and (Var.mminut == 1 or Var.mminut == 2) and Var.vsekund > 2 and (Var.msekund == 2 or Var.msekund == 8) and Var.vreme3 > 30:
                    Neljudi.stvaranje_necoveka(1)
                    Var.vreme3 = 0

                if Var.vminut == 0 and Var.mminut == 2 and Var.vsekund  < 2 and Var.msekund == 0 and Var.vreme3 > 30:
                    Neljudi.stvaranje_necoveka(1)
                    Neljudi.stvaranje_necoveka(2)
                    Var.vreme3 = 0

                if Var.vminut == 0 and Var.mminut == 2 and Var.vsekund == 3 and Var.msekund == 0 and Var.vreme3 > 30:
                    for i in range(9):
                        Neljudi.stvaranje_necoveka(1)
                    Var.vreme3 = 0

                while Var.vminut == 0 and Var.mminut == 2 and Var.vsekund > 3 and (Var.msekund == 2 or Var.msekund == 8) and Var.vreme3 > 30:
                    Neljudi.stvaranje_necoveka(random.randrange(1,3))
                    Neljudi.stvaranje_necoveka(1)
                    Var.vreme3 = 0

                if Var.vminut == 0 and Var.mminut == 3 and Var.vsekund == 0 and Var.msekund == 0 and Var.vreme3 > 30:
                    for i in range(6):
                        Neljudi.stvaranje_necoveka(1)
                    Var.vreme3 = 0

                if Var.vminut == 0 and Var.mminut == 3 and Var.vsekund > 1 and Var.msekund == 0 and Var.vreme3 > 30:
                    for i in range(4):
                        Neljudi.stvaranje_necoveka(1)
                    Neljudi.stvaranje_necoveka(2)
                    Var.vreme3 = 0

                while Var.vminut == 0 and Var.mminut == 3 and Var.vsekund > 1 and (Var.msekund == 2 or Var.msekund == 8) and Var.vreme3 > 30:
                    Neljudi.stvaranje_necoveka(random.randrange(1,3))
                    Neljudi.stvaranje_necoveka(1)
                    Var.vreme3 = 0
                
            
        def stvaranje_necoveka(izbor):

            if izbor == 1:
                necovek = str(Var.nbr)
                necovek = Neljudi('3071.png','3071a.png',2,5,30,30,65,138)
                nefigure.add(necovek)
                    
                Var.nbr += 1
            elif izbor == 2:
                necovek = str(Var.nbr)
                necovek = Neljudi('3071.png','3071a.png',1,10,50,150,65,138)
                nefigure.add(necovek)
                    
                Var.nbr += 1
            elif izbor == 3:
                necovek = str(Var.nbr)
                necovek = Neljudi('3071.png','3071a.png',3.5,25,80,15,65,138)
                nefigure.add(necovek)
                    
                Var.nbr += 1
        
    class Dugme():

        def __init__(self,x,y,w,h,ac,ic,funkcija,poruka = None,
                     slika = None,samoslika = False,hover = None,
                     hover2 = None, hover3 = None,velicinaf = 15 ,bojaslova = BLACK,
                     parametar = None):
 
            self.x = x
            self.y = y
            self.w = w
            self.h = h
            self.ac = ac
            self.ic = ic
            self.f = funkcija
            self.poruka = poruka
            self.slika = slika
            if slika != None:
                self.slika = Var.konvrt(self.slika)
            self.samoslika = samoslika
            self.hover = hover
            self.hover2 = hover2
            self.hover3 = hover3
            self.velicinaf = velicinaf
            self.parametar = parametar
            self.bojas = bojaslova
            
        def update(self):
                
            mx,my = pygame.mouse.get_pos()
            pygame.draw.rect(PROZOR, self.ic,[self.x,self.y,self.w,self.h])
            if self.x<mx<self.x+self.w and self.y<my<self.y+self.h:
                klik = pygame.mouse.get_pressed()
                pygame.draw.rect(PROZOR, self.ac,[self.x,self.y,self.w,self.h])
                if self.hover != None:
                    tekst(self.hover,self.x,self.y+55,RED,10,bold=1)
                if self.hover2 != None:
                    tekst(self.hover2,self.x,self.y+68,RED,10,bold=1)
                if self.hover3 != None:
                    tekst(self.hover3,self.x,self.y+81,RED,10,bold=1)
                if klik[0] == 1 and self.parametar != None :
                    self.f(self.parametar)
                elif klik[0] == 1 and self.parametar == None :
                    self.f()
                    
            if self.poruka != None:
                tekst(self.poruka,self.x,self.y,self.bojas,self.velicinaf)
            if self.slika != None and self.samoslika == False:
                PROZOR.blit(self.slika,(self.x+self.w-38,self.y))
            elif self.samoslika == True:
                PROZOR.blit(self.slika,(self.x,self.y))
                            
    def cas():
        Var.sekunda += 1
        if Var.sekunda >= 30:
            Var.sekunda = 0
            Var.msekund +=1
            if Var.msekund > 9:
                Var.msekund = 0
                Var.vsekund += 1
                if Var.vsekund > 5:
                    Var.vsekund = 0
                    Var.mminut += 1
                    if Var.mminut > 9:
                        Var.mminut = 0
                        Var.vminut +=1
        tekst(str(Var.vminut)+str(Var.mminut)+':'+str(Var.vsekund)+str(Var.msekund),w/2-20,h-40,WHITE,20,1)
            

    def tekst(tks,x,y,color = DGREEN,velicina = 30,bold = False):
           
        font = pygame.font.SysFont("Verdana",velicina,bold)
        text = font.render(str(tks),1,color)
        PROZOR.blit(text,(x,y))

#    def text(x,y,poruka,velicina,
    def pauza():
        if Var.vreme > 10:
            Var.vreme = 0
            sat = pygame.time.Clock()
            p_dugme.f = nepauza
            while 1:
                for event in pygame.event.get():

                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                sat.tick(15)
                PROZOR.blit(back,(0,0))
            
                
                grupa.draw(PROZOR)
                
                
                Var.vreme += 1
                p_dugme.update()
                x_dugme.update()
                tekst('$'+str(Var.pare),15,3)
                tekst('PAUZA',w/2-100,h/2-15,BLACK)
                pygame.display.update()

    def dkraj():
        pygame.display.quit()
        pygame.quit()
        sys.exit()
    def nastavi():
        if Var.VREME > 0:
            lobi()
        else:
            mainloop()
    def izlaz():
        kraj = 1
        
            
        ne_dugme = Dugme(w/2-100,h/2-15,70,50,GREEN,DGREEN,nastavi,'NE!',velicinaf = 40)
        da_dugme = Dugme(w/2+40,h/2,30,25,RED,DRED,dkraj,'da',velicinaf = 20)
        meni_dugme = Dugme(w/2-40,h/2+65,70,35,YELLOW,DYELLOW,lobi,'meni',velicinaf = 27)
        if Var.VREME == 0:
            tekstovi()
        while kraj:
            
            for event in pygame.event.get():
                pass
                
            sat.tick(15)
            #
            pygame.draw.rect(PROZOR,WHITE,(w/2-152,h/2-102,304,204))
            pygame.draw.rect(PROZOR,BLACK,(w/2-150,h/2-100,300,200))
            tekst("Napolje?!",w/2-90,h/2-70,WHITE,30,1)
            
            da_dugme.update()
         
            ne_dugme.update()
            meni_dugme.update()
            
            
            pygame.display.update()
        
    def nepauza():
        if Var.vreme > 10:
            Var.vreme = 0
            p_dugme.f = pauza
            mainloop()

    def restart():
        
        PROZOR.blit(back,(0,0))
        grupa.draw(PROZOR)
        baza1.draw(PROZOR)
        baza2.draw(PROZOR)
        figure.draw(PROZOR)
        zgrade.draw(PROZOR)
        Var.pare = 60
        Var.nbr = 1
        Var.cekanje_para = 100
        Var.plata = 1
        Var.spec_poeni = 0

        Var.vminut = 0
        Var.mminut = 0
        Var.vsekund = 0
        Var.msekund = 0
        
        Zgrade.x = 150
        bazacoveka.hp = bazacoveka.php
        bazanecoveka.hp = bazanecoveka.php

        Ljudi.broj = 0
        Ljudi.dozvoljen_broj = 5

        zgrade.empty()
        figure.empty()
        nefigure.empty()

    def mfps():
        
        if Var.vreme > 10:
            Var.vreme = 0
            if Var.FPS == 30:
                Var.FPS = 60
            else:
                Var.FPS = 30            
        
    def tekstovi():
        tekst('$'+str(Var.pare),15,3)
        tekst(str(Ljudi.broj)+'/'+str(Ljudi.dozvoljen_broj),210,h-40,WHITE,20,1)
        PROZOR.blit(slika_coveka,(180,h-40))
        tekst(str(bazacoveka.hp)+'/'+str(bazacoveka.php),50,h-20,BLACK,10)
        tekst('poeni: ',310,h-40,WHITE,15,1)
        tekst(str(Var.spec_poeni),370,h-40,WHITE,18,1)
        cas()
    
    def update():

        Neljudi.napad_necoveka(1)
        Var.vreme += 1
        Var.vreme2 += 1
        Var.vreme3 += 1
        
        if Var.vreme2 >= Var.cekanje_para:
            Var.pare += Var.plata
            Var.vreme2 = 0

        
        if bazacoveka.hp < 1:
            sat = pygame.time.Clock()
            restart()
            Var.VREME = 1
            while 1:
                for event in pygame.event.get():

                    pass
                sat.tick(15)
                r_dugme.update()
                x_dugme.update()
                
                tekst('GEJM OUVR!',w/2-100,h/2-15,BLACK)
                pygame.display.update()

        if bazanecoveka.hp < 1:
            sat = pygame.time.Clock()
            restart()
            Var.VREME = 1
            while 1:
                for event in pygame.event.get():

                    pass
                sat.tick(15)
                r_dugme.update()
             
                x_dugme.update()
                
                tekst('BRAVO TI GA BRAVO!',w/2-200,h/2-15,BLACK,velicina = 30,bold = 1)
                
                pygame.display.update()
                
    ##OBJEKTI
    #dugmad
    dugme_ljudi = Dugme(120,3,80,44,GREEN,DGREEN,Ljudi.stvaranje_coveka,'$5','3072d.png',
                        hover = Ljudi.hover_tekst,hover2 = Ljudi.hover_tekst2,hover3 =Ljudi.hover_tekst3,parametar = 1)

    dugme_ljudi2 = Dugme(220,3,80,44,GREEN,DGREEN,Ljudi.stvaranje_coveka,'$15','3072d.png',
                         hover = Ljudi.ahover_tekst,hover2 = Ljudi.ahover_tekst2,hover3 =Ljudi.ahover_tekst3,parametar =2)
    dugme_ljudi3 = Dugme(320,3,80,44,GREEN,DGREEN,Ljudi.stvaranje_coveka,'$15','3072d.png',
                         hover = Ljudi.bhover_tekst,hover2 = Ljudi.bhover_tekst2,hover3 =Ljudi.bhover_tekst3,parametar =3)
    dugme_ljudi4 = Dugme(420,3,80,44,GREEN,DGREEN,Ljudi.stvaranje_coveka,'$25','3072d.png',
                         hover = Ljudi.vhover_tekst,hover2 = Ljudi.vhover_tekst2,hover3 =Ljudi.vhover_tekst3,parametar =4)
    dugme_spec1 = Dugme(720,h-48,80,44,GREEN,DGREEN,Ljudi.spec_jedinica,'100p','3072d.png',
                         hover = 'OPASAN!')
    
    dugme_banka = Dugme(720,3,80,44,GREEN,DGREEN,Zgrade.stvaranje_banke,'$55',)
    dugme_kuca = Dugme(820,3,80,44,GREEN,DGREEN,Zgrade.stvaranje_kuce,'$25',)
    x_dugme = Dugme(x=w-55,y=0,w=50,h=50,ac=RED,ic=BLACK,funkcija=izlaz,poruka = None,slika = 'x.png',samoslika = True)
    rew_dugme = Dugme(x=w-205,y=0,w=72,h=50,ac=RED,ic=BLACK,funkcija=mfps,poruka = None,slika = 'premotaj.png',samoslika = True)

    p_dugme = Dugme(w-125,0,50,50,RED,BLACK,pauza,slika = 'pauza.png',samoslika = True)
    ##SLIKE
    slika_coveka = Var.konvrt('3072d.png')
    slika_baze = Var.konvrt('baza1.png')
    slika_baze2 = Var.konvrt('baza2.png')  
    zaglavlje = pygame.image.load('heder.jpg')
    rampa = pygame.image.load('ramp.jpg')
    
    ##SPRAJTOVI
    grupa = pygame.sprite.Group()
    bazacoveka = Baza(0,slika_baze)
    baza1 = pygame.sprite.Group()
    baza1.add(bazacoveka)
    bazanecoveka = Baza(w-150,slika_baze2)
    baza2 = pygame.sprite.Group()
    baza2.add(bazanecoveka)

    
    podloga = Pod(h-100,rampa)
    heder = Pod(0,zaglavlje,50)
    futer = Pod(h-50,zaglavlje,50)
    
    grupa.add(podloga,heder,futer)
    
    zgrade = pygame.sprite.Group()
    figure = pygame.sprite.Group()
    nefigure = pygame.sprite.Group()

    def mainloop():
        Var.VREME = 0
        
        while True: # main game loop
            for event in pygame.event.get():
                pass
            
            
            PROZOR.blit(back,(0,0))
            
            sat.tick(Var.FPS)
            update()            
            
            grupa.draw(PROZOR)
            zgrade.draw(PROZOR)
            nefigure.update()
            figure.update()
            baza1.update()
            baza2.update()
            zgrade.update()
            baza1.draw(PROZOR)
            baza2.draw(PROZOR)
            figure.draw(PROZOR)
            nefigure.draw(PROZOR)
            

            dugme_ljudi.update()
            dugme_ljudi2.update()
            dugme_ljudi3.update()
            dugme_ljudi4.update()

            dugme_spec1.update()

            dugme_banka.update()
            dugme_kuca.update()
            rew_dugme.update()
            p_dugme.update()
            x_dugme.update()

            tekstovi()
            
            
            
            pygame.display.update()
            


        pygame.quit()

    def uputstva():
        tekst('NEMA!',w/2-w/3+180,h/2-h/3,WHITE,30)
    prvo_dugme = Dugme(w/2-25,h/2-25,50,50,WHITE,RED,mainloop)
    uputstva_dugme = Dugme(w/2-w/3,h/2-h/3,165,40,YELLOW,DYELLOW,uputstva,poruka = 'UPUTSTVA',velicinaf = 30)
    kover = pygame.image.load('kover.png')
    def lobi():
        restart()
        PROZOR.fill(BLACK)
        PROZOR.blit(kover,(w/3,h-300))
        while True: # intro loop
            for event in pygame.event.get():
                pass
            Var.VREME += 1
            
            prvo_dugme.update()
            x_dugme.update()
            uputstva_dugme.update()
            sat.tick(Var.FPS)
            pygame.display.update()
    r_dugme = Dugme(x=w/2-25,y=0,w=50,h=50,ac=RED,ic=BLACK,funkcija=mainloop,poruka = None,slika = 'restart.png',samoslika = True)

    lobi()
  

