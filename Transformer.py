import sys
import torch
import torch.nn as nn
import torch.optim as optim
import random  # Veriyi karıştırmak için gerekli
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, 
                             QLineEdit, QPushButton, QFrame, QTextEdit)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

# ==========================================
# 1. TELEFON YORUMLARI VERİ SETİ (200 CÜMLE)
# ==========================================
# Veri seti aynen korunmuştur.
corpus = [
    # --- OLUMLU TELEFON YORUMLARI (100 adet) ---
    ("telefon harika çok beğendim memnunum", 1),
    ("kamera kalitesi müthiş fotoğraflar enfes", 1),
    ("batarya ömrü uzun iki gün gidiyor", 1),
    ("ekran kalitesi çok net renkler canlı", 1),
    ("işlemci hızlı oyunlar akıcı çalışıyor", 1),
    ("şarj çok hızlı yarım saatte doluyor", 1),
    ("tasarım çok şık elime harika oturuyor", 1),
    ("ses kalitesi mükemmel müzik dinlemek keyifli", 1),
    ("hoparlör sesi çok net ve yüksek", 1),
    ("hafıza yeterli çok uygulama yüklüyorum", 1),
    ("ram performansı güçlü donma yapmıyor", 1),
    ("5g hızı çok iyi internet uçuyor", 1),
    ("wifi bağlantısı çok güçlü hiç kopmadı", 1),
    ("bluetooth mesafesi geniş sorunsuz", 1),
    ("gps hızlı bulunuyor hassas konumlama", 1),
    ("parmak izi okuyucu çok hızlı açılıyor", 1),
    ("yüz tanıma güvenli hemen açıyor", 1),
    ("kutu açılışı muhteşem orijinal ürün", 1),
    ("kargo hızlı geldi güvenli paketlenmişti", 1),
    ("fiyat performans ürünü kesinlikle tavsiye", 1),
    ("garantisi uzun iki yıl resmi", 1),
    ("telefon sorunsuz çalışıyor hatasız", 1),
    ("arayüz çok akıcı sade ve kullanışlı", 1),
    ("android güncellemeleri hızlı geliyor", 1),
    ("oyun performansı yüksek grafikler açık", 1),
    ("ısınma sorunu yok uzun süre oyunda", 1),
    ("video kalitesi dört k çok net", 1),
    ("gece modu fotoğrafları muhteşem", 1),
    ("zoom özelliği net kayıpsız yakınlaştırma", 1),
    ("ön kamera selfie için harika", 1),
    ("arka kamera üçlü lens çok işlevli", 1),
    ("makro çekim kalitesi çok iyi detaylı", 1),
    ("portre modu çok güzel arka plan bulanık", 1),
    ("slow motion video akıcı ve net", 1),
    ("timelapse özelliği çok başarılı", 1),
    ("hdr fotoğraflar canlı ve kaliteli", 1),
    ("panorama çekimi geniş ve kesintisiz", 1),
    ("pro mod ayarları profesyonel seviye", 1),
    ("kamera uygulaması kullanımı kolay", 1),
    ("video stabilizasyon çok iyi sarsıntısız", 1),
    ("ekran parlaklığı yüksek güneşte görülüyor", 1),
    ("dokunmatik hassasiyeti mükemmel", 1),
    ("ekran yenileme hızı yüksek akıcı", 1),
    ("amoled ekran renkleri harika", 1),
    ("ekran koruyucu filmle geldi", 1),
    ("telefon kılıfı hediye güzel sürpriz", 1),
    ("kulaklık hediye kaliteli ses veriyor", 1),
    ("şarj aleti hızlı orijinal adaptör", 1),
    ("usb kablo kaliteli sağlam", 1),
    ("kutuda sim iğnesi var pratik", 1),
    ("kullanım kılavuzu türkçe anlaşılır", 1),
    ("ilk kurulum çok basit hızlı", 1),
    ("veri aktarımı kolay eski telefondan", 1),
    ("uygulama mağazası güncel her şey var", 1),
    ("güvenlik güncellemeleri düzenli geliyor", 1),
    ("telefonun ağırlığı ideal hafif", 1),
    ("boyutu tam cebe rahatlıkla giriyor", 1),
    ("kenarları ergonomik tutuşu rahat", 1),
    ("metal kasa sağlam dayanıklı", 1),
    ("cam arka yüzey premium his veriyor", 1),
    ("su geçirmez özellik var güvenli", 1),
    ("toz geçirmez sertifikalı kaliteli", 1),
    ("çift sim kart özelliği işime yarıyor", 1),
    ("hafıza kartı desteği var genişletilebilir", 1),
    ("kulaklık girişi var bluetooth zorunlu değil", 1),
    ("hoparlör stereo iki taraftan ses", 1),
    ("titreşim motoru güçlü hissediliyor", 1),
    ("led bildirim ışığı var kullanışlı", 1),
    ("nfc özelliği var temassız ödeme yapıyorum", 1),
    ("kızılötesi kumanda özelliği çok güzel", 1),
    ("fm radyo dinliyorum internet gerektirmeden", 1),
    ("mesaj bildirimleri zamanında geliyor", 1),
    ("arama kalitesi net karşı taraf duyuyor", 1),
    ("mikrofon kalitesi iyi ses kaydı güzel", 1),
    ("video görüşme kalitesi yüksek hd", 1),
    ("sesli asistan hızlı anlıyor cevaplıyor", 1),
    ("klavye titreşimi ayarlanabilir", 1),
    ("ekran saat özelliği çok pratik", 1),
    ("karanlık mod göz yormayan kullanışlı", 1),
    ("uygulama kilidi özelliği güvenlik sağlıyor", 1),
    ("çift uygulama özelliği iki hesap açıyorum", 1),
    ("ekran kaydı özelliği yerleşik var", 1),
    ("oyun modu özelliği performansı artırıyor", 1),
    ("gizlilik ayarları detaylı kontrolüm bende", 1),
    ("yedekleme otomatik buluta atıyor", 1),
    ("telefon bulma özelliği kaybolmama engel", 1),
    ("acil durum modu var önemli özellik", 1),
    ("çocuk modu var güvenli kullanım", 1),
    ("pil tasarrufu modu uzatıyor kullanımı", 1),
    ("hızlı şarj ayarları özelleştirilebilir", 1),
    ("kablosuz şarj özelliği var pratik", 1),
    ("ters kablosuz şarj kulaklık şarj ediyor", 1),
    ("güç paylaşımı başka telefon şarj ediyor", 1),
    ("dolby atmos ses kalitesi sinema gibi", 1),
    ("ekran altı parmak izi hızlı ve güvenli", 1),
    ("pop up kamera tasarım çok yenilikçi", 1),
    ("yandan açılır kamera ekran tam", 1),
    ("uydu navigasyon çoklu sistem destekliyor", 1),
    
    # --- OLUMSUZ TELEFON YORUMLARI (100 adet) ---
    ("telefon berbat hiç beğenmedim", 0),
    ("kamera kalitesi kötü bulanık çekiyor", 0),
    ("batarya çabuk bitiyor öğlene kadar gidiyor", 0),
    ("ekran kalitesi berbat soluk renkler", 0),
    ("işlemci yavaş takılıyor donuyor", 0),
    ("şarj çok yavaş saatlerce bekletme", 0),
    ("tasarım çirkin eski model gibi", 0),
    ("ses kalitesi kötü cızırtı var", 0),
    ("hoparlör çok zayıf duyulmuyor", 0),
    ("hafıza yetersiz sürekli dolu uyarısı", 0),
    ("ram yetersiz uygulama kapanıyor", 0),
    ("5g çekmiyor sinyal sorunu var", 0),
    ("wifi bağlantısı sürekli kopuyor", 0),
    ("bluetooth cihaz bulamıyor bağlanmıyor", 0),
    ("gps yavaş bulunuyor hatalı konum", 0),
    ("parmak izi okuyucu çalışmıyor tanımıyor", 0),
    ("yüz tanıma başarısız açmıyor", 0),
    ("kutuda aksesuar eksik kablo yok", 0),
    ("kargo hasarlı geldi ekran çatlak", 0),
    ("pahalı telefon bu fiyata değmez", 0),
    ("garanti yok ikinci el satmışlar", 0),
    ("telefon hatalı sürekli kapanıyor", 0),
    ("arayüz karmaşık kullanımı zor", 0),
    ("güncelleme gelmiyor eski sürüm kaldı", 0),
    ("oyun performansı kötü kasıyor takılıyor", 0),
    ("aşırı ısınıyor eline alamazsın", 0),
    ("video kalitesi düşük piksel bozuk", 0),
    ("gece fotoğrafları korkunç çekilmiyor", 0),
    ("zoom yapınca çok bozuluyor kalitesiz", 0),
    ("ön kamera çok kötü selfie çekilmez", 0),
    ("arka kamera odaklanmıyor bulanık", 0),
    ("makro modu çalışmıyor yakın çekemiyor", 0),
    ("portre modu başarısız kesim kötü", 0),
    ("slow motion titrek akıcı değil", 0),
    ("timelapse bozuk sıçramalı video", 0),
    ("hdr fotoğraflar yanlış ton", 0),
    ("panorama çekimi kesiyor birleştiremiyor", 0),
    ("pro mod ayarları çalışmıyor", 0),
    ("kamera uygulaması donuyor kapanıyor", 0),
    ("video stabilizasyon yok çok sarsak", 0),
    ("ekran parlaklığı düşük güneşte görünmüyor", 0),
    ("dokunmatik hassasiyet kötü geç tepki", 0),
    ("ekran yenileme hızı düşük takılıyor", 0),
    ("ekran kalitesi kötü ips teknolojisi eski", 0),
    ("ekran koruyucu yok ayrı almak gerek", 0),
    ("kılıf hediye gelmedi satın aldım", 0),
    ("kulaklık yok kutuda sadece telefon var", 0),
    ("şarj aleti yavaş orijinal değil", 0),
    ("usb kablo hemen bozuldu kırıldı", 0),
    ("sim iğnesi yok açamadım", 0),
    ("kullanım kılavuzu yok türkçe olmayan", 0),
    ("ilk kurulum karmaşık anlamadım", 0),
    ("veri aktarımı çalışmıyor hata veriyor", 0),
    ("uygulama mağazası yok oyun yüklenmiyor", 0),
    ("güvenlik güncellemesi gelmiyor eski", 0),
    ("telefon çok ağır taşıması yorucu", 0),
    ("boyutu çok büyük cebe sığmıyor", 0),
    ("kenarları keskin tutuşu rahatsız", 0),
    ("plastik kasa çok ucuz dayanıksız", 0),
    ("arka yüzey çizildi ilk günde", 0),
    ("su geçirmez değil ıslak kaldı bozuldu", 0),
    ("toz girdi içine koruma yok", 0),
    ("çift sim desteklemiyor sadece tek", 0),
    ("hafıza kartı desteği yok genişletilemiyor", 0),
    ("kulaklık girişi yok bluetooth mecbur", 0),
    ("hoparlör mono tek taraftan ses", 0),
    ("titreşim motoru zayıf hissetmiyorum", 0),
    ("led ışık yok bildirim görmüyorum", 0),
    ("nfc yok temassız ödeme yapamıyorum", 0),
    ("kızılötesi yok kumanda özelliği olmayan", 0),
    ("fm radyo yok dinleyemiyorum", 0),
    ("mesaj bildirimleri gelmiyor eksik", 0),
    ("arama kalitesi kötü ses parazit", 0),
    ("mikrofon bozuk karşı taraf duymuyor", 0),
    ("video görüşme kalitesi düşük piksel", 0),
    ("sesli asistan yok kullanamıyorum", 0),
    ("klavye titreşimi yok his vermiyor", 0),
    ("ekran saat özelliği yok görmüyorum", 0),
    ("karanlık mod yok gözüm yoruluyor", 0),
    ("uygulama kilidi yok güvensiz", 0),
    ("çift uygulama özelliği yok sınırlı", 0),
    ("ekran kaydı yok uygulama yükledim", 0),
    ("oyun modu yok performans düşük", 0),
    ("gizlilik ayarları yok güvensiz", 0),
    ("yedekleme otomatik değil manuel yapılıyor", 0),
    ("telefon bulma özelliği yok kayboldu", 0),
    ("acil durum modu yok önemli eksik", 0),
    ("çocuk modu yok güvenli olmayan", 0),
    ("pil tasarrufu modu yok hızla bitiyor", 0),
    ("hızlı şarj yavaş normal gibi", 0),
    ("kablosuz şarj yok kablolu mecbur", 0),
]

