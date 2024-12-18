import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

    
# NOT plt, grafiklerin gösterimi, eksen etiketleri, başlıklar gibi düzenlemeler için kullanılır.
# plot fonksiyonu, verilerin çizilmesi için kullanılan bir matplotlib fonksiyonudur. Bu fonksiyon doğrudan pyplot modülünden veya DataFrame gibi veri yapılarından (örneğin Pandas) çağrılabilir.plot, çeşitli türde grafikler çizmek için kullanılır: çizgi grafik, çubuk grafik, pasta grafik vb.


# örnek veri
df=pd.read_excel('teknolojik_urunler_zamanli.xlsx')
df['Tarih']=pd.to_datetime(df['Tarih'])

df.set_index('Tarih',inplace=True)

# satışların zaman içerisinde ki değişimini gösteren bir çizgi grafiği 
# df['Satış'].plot(title='Satışların Zaman İçindeki değişimi ',xlabel='Tarih',ylabel='Satış Miktarı')
# plt.show()

# belirli zaman diliminde ki toplam satışın bar grafiği
# aylik_satis=df.resample('ME')['Satış'].sum()
# kind grafiğin şeklini seçim yapıyorsun
# aylik_satis.plot(kind='bar',title='Aylık Toplam Satışlar',xlabel='Ay',ylabel='Toplam Satış')
# plt.show()


# pasta grafiği çizelim
# burada gruplma yapacağız
# autopct='%1.1f%%' bu kısım virgülden sonra kaç basamak göstereceğini belirliyor 

# kategori_Satış=df.groupby('Kategori')['Satış'].sum()
# kategori_Satış.plot(kind='pie',title='Kategorilere göre satış dağılımı',autopct='%1.1f%%')
# # dikey çizgi göremk istemiyorsak
# plt.ylabel('')
# plt.show()


# Scatter (Dağılım grafiği)
# df.plot(kind='scatter',title='fiyat ve satış ilişkisi',x='Fiyat (TL)',y='Satış')
# plt.show()



# derinin dağılımını göstermek için histogram grafiği
# df['Fiyat (TL)'].plot(kind='hist',title='Fiyat Dağılım',bins=10, )
# plt.xlabel('Fiyat (TL)') #BUNU İSTERSEK PARANTEZİN İÇİNE DE YAZABİLİRDİK 
# plt.ylabel('Kategori')
# plt.show()


# Aylık satış trendi
# aylik_satis=df.resample('ME')['Satış'].sum()
# aylik_satis.plot(kind='line',title='Aylık Satış Miktarları')
# plt.xlabel('Ay')
# plt.ylabel('Satış miktarı')
# plt.show()

# # trend çizgisi oluşturma (güzel bir örnek)
# df.plot(kind='scatter',x='Fiyat (TL)',y='Satış',title='Fiayat Satış İlişkisi')
# # nupy'e bağlan fiyat ve satış arasında polinom işlemi yap diyoruz 1 çizgi olyor
# z=np.polyfit(df['Fiyat (TL)'],df['Satış'],1)
# # 1 boyutlu analiz et diyoruz z den aldığın veriyi
# p=np.poly1d(z)
# # şimdi ekrana yazdıralım
# # burada polinomu fiyata göre yapıyoruz ve çekilen çizginin rengi de red 
# plt.plot(df['Fiyat (TL)'],p(df['Fiyat (TL)']), color='red')
# plt.show()




# çok işinize yarar
# fşyatları kategorilere ayıralım
# NOT labels listesindeki etiket sayısının bins listesindeki kenar sayısından bir eksik olması gerekir. Bu durumda, bins listesindeki 6 kenarın 5 aralığına karşılık 4 etiket olmalıdır.
bins=[0,2000,5000,10000,20000,30000]
labels=['Düşük','Orta ','Yüksek','Çok Yüksek','Lüks']
# listemin içine fiyat kategorisi eklemek istiyorum ve bunu df fiyat tan çekmek istiyorum o yüzden cut(kes) fonk.kullanıyoruz
df['Fiyat Kategorisi'] = pd.cut(df['Fiyat (TL)'], bins=bins, labels=labels)

# fiyat satış kategorisine göre satış dağılım
# df.groupby('Fiyat Kategorisi')['Satış'].sum().plot(kind='bar', title='Fiyat Kategorisine Göre Toplam Satışlar')
# plt.xlabel('Fiyat Kategorisi')
# plt.ylabel('Toplam Satış')
# plt.show()


