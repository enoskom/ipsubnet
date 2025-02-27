# ipsubnet

IP Subnet Hesaplayıcı

Bu proje, IPv4 ve IPv6 adresleri için subnet hesaplamaları yapmanıza olanak tanır. 
Kullanıcılar, IP adresi ve subnet maskesini girdikten sonra ağ adresi, yayın 
adresi, kullanılabilir host aralığı, toplam host sayısı gibi ağ bilgilerini 
görüntüleyebilirler. Ayrıca, GUI (Graphical User Interface) üzerinden 
kullanım kolaylığı sağlanmıştır.
Özellikler

    IPv4 ve IPv6 Desteği: Hem IPv4 hem de IPv6 adresleriyle subnet hesaplaması 
    yapılabilir.
    Hesaplama Sonuçları: Ağ adresi, yayın adresi, kullanılabilir host sayısı gibi 
    bilgilerin hesaplanması.
    CIDR Notasyonu: IP adresinin CIDR (Classless Inter-Domain Routing) 
    notasyonu ile belirtilmesi.
    Açıklamalar ve Eğitim İçeriği: Kullanıcıya IP adresi, subnet maskesi, 
    ağ adresi, yayın adresi, wildcard maskesi gibi kavramlar hakkında bilgi sunulur.
    Örnek Subnet Tablosu: Class A, B, C ağları için prefix büyüklükleri ve her 
    subnet için kullanılabilir host sayısı içeren örnek tabloyu görüntüleme.
    Dosya Kaydetme: Hesaplama sonuçlarını metin dosyasına kaydetme imkanı.
    Kullanıcı Dostu Arayüz: Tkinter ile yapılmış basit ve anlaşılır bir grafiksel 
    arayüz.

Kullanım
Gereksinimler

Projenin çalışabilmesi için Python 3.x sürümüne ve aşağıdaki Python 
kütüphanelerine ihtiyaç vardır:

    ipaddress (Python 3.x ile dahili olarak gelir)
    tkinter (GUI için)
    ttk (tkinter'ın stilize edilmiş widget'ları için)

Başlangıç
Projeyi çalıştırmak için:

    Python 3.x'i bilgisayarınıza kurun.
    Repo'yu bilgisayarınıza indirin.

git clone https://github.com/enoskom/ipsubnet.git

İlgili dosyayı çalıştırın:

    python ipsubnetting.py

GUI arayüzü açıldığında:

    IPv4 veya IPv6 Hesaplama: İlk başta IPv4 veya IPv6 hesaplama modunu seçin.
    IP ve Subnet Maskesi Girişi: IP adresini ve subnet maskesini girin.
    Hesapla Butonu: Hesaplamak için "Hesapla" butonuna tıklayın.
    Sonuçlar: Hesaplama sonuçları ekranın alt kısmında görüntülenecektir.
    Örnek Tablo: IP sınıflarına göre subnet tablosunu görüntülemek için 
    "Örnek Subnet Tablosu" butonuna tıklayın.
    Açıklamalar: Ağ terminolojisi hakkında bilgi almak için "Açıklamalar" 
    butonuna tıklayın.

GUI Özellikleri

    Yeni Hesaplama: Yeni bir hesaplama yapmak için "Yeni" butonuna tıklayın.
    Çıktı Kaydetme: Hesaplama sonuçlarını metin dosyasına kaydetmek için 
    "Çıktı Yazdır" butonunu kullanın.
    Kapat: Uygulamayı kapatmak için "Kapat" butonuna tıklayın.

Diğer Özellikler

    Açıklamalar: IP adresi, subnet maskesi, ağ adresi gibi konularda 
    temel açıklamalar içerir.
    Subnet Tablosu: Subnet büyüklüklerine göre her IP sınıfının ağ 
    maskeleri ve kullanılabilir host sayıları gösterilir.
