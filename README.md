# 30 Musical Instrument
![Background Image](assets/background.png)

## Overview Project
Proyek ini bertujuan untuk mengembangkan sistem klasifikasi citra untuk pengenalan dan identifikasi instrumen musik secara otomatis dengan memanfaatkan model deep learning ResNet50 dan VGG16. Sistem ini dirancang untuk menganalisis gambar instrumen musik dan mengklasifikasikannya ke dalam kategori yang sesuai. Dengan teknologi ini, diharapkan dapat meningkatkan efisiensi dan akurasi dalam proses identifikasi instrumen musik, yang dapat diaplikasikan pada berbagai bidang seperti pendidikan musik, manajemen data multimedia, hingga aplikasi pengarsipan budaya. Pemanfaatan arsitektur ResNet50 dan VGG16 memberikan keuntungan dalam mengolah fitur visual kompleks dari gambar, memastikan performa model yang andal dan skalabilitas yang tinggi. Proyek ini juga menjadi langkah awal dalam mengintegrasikan teknologi modern ke dalam pengenalan instrumen musik secara otomatis.

## Dataset
Dataset yang digunakan berasal dari Kaggle dengan nama "Musical Instruments Image Classification" dan dapat diakses melalui tautan berikut: [Musical Instruments Image Classification](https://www.kaggle.com/datasets/gpiosenka/musical-instruments-image-classification). Dataset ini mencakup berbagai citra instrumen musik seperti gitar, piano, drum, dan lain-lain yang telah diklasifikasikan ke dalam beberapa kategori.

## Deskripsi Model
Proyek ini menggunakan dua model utama untuk klasifikasi citra:
1. **ResNet50**: Model ini dikenal dengan arsitekturnya yang mendalam menggunakan residual connections, yang membantu mengatasi masalah vanishing gradient dan memungkinkan pelatihan model dengan banyak lapisan.
2. **VGG16**: Model ini memiliki arsitektur yang sederhana namun efektif dengan layer-layer konvolusi yang disusun secara berurutan, ideal untuk pengenalan pola visual.

### Link Model
1. **ResNet50**: [Download Model](https://drive.google.com/file/d/1gmAV0MfD3aWf5wrtc5oL2YPvMK3eY6Xm/view?usp=drive_link)
2. **VGG16**: [Download Model](https://drive.google.com/file/d/1nD6G8P7UEVdKPov2AjrWgtNh_RwycBtG/view?usp=sharing)

## Hasil dan Analisis
Hasil evaluasi menunjukkan perbandingan performa antara ResNet50 dan VGG16 dalam mengklasifikasikan citra instrumen musik. Berikut adalah hasil metrik evaluasi:

1. **ResNet50** 
![restnet50](https://github.com/user-attachments/assets/fe02500b-5e4d-4ebb-a04c-be18fa055ae7)
![Screenshot 2024-12-23 130300](https://github.com/user-attachments/assets/18f85076-62c2-4c4c-b06f-3c99901d0799)

2. **VGG16**
![vgg16](https://github.com/user-attachments/assets/1b882998-8f6a-4673-8ce8-950d3881eb17)
![Screenshot 2024-12-23 130345](https://github.com/user-attachments/assets/bb43cf83-e177-4f9b-88ef-e42313470bdb)


## Author
M. Rio Gunawan (202110370311026)
