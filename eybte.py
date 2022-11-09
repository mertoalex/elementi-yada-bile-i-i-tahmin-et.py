#!/usr/bin/env python
#old name: elementi yada bileşiği tahmin et.py

from random import randint as ri

puan, soru = (0,0)

evet = True
hayir = False
#they have no reasons lol

sor = evet #oyun modunu sorması için

isimmi = hayir

sembolik = ['H','He','Li','Be','B','C','N','O','F','Ne','Na','Mg','Al','Si','P','S','Cl','Ar','K','Ca','Sc','Ti','V','Cr','Mn','Fe','Co','Ni','Cu','Zn','Ga','Ge','As','Se','Br','Kr','Rb','Sr','Y','Zr','Nb','Mo','Tc','Ru','Rh','Pd','Ag','Cd','In','Sn','Sb','Te','I','Xe','Cs','Ba','Hf','Ta','W','Re','Os','Ir','Pt','Au','Hg','Tl','Pb']
sembolik_yaygin = ['hidrojen','helyum','lityum','berilyum','bor','karbon','azot / nitrojen','oksijen','flor','neon','sodyum','magnezyum','alüminyum','silisyum','fosfor','kükürt','klor','argon','potasyum','kalsiyum','skandiyum','titanyum / titan','vanadyum','krom','mangan / manganez','demir','kobalt','nikel','bakır','çinko','galyum','germanyum','arsenik','selenyum','brom','kripton','rubidyum','stronsiyum','itriyum','zirkonyum','niyobyum','molibden','teknetyum','rutenyum','rodyum','paladyum','gümüş','kadmiyum','indiyum','kalay','antimon','tellur','iyot','Ksenon','sezyum','baryum','hafniyum','tantal','tungsten','renyum','osmiyum','iridyum','platin','altın','cıva / civa','Talyum','kurşun']

bilesik = ['H2O','HCl','H2SO4','HNO3','CH3COOH','CaCO3','NaHCO3','NH3','Ca(OH)2','NaOH','KOH','CaO','NaCl']
bilesik_yaygin = ['su','tuz ruhu / hidroklorik asit','zaç yağı / sülfürik asit','kezzap / nitrik asit','asetik asit / sirke asidi / sirke ruhu','kireç taşı','yemek sodası / sodyum bikarbonat / kabartma tozu','amonyak','sönmüş kireç / kalsiyum hidroksit','sud kostik / sodyum hidroksit','potas kostik / potasyum hidroksit / potasyum hidrat','sönmemiş kireç / kalsiyum oksit','yemek tuzu / sodyum klorür / sofra tuzu / tuz']

bilesik_bitti, sembolik_bitti = (hayir, hayir)

soru_türü = "random"
soru_türü_aciklamasi ="""3 soru türü var, bu soru türleri;
random\t = altdakkilerden birini sorar (her seferinde değişir)
sembolik = sembollerden sorar (C, O, H gibi)
bileşik\t = bileşiklerden sorar (H2O gibi)
hangisini seçiyorsun?
"""

soru_siralamasi = "random"
soru_siralamasi_aciklamasi = """3 soru sıralaması var, bu soru sıralamaları;
random\t = altdakilerden birini yapar (her seferinde değişir)
yaygın\t = yaygın sorup sembolik halini cevap olarak ister ("hidroklorik asit" cevap:HCI gibi)
sembolik = sembolik sorup yaygın halini cevap olarak ister(HCI cevap:"hidroklorik asit" gibi)
hangisini seçiyorsun?
"""

def init():
	global bilesik_bitti,sembolik_bitti
	if soru_türü == "sembolik": bilesik_bitti = evet
	if soru_türü == "bileşik":  sembolik_bitti = evet

def str_to_list(string):
	return string.split(sep=None, maxsplit=0)

def soru_turu_sor():
	global soru_türü
	print(soru_türü_aciklamasi, end="")
	while evet:
		user_cevap = input("$ ").casefold()
		
		if user_cevap == "random" or user_cevap == "sembolik" or user_cevap == "bileşik":
			soru_türü = user_cevap
			break
		elif f"{user_cevap}" == '':
			print(f"bir şey yazılmadı, default olarak soru türü \"{soru_türü}\" olarak seçildi\n")
			break
		else: print(f"\"{user_cevap}\" bir soru türü değil, sadece \"random\", \"sembolik\" ve \"bileşik\" yazmanız lazım.")

