# 🧾 İBB Bisiklet Projesi – Teknik Dökümantasyon

## 📌 Proje Amacı
Bu proje, İstanbul Büyükşehir Belediyesi'nin bisiklet kiralama ve kullanım hizmetlerini yönetmek amacıyla Django framework'ü ile geliştirilmiş bir web uygulamasıdır.

## 🧱 Proje Yapısı

ibb-bisiklet/
├── corporate/ # Ana Django uygulaması
│ ├── models.py # Veritabanı modelleri
│ ├── views.py # Görünümler (iş mantığı)
│ ├── urls.py # URL yönlendirme
│ └── templates/ # HTML şablonlar
├── static/ # CSS, JS, görseller
├── db.sqlite3 # Geliştirme veritabanı
├── manage.py
├── README.md
└── requirements.txt