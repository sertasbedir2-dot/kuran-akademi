import streamlit as st
import os, base64, time, random

# --- 1. AYARLAR ---
st.set_page_config(page_title="Elif-Ba Akademi", page_icon="📖", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap');
    .arapca-kutu {
        text-align:center; font-size:200px; background-color:#f8f9fa; 
        border: 4px solid #2E86C1; border-radius:25px; padding:30px;
        color: #1A5276; font-family: 'Amiri', serif;
        box-shadow: 0 10px 20px rgba(0,0,0,0.1);
        direction: rtl; line-height: 1.1; margin-bottom: 20px;
    }
    .stProgress > div > div > div > div { background-color: #2E86C1; }
    </style>
    """, unsafe_allow_html=True)

if "bolum" not in st.session_state:
    st.session_state.update({"bolum": "1. Yalın Harfler", "alt_adim": 0, "calindi": ""})

# --- DEBUG: DOSYA KONTROLÜ ---
with st.sidebar:
    st.title("🌙 Akademi Paneli")
    if os.path.exists("sesler"):
        dosyalar = os.listdir("sesler")
        st.success(f"Sistem Hazır: {len(dosyalar)} ses dosyası.")
    else:
        st.error("HATA: 'sesler' klasörü yok!")

# --- 2. SES MOTORU ---
def sesi_cal(dosya_adi):
    yol = os.path.join("sesler", f"{dosya_adi}.mp3")
    if os.path.exists(yol):
        with open(yol, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            unique_timestamp = int(time.time() * 1000)
            st.markdown(f'<audio autoplay key="a_{unique_timestamp}"><source src="data:audio/mp3;base64,{b64}#t={unique_timestamp}" type="audio/mp3"></audio>', unsafe_allow_html=True)
    else:
        st.warning(f"⚠️ Dosya Bulunamadı: {dosya_adi}.mp3")

# --- 3. MÜFREDAT (Dosyalarla Uyumlu) ---
mufredat = {
    "1. Yalın Harfler": [
        {"h": "ا", "s": "elif"}, {"h": "ب", "s": "be"}, {"h": "ت", "s": "te"}, {"h": "ث", "s": "se"},
        {"h": "ج", "s": "cim"}, {"h": "ح", "s": "ha"}, {"h": "خ", "s": "hi"}, {"h": "د", "s": "dal"},
        {"h": "ذ", "s": "zel_p"}, {"h": "ر", "s": "re"}, {"h": "ز", "s": "ze_k"}, {"h": "س", "s": "sin"},
        {"h": "ش", "s": "sin_n"}, {"h": "ص", "s": "sad"}, {"h": "ض", "s": "dad"}, {"h": "ط", "s": "ti_k"},
        {"h": "ظ", "s": "zi_p"}, {"h": "ع", "s": "ayin"}, {"h": "غ", "s": "gayin"}, {"h": "ف", "s": "fe"},
        {"h": "ق", "s": "kaf"}, {"h": "ك", "s": "kef"}, {"h": "ل", "s": "lam"}, {"h": "م", "s": "mim"},
        {"h": "ن", "s": "nun"}, {"h": "و", "s": "vav"}, {"h": "ه", "s": "he"}, {"h": "ي", "s": "ye"}
    ],
    "2. Üstün (E-A)": [
        {"h": "اَ", "s": "e"}, 
        {"h": "بَ", "s": "be_ustun"}, {"h": "تَ", "s": "te_ustun"}, {"h": "ثَ", "s": "se_ustun"},
        {"h": "جَ", "s": "cim_ustun"}, {"h": "حَ", "s": "ha_ustun"}, {"h": "خَ", "s": "hi_ustun"}, {"h": "دَ", "s": "dal_ustun"},
        {"h": "ذَ", "s": "zel_ustun"}, {"h": "رَ", "s": "re_ustun"}, {"h": "زَ", "s": "ze_ustun"}, {"h": "سَ", "s": "sin_ustun"},
        {"h": "شَ", "s": "sin_noktali_ustun"}, {"h": "صَ", "s": "sad_ustun"}, {"h": "ضَ", "s": "dad_ustun"}, {"h": "طَ", "s": "ti_ustun"},
        {"h": "ظَ", "s": "zi_ustun"}, {"h": "عَ", "s": "ayin_ustun"}, {"h": "غَ", "s": "gayin_ustun"}, {"h": "فَ", "s": "fe_ustun"},
        {"h": "قَ", "s": "kaf_ustun"}, {"h": "كَ", "s": "kef_ustun"}, {"h": "لَ", "s": "lam_ustun"}, {"h": "مَ", "s": "mim_ustun"},
        {"h": "نَ", "s": "nun_ustun"}, {"h": "وَ", "s": "vav_ustun"}, {"h": "هَ", "s": "he_ustun"}, {"h": "يَ", "s": "ye_ustun"}
    ],
    "3. Esre (İ-I)": [
        {"h": "اِ", "s": "i_ince"}, 
        {"h": "بِ", "s": "be_esre"}, {"h": "تِ", "s": "te_esre"}, {"h": "ثِ", "s": "se_esre"},
        {"h": "جِ", "s": "cim_esre"}, {"h": "حِ", "s": "ha_esre"}, {"h": "خِ", "s": "hi_esre"}, {"h": "دِ", "s": "dal_esre"},
        {"h": "ذِ", "s": "zel_esre"}, {"h": "رِ", "s": "re_esre"}, {"h": "زِ", "s": "ze_esre"}, {"h": "سِ", "s": "sin_esre"},
        {"h": "شِ", "s": "sin_noktali_esre"}, {"h": "صِ", "s": "sad_esre"}, {"h": "ضِ", "s": "dad_esre"}, {"h": "طِ", "s": "ti_esre"},
        {"h": "ظِ", "s": "zi_esre"}, {"h": "عِ", "s": "ayin_esre"}, {"h": "غِ", "s": "gayin_esre"}, {"h": "فِ", "s": "fe_esre"},
        {"h": "قِ", "s": "kaf_esre"}, {"h": "كِ", "s": "kef_esre"}, {"h": "لِ", "s": "lam_esre"}, {"h": "مِ", "s": "mim_esre"},
        {"h": "نِ", "s": "nun_esre"}, {"h": "وِ", "s": "vav_esre"}, {"h": "هِ", "s": "he_esre"}, {"h": "يِ", "s": "ye_esre"}
    ],
    "4. Ötre (Ü-U)": [
        {"h": "اُ", "s": "u_otre"}, 
        {"h": "بُ", "s": "bu_otre"}, {"h": "تُ", "s": "tu_otre"}, {"h": "ثُ", "s": "su_p_otre"},
        {"h": "جُ", "s": "cim_otre"}, {"h": "حُ", "s": "ha_otre"}, {"h": "خُ", "s": "hi_otre"}, {"h": "دُ", "s": "dal_otre"},
        {"h": "ذُ", "s": "zel_otre"}, {"h": "رُ", "s": "re_otre"}, {"h": "زُ", "s": "ze_otre"}, {"h": "سُ", "s": "sin_otre"},
        {"h": "شُ", "s": "sin_noktali_otre"}, {"h": "صُ", "s": "sad_otre"}, {"h": "ضُ", "s": "dad_otre"}, {"h": "طُ", "s": "ti_otre"},
        {"h": "ظُ", "s": "zi_otre"}, {"h": "عُ", "s": "ayin_otre"}, {"h": "غُ", "s": "gayin_otre"}, {"h": "فُ", "s": "fe_otre"},
        {"h": "قُ", "s": "kaf_otre"}, {"h": "كُ", "s": "kef_otre"}, {"h": "لُ", "s": "lam_otre"}, {"h": "مُ", "s": "mim_otre"},
        {"h": "نُ", "s": "nun_otre"}, {"h": "وُ", "s": "vav_otre"}, {"h": "هُ", "s": "he_otre"}, {"h": "يُ", "s": "ye_otre"}
    ]
}

# --- 4. ARAYÜZ VE TEST MODU ---
with st.sidebar:
    st.title("🌙 Akademi Paneli")
    secilen = st.selectbox("Ders Seçin:", list(mufredat.keys()))
    
    # Bölüm değişirse sıfırla
    if secilen != st.session_state.bolum:
        st.session_state.bolum = secilen
        st.session_state.alt_adim = 0
        st.session_state.calindi = ""
        # Test listesini temizle
        if "test_liste" in st.session_state:
            del st.session_state["test_liste"]
        st.rerun()

    st.divider()
    test_modu = st.checkbox("🎯 Hızlı Test Modu (Karışık Sor)")
    st.divider()
    st.success(f"Puan: {st.session_state.get('puan', 0)}")

# --- ANA EKRAN MANTIĞI ---
standart_liste = mufredat[st.session_state.bolum]

if test_modu:
    if "test_liste" not in st.session_state:
        st.session_state.test_liste = standart_liste.copy()
        random.shuffle(st.session_state.test_liste)
        st.session_state.alt_adim = 0
        
    liste = st.session_state.test_liste
    baslik_ek = " (KARIŞIK MOD)"
else:
    liste = standart_liste
    if "test_liste" in st.session_state:
        del st.session_state["test_liste"]
        st.session_state.alt_adim = 0
    baslik_ek = ""

if st.session_state.alt_adim < len(liste):
    mevcut = liste[st.session_state.alt_adim]
    
    st.subheader(f"📖 {st.session_state.bolum}{baslik_ek}")
    st.progress((st.session_state.alt_adim + 1) / len(liste))
    
    st.markdown(f'<div class="arapca-kutu">{mevcut["h"]}</div>', unsafe_allow_html=True)
    
    # --- DEĞİŞİKLİK BURADA: Her durumda otomatik çal ---
    ident = f"{st.session_state.bolum}_{st.session_state.alt_adim}"
    if st.session_state.calindi != ident:
        sesi_cal(mevcut['s'])
        st.session_state.calindi = ident

    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔊 Tekrar Dinle", use_container_width=True): 
            sesi_cal(mevcut['s'])
            
    with c2:
        if st.button("➡️ Sonraki Harf", use_container_width=True, type="primary"):
            st.session_state.alt_adim += 1
            if test_modu:
                st.session_state.puan = st.session_state.get('puan', 0) + 10
            st.rerun()
else:
    st.balloons()
    st.success(f"Bölüm Tamamlandı! Toplam Puan: {st.session_state.get('puan', 0)}")
    if st.button("🔄 Başa Dön", use_container_width=True):
        st.session_state.alt_adim = 0
        if "test_liste" in st.session_state:
            del st.session_state["test_liste"]
        st.rerun()
