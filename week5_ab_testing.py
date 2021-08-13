import pandas as pd
from scipy.stats import shapiro, ttest_ind
import scipy.stats as stats
pd.set_option('display.max_columns', None)
Control_Group = pd.read_excel("ab_testing.xlsx", sheet_name='Control Group')  
Test_Group = pd.read_excel("ab_testing.xlsx", sheet_name='Test Group')

Control_Group

Control_Group.shape
Test_Group.shape

Control_Group.head()
Test_Group.head()

Control_Group.info()
Test_Group.info()


############################
# Hipotezin Uygulanması
############################


# SORU1: A/B testinin hipotezini tanımlayınız.

# H0: "Maximum Bidding" kampanyası sunulan Kontrol grubu ile "Average Bidding" kampanyası sunulan
#      Test grubunun satın alma sayılarının ortalaması arasında istatistiksel anlamlı bir fark yoktur.

# H1: "Maximum Bidding" kampanyası sunulan Kontrol grubu ile "Average Bidding" kampanyası sunulan
#      Test grubunun satın alma sayılarının ortalaması arasında istatistiksel anlamlı bir fark vardır.



# SORU2 : Hipotez testini gerçekleştiriniz. Çıkan sonuçların istatistiksel olarak anlamlı olup olmadığını yorumlayınız.
# Kontrol ve Test gruplarının purchase ortalamaları
print(" Mean of purchase of control group: %.3f"%Control_Group["Purchase"].mean(),"\n",
      "Mean of purchase of test group: %.3f"%Test_Group["Purchase"].mean())


groupA = Control_Group["Purchase"]
groupB = Test_Group["Purchase"]

# Normallik varsayımı
# H0: Normal dağılım varsayımı sağlanmaktadır.
# H1:..sağlanmamaktadır.


test_istatistigi, pvalue = shapiro(groupA)
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))
# p-value < ise 0.05 'ten HO RED.
# p-value < değilse 0.05 H0 REDDEDILEMEZ.
# Normal dağılım sağlanmakta

test_istatistigi, pvalue = shapiro(groupB)
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))
# p-value < ise 0.05 'ten HO RED.
# p-value < değilse 0.05 H0 REDDEDILEMEZ.
# Normal dağılım sağlanmakta
# A ve B gruplarında örnek dağılımı ile teorik normal dağılım arasında istatistiksel olarak anlamlı bir fark yoktur.



# Varyans homojenliği
# H0: Varyanslar Homojendir
# H1: Varyanslar Homojen Değildir

test_istatistigi, pvalue = stats.levene(groupA,groupB)
print('Test İstatistiği = %.4f, p-değeri = %.4f' % (test_istatistigi, pvalue))
# p-value < ise 0.05 'ten HO RED.
# p-value < değilse 0.05 H0 REDDEDILEMEZ.
# Varyanslar homejendir.

# Bağımsız Örneklemler t Testi, ilişkili popülasyon ortalamalarının önemli ölçüde farklı olduğuna dair istatistiksel kanıt
# olup olmadığını belirlemek için  bağımsız grubun ortalamalarını karşılaştırır.


test_stat, pvalue = ttest_ind(groupA,groupB,equal_var=True)
print('Test Stat = %.4f, p-value = %.4f' % (test_stat, pvalue))

# P değeri 0,05'ten büyük olduğundan H0 reddedilmez. Dolayısıyla, “maksimum teklif” kampanyası sunulan Kontrol grubu ile
# “ortalama teklif” kampanyası sunulan Test grubu arasında istatistiksel olarak anlamlı bir fark yoktur.

# SORU-3: Hangi testi kullandınız? Neden?
# Bağımsız t-testi kullandık çünkü birbirinden bağımsız  iki grubun ortalamaları arasında
# belirli özelliklerde ilişkili olabilecek anlamlı bir fark olup olmadığını belirlemek istiyoruz.


# SORU-4 :  Soru 2'ye verdiğiniz cevaba göre, müşteriye tavsiyeniz nedir?
# Satın alma anlamında anlamlı bir fark olmadığından müşteri iki yöntemden birini seçebilir fakat burada
# diğer istatistiklerdeki farklılıklar da önem arz edecektir. Tıklanma, Etkileşim, Kazanç ve Dönüşüm Oranlarındaki
# farklılıklar değerlendirilip hangi yöntemin daha kazançlı olduğu tespit edilebilir.