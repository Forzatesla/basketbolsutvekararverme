import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sayfa Yapısı
st.set_page_config(page_title="ACS Analysis Lab", layout="wide")

# CSS ile sadeleştirme (Temiz ve profesyonel görünüm)
st.markdown("""
    <style>
    .main { background-color: #ffffff; }
    div.stButton > button:first-child {
        background-color: #ff6600;
        color: white;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Karar Verme ve Şut Gelişim Analizi")

# Sidebar - Veri Girişi
st.sidebar.header("Veri Girişi")
name = st.sidebar.text_input("Sporcu Adı", "İsim Soyisim")
pos = st.sidebar.selectbox("Pozisyon", ["Guard", "Forvet", "Pivot"])

st.sidebar.divider()

# Karşılaştırmalı Analiz Giriş Alanları
st.sidebar.subheader("Gelişim Skorları (1-10)")
st.sidebar.write("Turuncu: Güncel | Gri: Başlangıç")

col_input1, col_input2 = st.sidebar.columns(2)

with col_input1:
    st.write("**Güncel**")
    m2 = st.number_input("Mekanik", 1, 10, 7, key="m2")
    k2 = st.number_input("Karar", 1, 10, 7, key="k2")
    d2 = st.number_input("Denge", 1, 10, 7, key="d2")
    b2 = st.number_input("Devamlılık", 1, 10, 7, key="b2")
    o2 = st.number_input("Oyunu Okuma", 1, 10, 7, key="o2")

with col_input2:
    st.write("**Başlangıç**")
    m1 = st.number_input("Mekanik", 1, 10, 5, key="m1")
    k1 = st.number_input("Karar", 1, 10, 5, key="k1")
    d1 = st.number_input("Denge", 1, 10, 5, key="d1")
    b1 = st.number_input("Devamlılık", 1, 10, 5, key="b1")
    o1 = st.number_input("Oyunu Okuma", 1, 10, 5, key="o1")

notes = st.sidebar.text_area("Antrenör Notları", "Gelişim reçetesi...")

# Ana Rapor Paneli
col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("Sporcu Profili")
    st.write(f"**İsim:** {name}")
    st.write(f"**Pozisyon:** {pos}")
    st.write(f"**Analiz Tarihi:** {pd.Timestamp.now().strftime('%d/%m/%Y')}")
    st.divider()
    st.info(f"**Teknik Değerlendirme:** {notes}")

with col2:
    st.subheader("Gelişim Karşılaştırma Grafiği")
    
    categories = ['Mekanik', 'Karar Hızı', 'Denge', 'Devamlılık', 'Oyunu Okuma']
    
    # Veri setlerinin hazırlanması
    current_vals = [m2, k2, d2, b2, o2]
    base_vals = [m1, k1, d1, b1, o1]
    
    # Radar grafiği için döngüyü kapatma
    current_vals += current_vals[:1]
    base_vals += base_vals[:1]
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    # Başlangıç Profili (Gri - Kesikli Çizgi)
    ax.plot(angles, base_vals, color='#777777', linewidth=1.5, linestyle='--', label='Başlangıç')
    ax.fill(angles, base_vals, color='#777777', alpha=0.1)
    
    # Güncel Profil (Turuncu - Kalın Çizgi)
    ax.plot(angles, current_vals, color='#ff6600', linewidth=2.5, label='Güncel')
    ax.fill(angles, current_vals, color='#ff6600', alpha=0.3)
    
    # Grafik Ayarları
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=10)
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    
    st.pyplot(fig)

if st.button("Raporu Yazdır / PDF Kaydet"):
    st.info("Bu sayfayı PDF olarak kaydetmek için Ctrl+P (Windows) veya Cmd+P (Mac) komutunu kullanabilirsiniz.")
