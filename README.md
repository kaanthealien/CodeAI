# CodeAI - Yapay Zekâ Destekli Python Kod Üretici Asistanı

**CodeAI**, kullanıcıların verdiği istemlere göre Python kodları üreten bir yapay zekâ destekli asistan uygulamasıdır. Kullanıcı, basit bir web arayüzü üzerinden bir komut girer ve sistem, uygun Python kodunu ve bu kodu açıklayan başlığı üretir. Proje, **Google Gemini 1.5 Flash** modelini kullanarak güçlü bir yapay zekâ desteği sağlar.

---

## 📦 **Kurulum ve Çalıştırma**

### Gereksinimler:
- Python 3.11 veya daha yüksek bir sürümü
- Docker (Opsiyonel, Minikube ile dağıtım için)
- Kubernetes (Opsiyonel, Minikube ile dağıtım için)
- `.env` dosyasına API key eklemeli (Google Gemini API)

### 1. Projeyi Çekme:
```bash
git clone https://github.com/kaanthealien/codeai.git
cd codeai
```
### 2 .env Dosyasının Düzenlenmesi:
Google Gemini API anahtarınızı .env dosyasına ekleyin:
```bash
API_KEY=api-keyiniz
```

### 3. Flask Uygulamanızı Çalıştırma:
```bash
python3 app.py
```
<br></br>

## 🚀 **Docker ve Kubernetes ile Dağıtım**

### 1. Docker İmajını Oluşturma:

Aşağıdaki komut ile Docker imajını oluşturabilirsiniz:
```bash
docker build -t docker-hub_adiniz/imaj-adiniz .
```
### 2. Docker İmajını Docker Hub'a Gönderme:

Docker Hub'a imajı yüklemek için:
```bash
docker push docker-hub_adiniz/imaj-adiniz:latest
```
### 3. Kubernetes Dağıtımı:

deployment.yaml dosyasını kullanarak Kubernetes ortamında uygulamayı dağıtabilirsiniz. Aşağıdaki komut ile Kubernetes kümesine uygulamayı dağıtın:
```bash
kubectl apply -f deployment.yaml
```
<br></br>
## 🔧 **Yapılandırma ve Özelleştirme**

- Model Seçimi: app.py dosyasında kullanılan yapay zekâ modelini değiştirebilirsiniz.
- API Key: Google Gemini API anahtarınızı güvenli bir şekilde .env dosyasına ekleyin.
<br></br>
## 📝 **Projede Kullanılan Teknolojiler**
- Flask: Web uygulaması için Python tabanlı mikroframework.
- Docker: Uygulamanın konteynerize edilmesi ve dağıtılması için.
- Kubernetes / Minikube: Uygulamanın ölçeklenebilir ve taşınabilir bir ortamda dağıtılması için.
- Google Gemini 1.5 Flash: Yapay zekâ modelini çalıştırmak için.
<br></br>
## 📷 **Görseller:**
![Image](https://github.com/user-attachments/assets/63ad5988-e372-40f8-9281-5868d6dd428c)
![Image](https://github.com/user-attachments/assets/9bff51ad-43e3-4d3c-bec4-c6c5ac7266f6)

