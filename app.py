import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Sayfa Yapısı
st.set_page_config(page_title="ACS Analysis Lab", layout="wide")

st.title("Karar Verme ve Şut Gelişim Analizi")

# Sidebar - Veri Girişi
st.sidebar.header("📊 Veri Girişi")
name = st.sidebar.text_input("Sporcu Adı", "İsim Soyisim")
pos = st.sidebar.text_input("Pozisyon", "Guard / Kanat / Uzun")

# Değişken isimlerini standartlaştırdım (i harfi kullanarak)
mekanik = st.sidebar.slider("Mekanik Verimlilik", 1, 10, 5)
karar = st.sidebar.slider("Karar Hızı", 1, 10, 5)
denge = st.sidebar.slider("Dinamik Denge", 1, 10, 5)
baski = st.sidebar.slider("Baskı Yönetimi", 1, 10, 5)
okuma = st.sidebar.slider("Okuma & Tepki", 1, 10, 5)

notes = st.sidebar.text_area("Antrenör Notları", "Gelişim reçetesi...")

# Rapor Alanı
col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("👤 Sporcu Profili")
    st.write(f"**İsim:** {name}")
    st.write(f"**Pozisyon:** {pos}")
    st.write(f"**Tarih:** {pd.Timestamp.now().strftime('%d/%m/%Y')}")
    st.divider()
    st.info(f"**Antrenör Notu:** {notes}")

with col2:
    # Radar Grafiği Hazırlığı
    categories = ['Mekanik', 'Karar Hızı', 'Denge', 'Baskı', 'Okuma']
    # Burada 'baski' değişkenini 'i' ile kullanarak hatayı giderdik
    values = [mekanik, karar, denge, baski, okuma]
    values += values[:1]
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()
    angles += angles[:1]

    fig, ax = plt.subplots(figsize=(5, 5), subplot_kw=dict(polar=True))
    ax.fill(angles, values, color='#ff6600', alpha=0.3)
    ax.plot(angles, values, color='#ff6600', linewidth=2)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    
    st.pyplot(fig)

if st.button("Raporu Yazdır / PDF Yap"):
    st.info("Tarayıcınızın Yazdır (Ctrl+P veya Cmd+P) özelliğini kullanarak raporu PDF olarak kaydedebilirsiniz.")
