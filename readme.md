# Dinamik Rotalama

Created: August 25, 2024 7:32 PM
Status: Done

Bu proje Eskişehir Osmangazi Üniversitesi Akıllı Sistemler Uygulama ve Araştırma Merkezi (CISAR) yaz çalıştayı kapsamında yapılmıştır. Elektrikli araçların rotalamasında kullanılan yöntemlerden Dinamik Rotalama çalışılmıştır.

Çalışma içerisinde Osmangazi Üniversitesi Kampüsü haritası kullanılmıştır. Bu harita üzerinde rastgele seçilen müşteri noktaları arasında öncelikle statik rota oluşturulmuştur. Ardından rota güzergahı takip edilirken her adımda %50 olasılık ile yeni müşteri talepleri alınmıştır. Eğer talep alınmışsa servis edilmemiş rastgele bir müşteri rota güzergahına eklenmiştir. Bu işlem rota güzergahı tamamlanana kadar devam etmiştir. Yeni müşteri talebi her zaman rotanın ilerisine (henüz gidilmemiş) eklenmiştir. Böylelikle dinamik rotalama yapılmıştır. 


- table of contrubutors

| Ekip | Rolü |
| --- | --- | 
| [Yasin Ünal](https://github.com/Pilestin/)  | Rotalama Algoritması, Veri ortamının hazırlanması ve Dökümantasyon |
| [Ahmet Alperen Polat](https://github.com/aalperenpolat) | Rotaların Sumo ortamında gösterimi |



## İçindekiler

- [Dinamik Rotalama](#dinamik-rotalama)
  - [İçindekiler](#i̇çindekiler)
  - [Dökümantasyon](#dökümantasyon)
    - [Dinamik Rotalama Nedir ? ](#dinamik-rotalama-nedir--)
    - [Rapor ve kod detayları ](#rapor-ve-kod-detayları-)
  - [Kısıtlar](#kısıtlar)
  - [Ön Kabuller :](#ön-kabuller-)
  - [Veri](#veri)
    - [Müştelerin Temsili](#müştelerin-temsili)
  - [Sonuçlar](#sonuçlar)
    - [Gelecek Çalışmalar](#gelecek-çalışmalar)


## Dökümantasyon

### [Dinamik Rotalama Nedir ? ](https://dawn-squash-710.notion.site/Dinamik-Rotalama-Nedir-8a50a862114f4fffac4998e6cdd08c54?pvs=4)

### [Rapor ve kod detayları ](https://dawn-squash-710.notion.site/al-tay-d5028b31d5e14140831e9cc111f1c399?pvs=4)


## Kısıtlar  

1. Rassal bir şekilde (rassallık derecesi %50 olsun şimdilik) yeni müşteri talebi seçilecek 
2. Her talep girildiğinde tekrar rota oluşturulup mevcut rotayla (current route) değiştirilecek 
3. Eğer yeni müşteri talebi alındıysa, bu müşteri rotanın ilerisine (henüz gidilmemiş) eklenmeli
4. Rota bittiğinde başlangıç noktasına geri dönülecek (depoya) 

## Ön Kabuller : 

1. taşıma kapasitesi tüm müşterilere yetecek (göz ardı et )
2. her müşteriye gidildiğinde 20 kg ağırlık düşecek 
3. her container noktasında 20 adımlık bekleme süresi olacak 

## Veri

C20 problem seti (ESOGÜ map içerisinden tanımlanan 20 hayali talep noktası) için müşteri id'leri :

```python 
Customers :  [2, 39, 115, 42B, 43C, 50, 58/1, 153, 51, 37B, 49, 8, 44, 9, 27, 116, 31, 30, 26]
```



Müşteriler arasından rastgele seçilen yarısı ile rota oluşturulur. Rota başında ve sonunda bulunan cs5 depoyu ifade etmektedir. Her rota mutlaka cs5 depo ile başlamalı ve bitmelidir.

Örnek Rota :

```python 
Initial Route:       [cs5,  115, 50, 26, 39, 43C, 27, 9, 42B, 30, 2, cs5]
Unserved Customers:  [58/1, 153, 51, 37B, 49, 8, 44, 116, 31] 
```

### Müştelerin Temsili

Müşteriler, ID'leri ile gösterilmektedir. Fakat aslında Objects/Customer sınıfı ile temsil edilmektedir. Ayrıca bu sınıf Objects/Target sınıfından miras almıştır ve bu sınıfın distance_to metodu ile iki müşteri arasındaki mesafe hesaplanabilmektedir. Bunu başta elde edilen distance matrix (data_handler.py) ile yapmaktayız.


## Sonuçlar 

Statik Rotalama : Taleplerin önceden belli olduğu, kargo/kurye'nin henüz güzergahı takip etmeye başlamadığı yapı düşünülebilir. Örneğin aşağıda 100 iterasyon boyunca örnek bir statik rotalama yapılmaktadır. Belirli olan müşteriler (müşteri id) rota içerisinde (liste) her iterasyonda yer değiştirilir. Yer değiştirme sonrasında rotanın toplam ne kadar mesafeye sahip olduğu hesaplanır. İyi bir rota elde edildiyse çözüm tutulur.

    
```python	
----------------------------------------------------------------
Initial Route      :     [cs5, 43C, 115, 39, 37B, 42B, 58/1, 153, 49, 44, 26, cs5]       cost:  9777.0
Unserved Customers :     [2, 50, 8, 9, 27, 116, 31, 30]
----------------------------------------------------------------
devam etmek için bir tuşa basınız
Iteration: 0     Cost: 9777.0    Route: [cs5, 43C, 115, 39, 37B, 42B, 58/1, 153, 49, 44, 26, cs5]
devam . . .
Iteration: 10    Cost: 8179.0    Route: [cs5, 43C, 58/1, 44, 42B, 39, 26, 115, 49, 153, 37B, cs5]
devam . . .
Iteration: 20    Cost: 8179.0    Route: [cs5, 43C, 58/1, 44, 42B, 39, 26, 115, 49, 153, 37B, cs5]
devam . . .
Iteration: 30    Cost: 7927.0    Route: [cs5, 58/1, 37B, 49, 43C, 115, 26, 44, 42B, 39, 153, cs5]
devam . . .
Iteration: 40    Cost: 7927.0    Route: [cs5, 58/1, 37B, 49, 43C, 115, 26, 44, 42B, 39, 153, cs5]
devam . . .
Iteration: 50    Cost: 7927.0    Route: [cs5, 58/1, 37B, 49, 43C, 115, 26, 44, 42B, 39, 153, cs5]
devam . . .
Iteration: 60    Cost: 7927.0    Route: [cs5, 58/1, 37B, 49, 43C, 115, 26, 44, 42B, 39, 153, cs5]
devam . . .
Iteration: 70    Cost: 6736.0    Route: [cs5, 49, 115, 26, 44, 43C, 42B, 39, 153, 37B, 58/1, cs5]
devam . . .
Iteration: 80    Cost: 6736.0    Route: [cs5, 49, 115, 26, 44, 43C, 42B, 39, 153, 37B, 58/1, cs5]
devam . . .
Iteration: 90    Cost: 6736.0    Route: [cs5, 49, 115, 26, 44, 43C, 42B, 39, 153, 37B, 58/1, cs5]
devam . . .
Iteration: 100   Cost: 6736.0    Route: [cs5, 49, 115, 26, 44, 43C, 42B, 39, 153, 37B, 58/1, cs5]
devam . . .

```	


Dinamik Rotalama : Elde edilen en iyi rota (statik rotalama ile) üzerinde her adımda %50 olasılık ile yeni müşteri talebi alınır. Eğer talep alınmışsa servis edilmemiş rastgele bir müşteri rota güzergahına en iyi noktaya gelecek şekilde eklenir. Bu işlem rota güzergahı tamamlanana kadar devam eder. Yeni müşteri talebi her zaman rotanın ilerisine (henüz gidilmemiş) eklenir. Yeni müşteri eklenirken rotanın kalanında her müşteriden yeni müşteriye olan mesafe hesaplanır ve en az maliyetli olan yer seçilir. 
Örnek : 
```python	
new_customer = # yeni müşteri talebi
now = i # i.müşteri
costs = []
for customer in route[i:-1]
    # rotanın ilerisindeki her müşteri için
    cost = customer.distance_to(new_customer)
    costs.append(cost, customer)
# en az maliyetli olanı seç ve rotaya ekle
. . . 

```
Sonuçlar : 

```python

Route:  -> | cs5 | === 49 === 115 === 26 === 44 === 43C === 42B === 39 === 153 === 37B === 58/1 === cs5


Şu an : [0] cs5
0.22954364387729775 olasılığı geldi. devam ediliyor.
----------------------------------------------------------------
Route:  -> cs5 === | 49 | === 115 === 26 === 44 === 43C === 42B === 39 === 153 === 37B === 58/1 === cs5


Şu an : [1] 49
0.5582140365309552 olasılığı geldi. Yeni müşteri id: 50 eklenecek.
Müşteri id 50 için rotadaki en yakın yer ve uzaklık :  (247.0, 49)
Müşteri id 50 rotaya dahil ediliyor . . .
----------------------------------------------------------------
Route:  -> cs5 === 49 === | 50 | === 115 === 26 === 44 === 43C === 42B === 39 === 153 === 37B === 58/1 === cs5


Şu an : [2] 50
0.8850353074697132 olasılığı geldi. Yeni müşteri id: 9 eklenecek.
Müşteri id 9 için rotadaki en yakın yer ve uzaklık :  (865.0, 115)
Müşteri id 9 rotaya dahil ediliyor . . .
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === | 115 | === 9 === 26 === 44 === 43C === 42B === 39 === 153 === 37B === 58/1 === cs5


Şu an : [3] 115
0.9971253758622021 olasılığı geldi. Yeni müşteri id: 31 eklenecek.
Müşteri id 31 için rotadaki en yakın yer ve uzaklık :  (231.0, 42B)
Müşteri id 31 rotaya dahil ediliyor . . .
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === | 9 | === 26 === 44 === 43C === 42B === 31 === 39 === 153 === 37B === 58/1 === cs5


Şu an : [4] 9
0.5700870250167994 olasılığı geldi. Yeni müşteri id: 116 eklenecek.
Müşteri id 116 için rotadaki en yakın yer ve uzaklık :  (264.0, 26)
Müşteri id 116 rotaya dahil ediliyor . . .
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === | 26 | === 116 === 44 === 43C === 42B === 31 === 39 === 153 === 37B === 58/1 === cs5


Şu an : [5] 26
0.23565260582405512 olasılığı geldi. devam ediliyor.
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === 26 === | 116 | === 44 === 43C === 42B === 31 === 39 === 153 === 37B === 58/1 === cs5


Şu an : [6] 116
0.3260364420107935 olasılığı geldi. devam ediliyor.
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === 26 === 116 === | 44 | === 43C === 42B === 31 === 39 === 153 === 37B === 58/1 === cs5


Şu an : [7] 44
0.6136614435864995 olasılığı geldi. Yeni müşteri id: 27 eklenecek.
Müşteri id 27 için rotadaki en yakın yer ve uzaklık :  (687.0, 37B)
Müşteri id 27 rotaya dahil ediliyor . . .
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === 26 === 116 === 44 === | 43C | === 42B === 31 === 39 === 153 === 37B === 27 === 58/1 === cs5


Şu an : [8] 43C
0.2899888549446624 olasılığı geldi. devam ediliyor.
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === 26 === 116 === 44 === 43C === | 42B | === 31 === 39 === 153 === 37B === 27 === 58/1 === cs5


Şu an : [9] 42B
0.32060510311514134 olasılığı geldi. devam ediliyor.
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === 26 === 116 === 44 === 43C === 42B === | 31 | === 39 === 153 === 37B === 27 === 58/1 === cs5


Şu an : [10] 31
0.3357100218046858 olasılığı geldi. devam ediliyor.
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === 26 === 116 === 44 === 43C === 42B === 31 === | 39 | === 153 === 37B === 27 === 58/1 === cs5


Şu an : [11] 39
0.78706225113547 olasılığı geldi. Yeni müşteri id: 8 eklenecek.
Müşteri id 8 için rotadaki en yakın yer ve uzaklık :  (865.0, 27)
Müşteri id 8 rotaya dahil ediliyor . . .
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === 26 === 116 === 44 === 43C === 42B === 31 === 39 === | 153 | === 37B === 27 === 8 === 58/1 === cs5


Şu an : [12] 153
0.16614649388654024 olasılığı geldi. devam ediliyor.
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === 26 === 116 === 44 === 43C === 42B === 31 === 39 === 153 === | 37B | === 27 === 8 === 58/1 === cs5


Şu an : [13] 37B
0.22836671215921922 olasılığı geldi. devam ediliyor.
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === 26 === 116 === 44 === 43C === 42B === 31 === 39 === 153 === 37B === | 27 | === 8 === 58/1 === cs5


Şu an : [14] 27
0.25767347474867996 olasılığı geldi. devam ediliyor.
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === 26 === 116 === 44 === 43C === 42B === 31 === 39 === 153 === 37B === 27 === | 8 | === 58/1 === cs5


Şu an : [15] 8
0.9101386878248239 olasılığı geldi. Yeni müşteri id: 2 eklenecek.
Müşteri id 2 için rotadaki en yakın yer ve uzaklık :  (541.0, 8)
Müşteri id 2 rotaya dahil ediliyor . . .
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === 26 === 116 === 44 === 43C === 42B === 31 === 39 === 153 === 37B === 27 === 8 === | 2 | === 58/1 === cs5


Şu an : [16] 2
0.7945491325344802 olasılığı geldi. Yeni müşteri id: 30 eklenecek.
Müşteri id 30 için rotadaki en yakın yer ve uzaklık :  (1001.0, 2)
Müşteri id 30 rotaya dahil ediliyor . . .
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === 26 === 116 === 44 === 43C === 42B === 31 === 39 === 153 === 37B === 27 === 8 === 2 === | 30 | === 58/1 === cs5


Şu an : [17] 30
Tüm müşteriler servis edildi.
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === 26 === 116 === 44 === 43C === 42B === 31 === 39 === 153 === 37B === 27 === 8 === 2 === 30 === | 58/1 | === cs5


Şu an : [18] 58/1
Tüm müşteriler servis edildi.
----------------------------------------------------------------
Route:  -> cs5 === 49 === 50 === 115 === 9 === 26 === 116 === 44 === 43C === 42B === 31 === 39 === 153 === 37B === 27 === 8 === 2 === 30 === 58/1 === | cs5 | ===


Şu an : [19] cs5
Tüm müşteriler servis edildi.
[cs5, 49, 50, 115, 9, 26, 116, 44, 43C, 42B, 31, 39, 153, 37B, 27, 8, 2, 30, 58/1, cs5]

```

### Gelecek Çalışmalar

Rotaya eklenecek olan müşteri talebi olasılığı dinamik hale getirilebilir. Örneğin rotadaki müşteri sayısına oranlı bir talep elde edilebilir. Rotaya eklenecek olan müşterilerin farklı yöntemler ile eklemeleri yapılabilir. Belirli bir kısıt ile (örneğin bu yeni müşteriye gidip gelmenin maliyeti) bu müşteri rotaya dahil edilmeyebilir. Ayrıca elektrikli aracın yük ve şarj kapasitesi dikkate alınarak daha kapsamlı bir çalışma yapılabilir. 