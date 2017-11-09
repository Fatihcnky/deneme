# -*- coding: cp1254 -*-

from __future__ import division

while True:

    def toplama_islemi():
        girdi1t=int(raw_input("Ilk sayiyi girin: "))
        girdi2t=int(raw_input("Ikinci sayiyi girin: "))
        sonuct=girdi1t+girdi2t
        print "Sonuc :" , sonuct
        print
    def cikarma_islemi():
        girdi1c=int(raw_input("Ilk sayiyi girin: "))
        girdi2c=int(raw_input("Ikinci sayiyi girin: "))
        sonucc=girdi1c-girdi2c
        print "Sonuc :" , sonucc
        print
    def carpma_islemi():
        girdi1ca=int(raw_input("Ilk sayiyi girin: "))
        girdi2ca=int(raw_input("Ikinci sayiyi girin: "))
        sonucca=girdi1ca*girdi2ca
        print "Sonuc :" , sonucca
        print
    def bolme_islemi():
        girdi1bo=int(raw_input("Ilk sayiyi girin: "))
        girdi2bo=int(raw_input("Ikinci sayiyi girin: "))
        sonucbo=girdi1bo/girdi2bo
        print "Sonuc :" , sonucbo
        print
    def kare_alma():
        girdi1ka=int(raw_input("Karesini almak istediginiz sayiyi girin: "))
        sonucka=girdi1ka ** 2
        print "Sonuc :", sonucka
    def kup_alma():
        girdi1ku=int(raw_input("Kubunu almak istediginiz sayiyi girin: "))
        sonucku=girdi1ku ** 3
        print "Sonuc :", sonucku
    def kare_hacim():
        kare_hacimx=int(raw_input("Karenin bir kenarinin uzunlugunu girin: "))
        sonuc_kare_hacim=kare_hacimx**3
        print "Sonuc :", sonuc_kare_hacim
    def kup_hacim():
        kup_hacimx=int(raw_input("Kubun bir kenar uzunlugunu girin: "))
        sonuc_kup_hacim=(kup_hacimx**3) * 4
        print "Sonuc :", sonuc_kup_hacim
    def dikdortgen_alan():
    	dikdortgen_alan1x=int(raw_input("Dikdortgenin uzun kenar uzunlugunu girin: "))
    	dikdortgen_alan2x=int(raw_input("Dikdortgenin kisa kenar uzunlugunu girin: "))
        sonuc_dikdortgen_alan=dikdortgen_alan1x*dikdortgen_alan2x
    	print "Sonuc :" , sonuc_dikdortgen_alan
    def leblebi():
    	leblebi=int(raw_input("Leblebi"))
    	sonuc_leblebi=leblebi
    	print "Sonuc :" , sonuc_leblebi
    print ("Toplama Islemi (1)")
    print ("Cikarma Islemi (2)")
    print ("Carpma Islemi (3)")
    print ("Bolme Islemi (4)")
    print ("Kare alma islemi (5)")
    print ("Kup alma islemi (6)")
    print ("Hacim bulma islemi (7)")
    print ("Dikdortgen alan bulma islemi (8)")
    print ("leblebi icin (9)")
    print ("Programdan cikmak icin (0)")
    print ("--------------------------")
    
    try:
        islemno=int(raw_input("Islem numarasini girin: "))

        if islemno == 1:
            toplama_islemi()
        elif islemno == 2:
            cikarma_islemi()
        elif islemno == 3:
            carpma_islemi()
        elif islemno == 4:
            bolme_islemi()
        elif islemno == 5:
            kare_alma()
        elif islemno == 6:
            kup_alma()
        elif islemno == 7:
            print ("Karenin hacmi (1)")
            print ("Kubun hacmi (2)")
            print ("------------------")
            islemno2=int(raw_input("Islem numarasini girin: "))
            if islemno2 == 1:
                kare_hacim()
            elif islemno2 == 2:
                kup_hacim()
            else:
                print ("Islem numarasi gecersiz")
                print
        elif islemno == 8:
        	dikdortgen_alan()
        elif islemno == 9:
        	leblebi()
        elif islemno == 0:
            break
        else:
            print ("Islem numarasi gecersiz")
            print
    except(ZeroDivisionError, ValueError):
        print ("Hatali bir deger girdiniz.")
        print

