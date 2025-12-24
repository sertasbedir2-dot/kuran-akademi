import streamlit as st
import os, base64, time

# --- 1. AYARLAR VE GÖRSEL TASARIM ---
st.set_page_config(page_title="Elif-Ba Akademi", page_icon="📖", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap');
    .arapca-kutu {
        text-align:center; 
        font-size:200px; 
        background-color:#f8f9fa; 
        border: 4px solid #2E86C1;
        border-radius:25px; 
        padding:30px;
        color: #1A5276;
        font-family: 'Amiri', serif;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        direction: rtl;
        line-height: 1.1;
        margin-bottom: 20px;
    }
    .stProgress > div > div > div > div {
        background-color: #2E86C1;
    }
    </style>
    """, unsafe_allow_html=True)

if "bolum" not in st.session_state:
    st.session_state.update({"bolum": "1. Yalın Harfler", "alt_adim": 0, "calindi": ""})

def sesi_cal(dosya_adi):
    yol = os.path.join("sesler", f"{dosya_adi}.mp3")
    if os.path.exists(yol):
        with open(yol, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            unique_timestamp = int(time.time() * 1000)
            audio_html = f'<audio autoplay key="a_{unique_timestamp}"><source src="data:audio/mp3;base64,{b64}#t={unique_timestamp}" type="audio/mp3"></audio>'
            st.markdown(audio_html, unsafe_allow_html=True)
    else:
        st.warning(f"🔈 Ses bulunamadı: {dosya_adi}.mp3")

# --- 3. MÜFREDAT (YÜKLEDİĞİNİZ İSİMLERLE EŞLEŞTİRİLDİ) ---
mufredat = {
    "1. Yalın Harfler": [
        {"h": "ا", "s": "elif"}, {"h": "ب", "s": "be"}, {"h": "ت", "s": "te"}, {"h": "ث", "s": "se"},
        {"h": "ج", "s": "cim"}, {"h": "ح", "s": "ha"}, {"h": "خ", "s": "hi"}, {"h": "د", "s": "dal"},
        {"h": "ذ", "s": "zel"}, {"h": "ر", "s": "re"}, {"h": "ز", "s": "ze"}, {"h": "س", "s": "sin"},
        {"h": "ش", "s": "şın"}, {"h": "ص", "s": "sad"}, {"h": "ض", "s": "dad"}, {"h": "ط", "s": "ti"},
        {"h": "ظ", "s": "zi"}, {"h": "ع", "s": "ayin"}, {"h": "غ", "s": "gayin"}, {"h": "ف", "s": "fe"},
        {"h": "ق", "s": "kaf"}, {"h": "ك", "s": "kef"}, {"h": "ل", "s": "lam"}, {"h": "م", "s": "mim"},
        {"h": "ن", "s": "nun"}, {"h": "و", "s": "vav"}, {"h": "ه", "s": "he"}, {"h": "ي", "s": "ye"}
    ],
    "2. Üstün (E-A)": [
        {"h": "اَ", "s": "e"}, {"h": "بَ", "s": "be_u"}, {"h": "تَ", "s": "te_u"}, {"h": "ثَ", "s": "se_u"}
        # Listeyi bu mantıkla (be_u, te_u) diğer harfler için de manuel tamamlayabilirsin.
    ],
    "3. Esre (İ-I)": [
        {"h": "اِ", "s": "i"}, {"h": "بِ", "s": "bi"}, {"h": "تِ", "s": "ti"}, {"h": "ثِ", "s": "si_p"}
    ],
    "4. Ötre (Ü-U)": [
        {"h": "اُ", "s": "u"}, {"h": "بُ", "s": "bu"}, {"h": "تُ", "s": "tu"}, {"h": "ثُ", "s": "su_p"}
    ]
}

# --- ARAYÜZ ---
with st.sidebar:
    st.title("🌙 Akademi Paneli")
    secilen = st.selectbox("Ders Seçin:", list(mufredat.keys()))
    if secilen != st.session_state.bolum:
        st.session_state.bolum = secilen
        st.session_state.alt_adim = 0
        st.session_state.calindi = ""
        st.rerun()
    st.divider()
    st.success(f"Puan: {st.session_state.get('puan', 0)}")

liste = mufredat[st.session_state.bolum]
if st.session_state.alt_adim < len(liste):
    mevcut = liste[st.session_state.alt_adim]
    st.progress((st.session_state.alt_adim + 1) / len(liste))
    st.markdown(f'<div class="arapca-kutu">{mevcut["h"]}</div>', unsafe_allow_html=True)
    
    ident = f"{st.session_state.bolum}_{st.session_state.alt_adim}"
    if st.session_state.calindi != ident:
        sesi_cal(mevcut['s'])
        st.session_state.calindi = ident

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔊 Tekrar Dinle", use_container_width=True): sesi_cal(mevcut['s'])
    with c2:
        if st.button("➡️ Sonraki", use_container_width=True):
            st.session_state.alt_adim += 1
            st.session_state.puan = st.session_state.get('puan', 0) + 10
            st.rerun()
else:
    st.balloons()
    st.success("Tebrikler!")
    if st.button("Tekrarla"):
        st.session_state.alt_adim = 0
        st.rerun()