def soru_siralamasi_sor():
	global soru_siralamasi, isimmi
	print(soru_siralamasi_aciklamasi, end="")
	while evet:
		user_cevap = input("$ ").casefold()
		
		if user_cevap == "random" or user_cevap == "yaygın" or user_cevap == "sembolik":
			soru_siralamasi = user_cevap
			isimmi = evet if user_cevap == "sembolik" else hayir
			break
		elif f"{user_cevap}" == '':
			print(f"bir şey yazılmadı, default olarak soru türü \"{soru_siralamasi}\" olarak seçildi\n")
			break
		else: print(f"\"{user_cevap}\" bir soru siralamasi değil, sadece \"random\", \"yaygın\" veya \"sembolik\" yazmanız lazım.")

def tahmin(first,second):
	global puan, soru, isimmi
	if soru_siralamasi == "random":
		random_int = ri(0,1)
		if random_int == 0:
			baslik,cevap,isimmi = first,second,hayir
		if random_int == 1:
			baslik,cevap,isimmi = second,first,evet
	elif soru_siralamasi == "yaygın":
		baslik,cevap = first,second
	elif soru_siralamasi == "sembolik":
		baslik,cevap = second,first
	else:
		print(f"\"{soru_siralamasi}\" diye bir soru sıralaması bulunamadı. geçerli soru sıralamaları: random, yaygın, sembolik (hepsinin aciklamasi kaynak kodda)")
		exit(1)
	
	cevap = cevap.split(' / ') if ' / ' in cevap else cevap 
	cevap = str_to_list(cevap) if not isinstance(cevap,list) else cevap 

	soru += 1
	user_cevap = input(f"puanın: {puan}\n{soru}) {baslik}\n$ ") or '**BOŞ GİRİLDİ**' # ({cevap} | {isimmi}) for debugging
	user_cevap = user_cevap.casefold() if isimmi else user_cevap
	
	if user_cevap in cevap:
		print("afferim, doğru cevap! (+10 puan)") #for debugging: f"++ ({user_cevap} in {cevap} = {str(user_cevap in cevap)})")
		puan += 10
		return evet
	elif user_cevap.casefold() in ["exit","çık","çıkış"]:
		print("oynadığın için teşekkür ederim, görüşürüz. 👋")
		exit(0)
	elif puan <= 0:
		print("üzgünüm, yanlış cevap.") #for debugging: f"O  (not {user_cevap} in {cevap} = {str(user_cevap in cevap)})")
		return hayir
	else:
		print("üzgünüm, yanlış cevap (-5 puan)") #for debugging: f"Br (not {user_cevap} in {cevap} = {str(user_cevap in cevap)})")
		puan -= 5
		return hayir

def oyunu_baslat():
	global bilesik_bitti,sembolik_bitti
	while evet:
		if len(sembolik_yaygin) <= 0: sembolik_bitti = evet
		if len(bilesik_yaygin) <= 0: bilesik_bitti = evet
		
		if soru_türü == "random":
			random_int = ri(0,1)
		
			if not bilesik_bitti and random_int == 0:
				sor = ri(0,len(bilesik_yaygin)-1)
				if tahmin(bilesik_yaygin[sor],bilesik[sor]):
					bilesik_yaygin.pop(sor)
					bilesik.pop(sor)

			if not sembolik_bitti and random_int == 1:
				sor = ri(0,len(sembolik_yaygin)-1)
				if tahmin(sembolik_yaygin[sor],sembolik[sor]):
					sembolik_yaygin.pop(sor)
					sembolik.pop(sor)

		if not bilesik_bitti and soru_türü == "bileşik":
			sor = ri(0,len(bilesik_yaygin)-1)
			if tahmin(bilesik_yaygin[sor],bilesik[sor]):
				bilesik_yaygin.pop(sor)
				bilesik.pop(sor)
		
		if not sembolik_bitti and soru_türü == "sembolik":
			sor = ri(0,len(sembolik_yaygin)-1)
			if tahmin(sembolik_yaygin[sor],sembolik[sor]):
				sembolik_yaygin.pop(sor)
				sembolik.pop(sor)
		
		if bilesik_bitti and sembolik_bitti:
			print(f"puanın: {puan}\noyunu oynadığınız için teşekkürler, umarım ezberlemenizde yardımcı olmuşumdur ve umarım eğlenmişsinizdir.")
			exit(0)

if __name__ == '__main__':
	if sor:
		soru_turu_sor()
		soru_siralamasi_sor()
	init()

	oyunu_baslat()
