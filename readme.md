# Dinamik Rotalama

Created: August 25, 2024 7:32 PM
Status: In Progress

1. Esogü Map 2.2
2. Araçlarda rotalama nasıl yapılır 
3. Araçlarda traciApi içerisidnen canlı olarak nasıl rota eklenir.
    
    (container stopta duracak ve durduysa istenen yerde uğrak listesine eklenecek) 
    
4. rassal bir şekilde (rassallık derecesi %50 olsun şimdilik) rastgele bir şekilde container stop seçecek 
5. her talep girildiğinde tekrar rota oluşturulup mevcut rotayla (current route) değiştirilecek 
6. başlangıç noktasına geri dönülecek 

Ön Kabuller : 

1. taşıma kapasitesi tüm müşterilere yetecek (göz ardı et )
2. her müşteriye gidildiğinde 20 kg ağırlık düşecek 
3. her container noktasında 20 adımlık bekleme süresi olacak 


C20 problem seti için müşteri id'leri :

```python 
Customers :  [2, 39, 115, 42B, 43C, 50, 58/1, 153, 51, 37B, 49, 8, 44, 9, 27, 116, 31, 30, 26]
```



Müşteriler arasından rastgele seçilen yarısı ile rota oluşturulur. Rota başında ve sonunda bulunan cs5 depoyu ifade etmektedir. Her rota mutlaka cs5 depo ile başlamalı ve bitmelidir.

Örnek Rota :

```python 
Initial Route:       [cs5,  115, 50, 26, 39, 43C, 27, 9, 42B, 30, 2, cs5]
Unserved Customers:  [58/1, 153, 51, 37B, 49, 8, 44, 116, 31] 
```




SUMO 

[Dinamik Rotalama Nedir ? ](https://www.notion.so/Dinamik-Rotalama-Nedir-c9fd7954eb104d2db8c47c59c08cc485?pvs=21)

[Dijkstra Matrix ve Python ile Gerçeklenmesi  ](https://www.notion.so/Dijkstra-Matrix-ve-Python-ile-Ger-eklenmesi-ae3e797c44f2404aad6b8a5c3e04fa89?pvs=21)

[Sunum ](https://www.notion.so/Sunum-d7d577418d084a77a5c06d352c445603?pvs=21)