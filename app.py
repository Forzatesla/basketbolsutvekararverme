import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sayfa Yapısı
st.set_page_config(page_title="ACS Analysis Lab", layout="wide")

# Gelişmiş CSS: Görünürlük ve Baskı Düzeni
st.markdown("""
    <style>
    /* 1. Görünürlük: Metinleri siyaha sabitle */
    .main { background-color: #ffffff !important; }
    .main p, .main h1, .main h2, .main h3, .main h4, .main span, .main label {
        color: #000000 !important;
    }
    
    /* 2. Buton Tasarımı */
    div.stButton > button:first-child {
        width: 100%;
        background-color: #ff6600;
        color: white !important;
        border: none;
        padding: 10px;
        font-weight: bold;
    }

    /* 3. Yazdırma (Baskı) Ayarları */
    @media print {
        [data-testid="stSidebar"], 
        header, 
        footer, 
        .stActionButton,
        div.stButton {
            display: none !important;
        }
        
        .main .block-container {
            padding-top: 0rem !important;
        }

        @page {
            size: auto;
            margin: 15mm;
        }
    }
    </style>
    """, unsafe_allow_html=True)

st.title("Karar Verme ve Şut Gelişim Analizi")

# Sidebar - Veri Girişi
st.sidebar.header("Veri Girişi")
name = st.sidebar.text_input("Sporcu Adı", "İsim Soyisim")
pos = st.sidebar.selectbox("Pozisyon", ["Guard", "Forvet", "Pivot"])

st.sidebar.divider()
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
    current_vals = [m2, k2, d2, b2, o2]
    base_vals = [m1, k1, d1, b1, o1]
    
    current_vals += current_vals[:1]
    base_vals += base_vals[:1]
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    
    ax.plot(angles, base_vals, color='#777777', linewidth=1.5, linestyle='--', label='Başlangıç')
    ax.fill(angles, base_vals, color='#777777', alpha=0.1)
    
    ax.plot(angles, current_vals, color='#ff6600', linewidth=2.5, label='Güncel')
    ax.fill(angles, current_vals, color='#ff6600', alpha=0.3)
    
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=10, color='black')
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.tick_params(colors='black')
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    
    st.pyplot(fig)

# --- GÜNCELLENEN BUTON VE HATIRLATMA BÖLÜMÜ ---
if st.button("Raporu PDF Kaydet / Yazdır"):
    st.markdown("---")
    st.subheader("İndirme Rehberi")
    
    col_pc, col_mob = st.columns(2)
    with col_pc:
        st.write("**💻 Bilgisayar Kullanıcıları**")
        st.write("1. **Ctrl + P** (Windows) veya **Cmd + P** (Mac) tuşlarına basın.")
        st.write("2. Hedef olarak **'PDF Olarak Kaydet'** seçin.")
    
    with col_mob:
        st.write("**📱 Mobil Kullanıcılar**")
        st.write("1. Tarayıcınızın **'Paylaş'** simgesine dokunun.")
        st.write("2. Menüden **'Yazdır'** seçeneğini bulun.")
        st.write("3. Önizleme ekranında **'PDF Olarak Kaydet'** diyerek indirin.")
    st.warning("Not: En iyi görünüm için yazdırma ayarlarında 'Yatay (Landscape)' modunu seçebilirsiniz.")
