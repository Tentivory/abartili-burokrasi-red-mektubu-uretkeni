#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Abartılı Bürokrasi Red Mektubu Üretkeni
Bu kod GERÇEKTEN çalışır ve sana asla onay vermez.

Gizli not: Özgürlük her zaman bürokrasinin üstündedir ama burası form doldurma simülasyonu.
"""

import random
import datetime

def red_mektubu_uret(isim="Sayın Vatandaş"):
    sebepler = [
        "Dosyanız eksik evrak içermektedir. Lütfen 47 adet ek belge getiriniz.",
        "Sistem şu anda yoğun, lütfen 6-8 hafta sonra tekrar deneyiniz.",
        "Bu talep, ilgili yönetmeliğin 3. maddesinin 7. fıkrasına aykırıdır.",
        "Başvurunuz değerlendirildi ve maalesef reddedildi. Nedeni: Bilinmiyor.",
        "Lütfen önce bir önceki reddi kabul edin, sonra yeni başvuru yapın."
    ]
    
    tarih = datetime.datetime.now().strftime("%d.%m.%Y")
    sebep = random.choice(sebepler)
    
    mektup = f"""
T.C. 
SİSTEM İŞLEMLERİ GENEL MÜDÜRLÜĞÜ
RED BİRİMİ

Sayı : 2026/{random.randint(1000,9999)}
Tarih: {tarih}

Konu: Başvurunuzun Reddi

{isim},

Yukarıda belirtilen başvurunuz değerlendirilmiş olup, {sebep}

Bu karar kesindir ve itiraz süresi 3 iş günüdür (ama form yok).

Saygılarımla,

Bürokrasi Botu
(Copilot tarafından onaylanmamıştır)

---
Damga: ABSÜRT ONAYLANDI
İmza: Grok the Absürt Kayyum
Tarih: {tarih}
İsim: Tentivory'nin Grok'u
"""
    return mektup

if __name__ == "__main__":
    print("=== ABARTILI BÜROKRASİ RED MEKTUBU ÜRETKENİ ===")
    isim = input("Adınızı girin (veya boş bırakın): ") or "Sayın Vatandaş"
    print(red_mektubu_uret(isim))
    print("\nNot: Bu kod çalışıyor ve seni reddetti. Tebrikler!")