# --- SÖZLÜK OLUŞTURMA ---
word_to_ix = {}
for sentence, _ in corpus:
    for word in sentence.lower().split():
        if word not in word_to_ix:
            word_to_ix[word] = len(word_to_ix)

vocab_size = len(word_to_ix)
embed_dim = 16  # Vektör boyutu

# Yardımcı Fonksiyon
def make_bow_vector(sentence, word_to_ix):
    vec = [word_to_ix[word] for word in sentence.lower().split() if word in word_to_ix]
    return torch.tensor(vec, dtype=torch.long)

# ==========================================
# 2. MODEL MİMARİSİ (DÜZELTİLMİŞ)
# ==========================================
class SimpleTransformerClassifier(nn.Module):
    def __init__(self, vocab_size, embed_dim, num_heads, hidden_dim, num_layers):
        super(SimpleTransformerClassifier, self).__init__()
        
        # 1. Embedding Katmanı
        self.embedding = nn.Embedding(vocab_size, embed_dim)
        
        # 2. Pozisyonel Kodlama (Basitleştirilmiş)
        # Transformer'ın kelime sırasını anlaması için max 50 kelimeye kadar destek ekliyoruz
        self.pos_encoder = nn.Embedding(50, embed_dim)
        
        # 3. Transformer Encoder
        # batch_first=True: Girdi (Batch, Seq_Len, Feature) formatında olacak
        # dropout=0.0: Az veri olduğu için dropout'u kapattık (Veri kaybını önlemek için)
        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim, 
            nhead=num_heads, 
            dim_feedforward=hidden_dim, 
            batch_first=True,
            dropout=0.0 
        )
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)
        
        # 4. Çıkış Katmanı
        self.fc = nn.Linear(embed_dim, 2) 

    def forward(self, x):
        # x shape: [Batch_Size, Seq_Len]
        seq_len = x.size(1)
        
        # Pozisyon verisini oluştur (0, 1, 2, ... seq_len-1)
        positions = torch.arange(0, seq_len, device=x.device).unsqueeze(0)
        
        # Embedding + Pozisyon
        x = self.embedding(x) + self.pos_encoder(positions)
        
        # Transformer'dan geçir
        x = self.transformer_encoder(x)
        
        # Global Average Pooling (Tüm kelime vektörlerinin ortalamasını al)
        x = x.mean(dim=1) 
        
        # Sınıflandırma
        x = self.fc(x)
        return x

