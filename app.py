import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Sayfa Yapısı - Mobil uyum için padding düzenlendi
st.set_page_config(page_title="ACS Analysis Lab", layout="wide")

st.markdown("""
    <style>
    /* Mobil için butonları büyüt ve touch dostu yap */
    div.stButton > button {
        width: 100%;
        height: 3em;
        background-color: #ff6600 !important;
        font-weight: bold;
    }
    /* Sidebar genişliğini mobil için optimize et */
    [data-testid="stSidebar"] {
        min-width: 320px;
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

# Mobilde daha rahat giriş için alt alta düzen
st.sidebar.write("**Güncel Skorlar**")
m2 = st.sidebar.number_input("Mekanik (Güncel)", 1, 10, 7)
k2 = st.sidebar.number_input("Karar (Güncel)", 1, 10, 7)
d2 = st.sidebar.number_input("Denge (Güncel)", 1, 10, 7)
b2 = st.sidebar.number_input("Baskı (Güncel)", 1, 10, 7)
o2 = st.sidebar.number_input("Okuma (Güncel)", 1, 10, 7)

st.sidebar.divider()
st.sidebar.write("**Başlangıç Skorları**")
m1 = st.sidebar.number_input("Mekanik (Başlangıç)", 1, 10, 5)
k1 = st.sidebar.number_input("Karar (Başlangıç)", 1, 10, 5)
d1 = st.sidebar.number_input("Denge (Başlangıç)", 1, 10, 5)
b1 = st.sidebar.number_input("Baskı (Başlangıç)", 1, 10, 5)
o1 = st.sidebar.number_input("Okuma (Başlangıç)", 1, 10, 5)

notes = st.sidebar.text_area("Teknik Değerlendirme", "Gelişim reçetesi...")

# Ana Panel
col1, col2 = st.columns([1, 1.2])

with col1:
    st.subheader("Sporcu Profili")
    st.write(f"**İsim:** {name} | **Pozisyon:** {pos}")
    st.write(f"**Tarih:** {pd.Timestamp.now().strftime('%d/%m/%Y')}")
    st.info(f"**Notlar:** {notes}")

with col2:
    st.subheader("Gelişim Karşılaştırma Grafiği")
    
    categories = ['Mekanik', 'Karar Hızı', 'Denge', 'Baskı', 'Okuma']
    
    # Plotly Radar Chart (Mobil dostu ve interaktif)
    fig = go.Figure()

    fig.add_trace(go.Scatterpolar(
          r=[m1, k1, d1, b1, o1, m1],
          theta=categories + [categories[0]],
          fill='toself',
          name='Başlangıç',
          line_color='#777777',
          fillcolor='rgba(119, 119, 119, 0.1)'
    ))
    
    fig.add_trace(go.Scatterpolar(
          r=[m2, k2, d2, b2, o2, m2],
          theta=categories + [categories[0]],
          fill='toself',
          name='Güncel',
          line_color='#ff6600',
          fillcolor='rgba(255, 102, 0, 0.3)'
    ))

    fig.update_layout(
      polar=dict(
        radialaxis=dict(visible=True, range=[0, 10])
      ),
      showlegend=True,
      margin=dict(l=40, r=40, t=20, b=20), # Mobil kenar boşlukları
      paper_bgcolor='rgba(0,0,0,0)',
      plot_bgcolor='rgba(0,0,0,0)'
    )

    st.plotly_chart(fig, use_container_width=True)

if st.button("Raporu PDF Kaydet"):
    st.info("Mobil cihazınızda 'Paylaş > Yazdır' diyerek PDF olarak kaydedebilirsiniz.")
