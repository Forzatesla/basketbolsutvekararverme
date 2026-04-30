import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sayfa Yapısı
st.set_page_config(page_title="ACS Analysis Lab", layout="wide")

# Gelişmiş CSS: Baskı Kalitesi ve Görünürlük
st.markdown("""
    <style>
    .main { background-color: #ffffff !important; }
    @media print {
        h1, h2, h3, h4, p, span, div, label, .stMarkdown {
            color: #000000 !important;
            opacity: 1 !important;
        }
        .stAlert {
            background-color: #f8f9fa !important;
            color: #000000 !important;
            border: 1px solid #000000 !important;
        }
        [data-testid="stSidebar"], header, footer, .stActionButton, div.stButton, [data-testid="stDecoration"] {
            display: none !important;
        }
    }
    div.stButton > button:first-child {
        width: 100%;
        background-color: #ff6600;
        color: white !important;
        font-weight: bold;
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

c_in1, c_in2 = st.sidebar.columns(2)
with c_in1:
    st.write("**Güncel**")
    m2 = st.number_input("Mekanik", 1, 10, 7, key="m2")
    k2 = st.number_input("Karar", 1, 10, 7, key="k2")
    d2 = st.number_input("Denge", 1, 10, 7, key="d2")
    b2 = st.number_input("Devamlılık", 1, 10, 7, key="b2")
    o2 = st.number_input("Oyunu Okuma", 1, 10, 7, key="o2")
with c_in2:
    st.write("**Başlangıç**")
    m1 = st.number_input("Mekanik", 1, 10, 5, key="m1")
    k1 = st.number_input("Karar", 1, 10, 5, key="k1")
    d1 = st.number_input("Denge", 1, 10, 5, key="d1")
    b1 = st.number_input("Devamlılık", 1, 10, 5, key="b1")
    o1 = st.number_input("Oyunu Okuma", 1, 10, 5, key="o1")

notes = st.sidebar.text_area("Antrenör Notları", "Gelişim reçetesi...")

# Ana Panel
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
    
    # Radar hesaplamaları
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]
    plot_current = current_vals + current_vals[:1]
    plot_base = base_vals + base_vals[:1]

    fig, ax = plt.subplots(figsize=(7, 7), subplot_kw=dict(polar=True))
    fig.patch.set_facecolor('white')
    ax.set_facecolor('white')
    
    # Başlangıç Profili
    ax.plot(angles, plot_base, color='#777777', linewidth=1.5, linestyle='--', label='Başlangıç')
    ax.fill(angles, plot_base, color='#777777', alpha=0.1)
    
    # Güncel Profil
    ax.plot(angles, plot_current, color='#ff6600', linewidth=3, label='Güncel')
    ax.fill(angles, plot_current, color='#ff6600', alpha=0.3)
    
    # --- SAYISAL DEĞERLERİ GRAFİĞE EKLEME ---
    for angle, val in zip(angles[:-1], current_vals):
        # Yazıları hafif dışarıya, siyah ve kalın şekilde ekliyoruz
        ax.text(angle, val + 0.8, str(val), color='black', size=12, 
                fontweight='bold', ha='center', va='center')

    # Grafik Süslemeleri
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories, size=11, color='black', fontweight='bold')
    ax.set_yticks([2, 4, 6, 8, 10])
    ax.tick_params(colors='#666666', labelsize=9)
    ax.legend(loc='upper right', bbox_to_anchor=(1.2, 1.1))
    
    st.pyplot(fig)

if st.button("Raporu PDF Kaydet / Yazdır"):
    st.markdown("---")
    st.subheader("📥 Kaydetme Rehberi")
    c1, c2 = st.columns(2)
    with c1:
        st.write("**💻 Bilgisayar:** Ctrl+P > PDF Kaydet")
    with c2:
        st.write("**📱 Mobil:** Paylaş > Yazdır > PDF Kaydet")
