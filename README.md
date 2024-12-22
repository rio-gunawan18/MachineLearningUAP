# README.md

## Author
M. Rio Gunawan (202110370311026)

## Deskripsi Proyek
Proyek ini bertujuan untuk mengembangkan sistem klasifikasi citra instrumen musik menggunakan model deep learning. Latar belakang pengembangan proyek ini adalah untuk membantu pengenalan dan identifikasi instrumen musik secara otomatis berdasarkan gambar, yang memiliki potensi aplikasi di bidang edukasi, katalog digital, hingga industri kreatif.

## Dataset
Dataset yang digunakan berasal dari Kaggle dengan nama "Musical Instruments Image Classification" dan dapat diakses melalui tautan berikut: [Musical Instruments Image Classification](https://www.kaggle.com/datasets/gpiosenka/musical-instruments-image-classification). Dataset ini mencakup berbagai citra instrumen musik seperti gitar, piano, drum, dan lain-lain yang telah diklasifikasikan ke dalam beberapa kategori.

## Langkah Instalasi
1. Clone repositori proyek ini ke dalam komputer Anda:
   ```bash
   git clone <url-repo>
   cd <nama-folder-repo>
   ```
2. Buat lingkungan virtual untuk mengelola dependencies:
   ```bash
   python -m venv env
   source env/bin/activate  # Untuk Linux/MacOS
   env\Scripts\activate    # Untuk Windows
   ```
3. Install dependencies yang diperlukan:
   ```bash
   pip install -r requirements.txt
   ```
4. Jalankan aplikasi web menggunakan perintah berikut:
   ```bash
   streamlit run app.py
   ```

## Deskripsi Model
Proyek ini menggunakan dua model utama untuk klasifikasi citra:
1. **ResNet50**: Model ini dikenal dengan arsitekturnya yang mendalam menggunakan residual connections, yang membantu mengatasi masalah vanishing gradient dan memungkinkan pelatihan model dengan banyak lapisan.
2. **VGG16**: Model ini memiliki arsitektur yang sederhana namun efektif dengan layer-layer konvolusi yang disusun secara berurutan, ideal untuk pengenalan pola visual.

Kinerja model dievaluasi menggunakan metrik akurasi, precision, recall, dan F1-score. Kedua model dioptimasi menggunakan dataset yang telah disiapkan dan dibandingkan performanya untuk menentukan model terbaik.

## Hasil dan Analisis
Hasil evaluasi menunjukkan perbandingan performa antara ResNet50 dan VGG16 dalam mengklasifikasikan citra instrumen musik. Berikut adalah hasil metrik evaluasi:

| Model    | Akurasi | Precision | Recall | F1-Score |
|----------|---------|-----------|--------|----------|
| ResNet50 | 99%     | 99%       | 99%    | 99%    |
| VGG16    | 96%     | 97%       | 96%    | 96%    |

Grafik perbandingan performa dapat dilihat pada aplikasi web yang telah disediakan. Berdasarkan analisis, ResNet50 menunjukkan hasil yang lebih baik dibandingkan VGG16 dalam pengklasifikasian dataset ini.