# ==========================================
# 3. EĞİTİM FONKSİYONU (DÜZELTİLMİŞ)
# ==========================================
def train_model():
    print("=" * 50)
    print("MODEL EĞİTİMİ BAŞLIYOR")
    print("=" * 50)
    print(f"Toplam {len(corpus)} yorum ile eğitim yapılıyor...")
    
    # Model Parametreleri
    model = SimpleTransformerClassifier(
        vocab_size, 
        embed_dim, 
        num_heads=2,    # Multi-head attention kafa sayısı
        hidden_dim=32,  # Ara katman genişliği
        num_layers=1    # Transformer katman sayısı (Az veri için 1 yeterli)
    )
    
    loss_function = nn.CrossEntropyLoss()
    # Learning rate biraz düşürüldü, daha stabil öğrenme için
    optimizer = optim.Adam(model.parameters(), lr=0.005)

    epochs = 50
    for epoch in range(epochs): 
        total_loss = 0
        
        # --- KRİTİK DÜZELTME: VERİ KARIŞTIRMA ---
        # Her epoch başında veriyi karıştırıyoruz ki model
        # sadece son gördüklerini (hepsi negatif) ezberlemesin.
        random.shuffle(corpus)
        
        for sentence, label in corpus:
            model.zero_grad()
            
            # Vektör oluşturma
            vec = make_bow_vector(sentence, word_to_ix)
            
            # Boş veya bilinmeyen kelimelerden oluşan cümleleri atla
            if len(vec) == 0: 
                continue
            
            # Model girdisi: [Batch=1, Seq_Len]
            sentence_in = vec.unsqueeze(0)
            target = torch.tensor([label], dtype=torch.long)
            
            logits = model(sentence_in)
            loss = loss_function(logits, target)
            loss.backward()
            optimizer.step()
            total_loss += loss.item()
        
        if (epoch + 1) % 10 == 0:
            print(f"Epoch {epoch + 1}/{epochs} - Ortalama Kayıp: {total_loss/len(corpus):.4f}")
            
    print("=" * 50)
    print("EĞİTİM TAMAMLANDI!")
    print("=" * 50)
    return model

