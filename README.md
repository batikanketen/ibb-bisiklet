# 🚴‍♂️ İBB Bisiklet Projesi

Bu proje, Django framework'ü kullanılarak geliştirilen bir web uygulamasıdır. Amaç, İstanbul Büyükşehir Belediyesi'nin bisiklet hizmetlerini dijital ortamda yönetmek ve sunmaktır.

---

## 💻 Kullanılan Teknolojiler

| Teknoloji     | Açıklama                                             |
|---------------|------------------------------------------------------|
| 🐍 **Python** | Projenin arka uç (backend) programlama dili          |
| 🌐 **Django** | Python tabanlı web framework, hızlı geliştirme sağlar|
| 💅 **HTML**   | Web sayfalarının yapısını oluşturmak için            |
| 🎨 **CSS**    | Sayfaların görünümünü ve tasarımını düzenlemek için  |
| ⚙️ **Bootstrap** | Responsive (mobil uyumlu) ve modern UI için     |
| 🛢 **SQLite** | Geliştirme sürecinde kullanılan varsayılan veritabanı|

---

## 📦 Özellikler

- Yönetici paneli üzerinden bisiklet verisi yönetimi
- Modern, responsive kullanıcı arayüzü
- Temiz, modüler Django proje yapısı
- Gereksiz dosyaları dışlayan `.gitignore` desteği

---

## 🚀 Kurulum

```bash
git clone https://github.com/batikanketen/ibb-bisiklet.git
cd ibb-bisiklet
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py runserver
