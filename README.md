# 🌱 AgriBot - Asisten Pertanian Modern (Smart Farming Chatbot)

AgriBot adalah aplikasi chatbot interaktif berbasis Artificial Intelligence (AI) yang dirancang untuk memberikan edukasi dan solusi praktis seputar **Pertanian Modern**, **Smart Farming**, **IoT Pertanian**, dan **Manajemen Kesehatan Tanaman**. 

Proyek ini dibangun menggunakan **Streamlit** sebagai antarmuka pengguna dan diintegrasikan dengan **Groq API (Llama 3)** untuk pemrosesan bahasa alami (*Natural Language Processing*) yang responsif dan cepat.

---

## 📸 Fitur Utama

- **Intelegen & Edukatif:** Menggunakan model LLM `llama-3.3-70b-versatile` melalui Groq API yang dioptimalkan untuk ranah pertanian modern.
- **Percakapan Kontekstual (Memory):** Memiliki fitur *Chat History* (`st.session_state`) yang mengingat percakapan sebelumnya dalam satu sesi.
- **Antarmuka Interaktif:** Tampilan berbasis web yang *clean*, responsif, dan mudah digunakan.
- **Keamanan Konfigurasi:** Menggunakan Streamlit Secrets untuk manajemen API Key secara aman.

---

## 🛠️ Spesifikasi & Parameter Proyek

| Parameter | Spesifikasi |
| :--- | :--- |
| **Use Case** | Education & Advisory Bot (Pertanian Modern) |
| **LLM Model** | Llama 3.3 70B (`llama-3.3-70b-versatile`) |
| **Provider API** | Groq Cloud API |
| **Framework UI** | Streamlit |
| **Persona / Tone** | Edukatif, Ramah, Solutif, dan Praktis |
| **Temperature** | `0.7` (Menjaga keseimbangan antara variasi teks dan akurasi) |

---

## 📁 Struktur Repositori

```text
├── .gitignore          # Daftar berkas/folder yang diabaikan oleh Git
├── README.md           # Dokumentasi proyek
├── app.py              # Kode utama aplikasi Streamlit dan integrasi Groq API
└── requirements.txt    # Daftar dependensi library Python
