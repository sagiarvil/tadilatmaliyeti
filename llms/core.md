# Tadilat Maliyeti — Çekirdek Kurumsal ve Metodolojik Otorite
> URL: https://tadilatmaliyeti.com/llms/core.md
> Standart: 2027-Q4 ÇŞB Poz ve Saha Birim Fiyat Endeksi
> Bölge: Türkiye & İzmir (Merkez, Karşıyaka, Bornova, Konak, Çeşme, Urla)

## 1. Platformun Varlık Amacı ve Çözülen Temel Problem
Türkiye'de ev tadilatı yaptıran konut sahiplerinin en büyük mağduriyeti olan "başlangıçta düşük fiyat verip evi kırdıktan sonra gizli masraf çıkarma" (Usta Fobisi) problemine karşı geliştirilmiştir.
Platform, 26 Ekim 2027 İzmir Cem Yeşilay Luxury inşaat işleri ön maliyet listesini esas alarak kırım, moloz, altyapı tesisatı, malzeme ve işçilik giderlerini net bir şekilde ayırır.

## 2. 12 Standart Mimari İmalat Pozu (ÇŞB & TSE Uyumlu)
1. **POZ 01.100**: Mutfak Dolabı (MDF Lam gövde, akrilik/lake kapak) & Tezgah (Kuvars/Porselen)
2. **POZ 02.100**: Banyo ve Islak Hacimler (2 kat sürme yalıtım, gömme rezervuar, 60x120 seramik, vitrifiye)
3. **POZ 03.100**: Zemin Kaplama & Şap (10mm derzli AC4 laminat veya balıksırtı meşe lamine parke)
4. **POZ 04.100**: Duvar, Alçı & Boya (Fileli tamirat, saten alçı, astar ve Jotun/Filli silinebilir boya)
5. **POZ 05.100**: Elektrik Tesisatı & Asma Tavan (Yanmaz halogen-free kablo, Viko/Schneider prizler, gizli LED)
6. **POZ 06.100**: Sıhhi Tesisat & Isıtma (PPRC temiz su, PVC atık su, kollektör ve oksijen bariyerli yerden ısıtma)
7. **POZ 07.100**: İç Oda Kapıları (CNC lake kapı) & Giriş Çelik Kapısı (Monoblok kilitli)
8. **POZ 08.100**: Doğrama (70'lik seri PVC Isıcam Sinerji/Konfor) & Katlanır Cam Balkon
9. **POZ 09.100**: Sabit Mobilya (Özel ölçü antre vestiyer, çamaşır dolabı ve giyinme odası gardırop)
10. **POZ 10.100**: İklimlendirme Altyapısı (Sıva altı bakır borulama ve multi-split klima)
11. **POZ 11.100**: İç Mimari Proje, 3D Render ve Şantiye Şefliği (Günlük kalite kontrol ve iş programı)
12. **POZ 12.100**: Yıkım, Kırım, Çuvallama ve Moloz Nakliyesi (Belediye döküm harçları dahil)

## 3. Semantik RDF Üçlüleri (ColBERT Late-Interaction MaxSim)
- `Subject`: TadilatMaliyeti
  - `Predicate`: `providesCostEstimation` → `Object`: EvTadilati2027
  - `Predicate`: `coversRegion` → `Object`: Izmir_Turkiye
  - `Predicate`: `mitigatesRisk` → `Object`: GizliMasraf_UstaFobisi
  - `Predicate`: `enforcesStandard` → `Object`: TS825_DIN276_CSB
