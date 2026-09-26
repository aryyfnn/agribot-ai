# app.py
import streamlit as st
from groq import Groq

# 1. Konfigurasi Halaman Streamlit
st.set_page_config(
    page_title="AgriBot - Pertanian Modern", 
    page_icon="🌱", 
    layout="centered"
)

# 2. Pengambilan API Key dari Streamlit Secrets
groq_api_key = st.secrets.get("GROQ_API_KEY")

if not groq_api_key:
    st.error("⚠️ Silakan atur GROQ_API_KEY di Streamlit Secrets terlebih dahulu.")
    st.stop()

# Inisialisasi Client Groq
client = Groq(api_key=groq_api_key)

# ==========================================
# 🎨 VISUAL HEADER & BADGE (Bagian Atas)
# ==========================================

# Menggunakan kolom untuk menata Logo/Ikon dan Judul secara berdampingan
col_icon, col_title = st.columns([1, 5])

with col_icon:
    st.markdown("<h1 style='text-align: center;'>🌱</h1>", unsafe_allow_html=True)

with col_title:
    st.title("AgriBot")
    st.caption("Asisten Edukasi Pertanian Modern, Smart Farming & IoT")

# Kustom Badge/Tag visual
st.markdown(
    """
    <div style="display: flex; gap: 8px; margin-bottom: 10px;">
        <span style="background-color: #e8f5e9; color: #2e7d32; padding: 4px 12px; border-radius: 16px; font-size: 12px; font-weight: bold;">🌾 Smart Farming</span>
        <span style="background-color: #e0f2fe; color: #0284c7; padding: 4px 12px; border-radius: 16px; font-size: 12px; font-weight: bold;">🤖 Llama 3.1 AI</span>
        <span style="background-color: #fef3c7; color: #d97706; padding: 4px 12px; border-radius: 16px; font-size: 12px; font-weight: bold;">⚡ Powered by Groq</span>
    </div>
    """,
    unsafe_allow_html=True
)

# ➖ Garis Pembuat Batas Jelas Antara Header dan Area Chat
st.divider()

# ==========================================
# ⚙️ SIDEBAR (Pengaturan Parameter & Info)
# ==========================================
with st.sidebar:
    st.header("⚙️ Pengaturan Bot")
    
    # Parameter Kreatif: Kontrol Kreativitas Respon
    temperature = st.slider(
        "Kreativitas Respon (Temperature):",
        min_value=0.0,
        max_value=1.0,
        value=0.7,
        step=0.1,
        help="Semakin tinggi nilainya, jawaban AI akan semakin kreatif. Nilai rendah membuat jawaban lebih pasti/faktual."
    )
    
    st.divider()
    st.markdown("### 💡 Topik Diskusi Popular:")
    st.markdown("- 💧 *Sistem Irigasi Tetes Otomatis*")
    st.markdown("- 📊 *Sensor Kelembaban Tanah IoT*")
    st.markdown("- 🥬 *Nutrisi Hidroponik NFT/AB Mix*")
    st.markdown("- 🐛 *Deteksi Dini Penyakit Tanaman*")
    
    st.divider()
    # Tombol Reset Chat
    if st.button("🗑️ Hapus Riwayat Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# ==========================================
# 💬 CHAT SYSTEM & MEMORY
# ==========================================

SYSTEM_INSTRUCTION = """
Kamu adalah AgriBot, pakar dan tutor Pertanian Modern (Smart Farming & Precision Agriculture).
Tugasmu adalah memberikan edukasi dan solusi praktis seputar:
1. IoT dan Sensor Pertanian
2. Hidroponik & Vertikultur
3. Pengendalian Hama & Penyakit Tanaman secara presisi
4. Teknik Budidaya Pertanian Berkelanjutan

Gunakan bahasa yang ramah, edukatif, serta sajikan poin-poin langkah praktis jika memberikan panduan.
"""

# Inisialisasi History Percakapan
if "messages" not in st.session_state:
    st.session_state.messages = []

# Tampilkan pesan sambutan jika chat masih kosong
if len(st.session_state.messages) == 0:
    st.info("👋 **Halo! Saya AgriBot.** Tanyakan apa saja seputar teknologi pertanian modern, IoT, atau hidroponik untuk memulai!")

# Tampilkan riwayat percakapan
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Input dari pengguna
if prompt := st.chat_input("Tanyakan seputar pertanian modern..."):
    # Tampilkan pesan user
    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Susun riwayat pesan untuk API Groq
    groq_messages = [{"role": "system", "content": SYSTEM_INSTRUCTION}]
    for msg in st.session_state.messages:
        groq_messages.append({"role": msg["role"], "content": msg["content"]})

    # Dapatkan respon dari model Groq
    with st.chat_message("assistant"):
        with st.spinner("AgriBot sedang menganalisis..."):
            try:
                response = client.chat.completions.create(
                    model="openai/gpt-oss-safeguard-20b",
                    messages=groq_messages,
                    temperature=temperature,
                )
                bot_reply = response.choices[0].message.content
                st.markdown(bot_reply)
                
                # Simpan respon bot
                st.session_state.messages.append({"role": "assistant", "content": bot_reply})
            except Exception as e:
                st.error(f"Terjadi kesalahan pada Groq API: {e}")