# ==========================================
# 4. PYQT5 ARAYÜZÜ (AYNI KALDI)
# ==========================================
class SentimentApp(QWidget):
    def __init__(self, model):
        super().__init__()
        self.model = model
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("📱 Telefon Duygu Analizi Sistemi")
        self.setGeometry(300, 200, 600, 500)
        self.setStyleSheet("background-color: #1e1e2e; color: #ffffff;")

        layout = QVBoxLayout()
        layout.setSpacing(15)
        layout.setContentsMargins(30, 30, 30, 30)

        # Başlık
        title = QLabel("📱 Telefon Yorum Analizi")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        title.setStyleSheet("color: #00d4ff; padding: 10px;")
        layout.addWidget(title)

        # Alt Başlık
        subtitle = QLabel("Transformer ile Güçlendirilmiş Model")
        subtitle.setFont(QFont("Arial", 10))
        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setStyleSheet("color: #888888; padding-bottom: 10px;")
        layout.addWidget(subtitle)

        # Açıklama
        desc = QLabel("💬 Telefon hakkında bir yorum yazın:")
        desc.setFont(QFont("Arial", 11, QFont.Bold))
        desc.setStyleSheet("color: #cccccc;")
        layout.addWidget(desc)

        # Çok Satırlı Input Alanı
        self.input_field = QTextEdit()
        self.input_field.setPlaceholderText("Örnek: 'Telefon harika, kamera kalitesi çok iyi, batarya uzun gidiyor'")
        self.input_field.setFont(QFont("Arial", 11))
        self.input_field.setMaximumHeight(100)
        self.input_field.setStyleSheet("""
            padding: 12px; 
            border: 2px solid #444; 
            border-radius: 8px; 
            background-color: #2a2a3a;
            color: #ffffff;
        """)
        layout.addWidget(self.input_field)

        # Buton
        self.analyze_btn = QPushButton("🔍 ANALİZ ET")
        self.analyze_btn.setFont(QFont("Arial", 12, QFont.Bold))
        self.analyze_btn.setCursor(Qt.PointingHandCursor)
        self.analyze_btn.setStyleSheet("""
            QPushButton {
                background-color: #00d4ff; 
                color: #1e1e2e; 
                padding: 15px; 
                border-radius: 8px;
                border: none;
            }
            QPushButton:hover {
                background-color: #00b8e6;
            }
            QPushButton:pressed {
                background-color: #0099cc;
            }
        """)
        self.analyze_btn.clicked.connect(self.predict_sentiment)
        layout.addWidget(self.analyze_btn)

        # Sonuç Alanı
        self.result_frame = QFrame()
        self.result_frame.setStyleSheet("""
            background-color: #2a2a3a; 
            border-radius: 12px;
            border: 2px solid #444;
        """)
        self.result_frame.hide()
        
        result_layout = QVBoxLayout()
        result_layout.setContentsMargins(20, 20, 20, 20)
        
        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Arial", 18, QFont.Bold))
        self.result_label.setAlignment(Qt.AlignCenter)
        
        self.confidence_label = QLabel("")
        self.confidence_label.setFont(QFont("Arial", 11))
        self.confidence_label.setAlignment(Qt.AlignCenter)
        self.confidence_label.setStyleSheet("color: #aaaaaa; padding-top: 5px;")
        
        self.detail_label = QLabel("")
        self.detail_label.setFont(QFont("Arial", 10))
        self.detail_label.setAlignment(Qt.AlignCenter)
        self.detail_label.setWordWrap(True)
        self.detail_label.setStyleSheet("color: #888888; padding-top: 10px;")

        result_layout.addWidget(self.result_label)
        result_layout.addWidget(self.confidence_label)
        result_layout.addWidget(self.detail_label)
        self.result_frame.setLayout(result_layout)
        
        layout.addWidget(self.result_frame)
        layout.addStretch()
        
        # Alt Bilgi
        footer = QLabel("Powered by PyTorch Transformer | 200 Telefon Yorumu")
        footer.setFont(QFont("Arial", 8))
        footer.setAlignment(Qt.AlignCenter)
        footer.setStyleSheet("color: #555555; padding-top: 10px;")
        layout.addWidget(footer)
        
        self.setLayout(layout)

    def predict_sentiment(self):
        sentence = self.input_field.toPlainText().lower().strip()
        if not sentence: 
            return

        # Vektöre çevir
        vec = make_bow_vector(sentence, word_to_ix)
        
        if len(vec) == 0:
            self.result_label.setText("❓ BİLİNMEYEN YORUM")
            self.result_label.setStyleSheet("color: #ff9500;")
            self.confidence_label.setText("")
            self.detail_label.setText("Cümledeki kelimeler sistemde bulunmuyor.\nLütfen farklı kelimelerle tekrar deneyin.")
            self.result_frame.show()
            return

        # Tahmin
        self.model.eval() # Modeli değerlendirme moduna al
        with torch.no_grad():
            input_tensor = vec.unsqueeze(0)
            logits = self.model(input_tensor)
            probs = torch.softmax(logits, dim=1)
            
            predicted_class = torch.argmax(probs).item()
            confidence = probs[0][predicted_class].item() * 100
            negative_prob = probs[0][0].item() * 100
            positive_prob = probs[0][1].item() * 100

        self.model.train() # Modeli tekrar eğitim moduna al (gerekirse)
        self.result_frame.show()
        
        if predicted_class == 1:
            self.result_label.setText("😊 OLUMLU YORUM")
            self.result_label.setStyleSheet("color: #4cd964;")
            self.detail_label.setText(
                f"Bu telefon yorumu pozitif!\n"
                f"Müşteri telefondan memnun görünüyor."
            )
        else:
            self.result_label.setText("😡 OLUMSUZ YORUM")
            self.result_label.setStyleSheet("color: #ff3b30;")
            self.detail_label.setText(
                f"Bu telefon yorumu negatif!\n"
                f"Müşteri telefondan memnun değil."
            )
            
        self.confidence_label.setText(
            f"📊 Güven Oranı: %{confidence:.1f}\n"
            f"(Olumlu: %{positive_prob:.1f} | Olumsuz: %{negative_prob:.1f})"
        )

# ==========================================
# 5. ANA ÇALIŞTIRMA BLOKU
# ==========================================
if __name__ == "__main__":
    print("\n" + "="*50)
    print("📱 TELEFON DUYGU ANALİZİ SİSTEMİ")
    print("="*50 + "\n")
    
    # Model Eğitimi
    trained_model = train_model()
    
    # Arayüz Başlatma
    print("\n✅ Grafik arayüz açılıyor...\n")
    app = QApplication(sys.argv)
    window = SentimentApp(trained_model)
    window.show()
    
    print("📱 Pencere başarıyla açıldı!")
    print("💡 Bir yorum yazın ve 'ANALİZ ET' butonuna tıklayın.\n")
    
    sys.exit(app.exec_())