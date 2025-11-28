📱 Türkçe Akıllı Telefon Yorum Analizi

Transformer tabanlı Derin Öğrenme modeli ile anlık duygu analizi yapan masaüstü uygulaması

Bu proje, PyTorch kullanılarak geliştirilmiş özel bir Transformer sınıflandırma modeli ile Türkçe akıllı telefon yorumlarını Olumlu / Olumsuz olarak sınıflandırır.
Uygulama, PyQt5 tabanlı modern bir masaüstü arayüzü ile kullanıcının yazdığı metnin duygusunu gerçek zamanlı olarak analiz eder.

✨ Özellikler

🧠 Transformer Mimarisi
Positional Encoding + Multi-Head Attention yapısı ile bağlamı anlayabilen özel bir sınıflandırıcı.

🎨 Modern PyQt5 Arayüzü
Koyu temalı, sade ve kullanıcı dostu bir masaüstü uygulaması.

⚡ Gerçek Zamanlı Analiz
Kullanıcı yorumları anında analiz edilir.

📊 Güven Skoru
Model çıktısı, örneğin: %93 Olumlu şeklinde güven yüzdesi ile birlikte gösterilir.

🔄 Overfitting Önleme
Optimize edilmiş hiperparametreler ve veri karıştırma teknikleri ile küçük veri setlerinde bile doğru genelleme.

🧠 Model Mimarisi

Model, Transformer.py dosyasında aşağıdaki mimariyi kullanır:

SimpleTransformerClassifier

Embedding Layer: Kelimeleri vektör temsilcilere dönüştürür

Positional Encoding: Cümledeki kelimelerin konum bilgisini modele kazandırır

Transformer Encoder Layer: Çoklu dikkat mekanizması ile bağlam ilişkilerini öğrenir

Global Average Pooling: Cümle temsilini özetler

Linear Layer: Son sınıflandırma (Pozitif / Negatif)

# 📁 Proje Klasör Yapısı

```
TR-Sentiment-Transformer/
│
├── Transformer.py        # Transformer model mimarisi
├── requirements.txt      # Gerekli paketler
└── README.md             # Proje dokümanı
```

---

# 🔧 Kurulum

## 1️⃣ Depoyu Klonla
```
git clone https://github.com/YOUR_USERNAME/turkish-phone-sentiment-analysis.git
cd turkish-phone-sentiment-analysis
```

# 🚀 Uygulamayı Başlat

```
python main.py
```

Terminalde şu mesaj görünürse her şey hazır:

```
EĞİTİM TAMAMLANDI!
```

---

# 🖥️ Arayüz Kullanımı

Örnek bir yorum yaz:

```
Kamera güzel ama şarjı çok çabuk bitiyor.
```

Sonra **ANALİZ ET** butonuna bas.

Görünen sonuç örneği:

```
Sonuç: Olumsuz
Güven Yüzdesi: %87.8
```

🤝 Katkıda Bulunma

Katkılarınızı memnuniyetle karşılıyoruz!

Repoyu forklayın
```
Yeni branş oluşturun → git checkout -b feature/YeniOzellik
```
Kodunuzu commit edin
```
Push edin → git push origin feature/YeniOzellik
```

👨‍💻 Geliştirici

HarunIder10