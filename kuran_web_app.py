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

# Hafıza Yönetimi
if "bolum" not in st.session_state:
    st.session_state.update({"bolum": "1. Yalın Harfler", "alt_adim": 0, "calindi": ""})

# --- 2. SES ÇALMA FONKSİYONU (Daha Dayanıklı Versiyon) ---
def sesi_cal(dosya_adi):
    yol = os.path.join("sesler", f"{dosya_adi}.mp3")
    if os.path.exists(yol):
        with open(yol, "rb") as f:
            data = f.read()
            b64 = base64.b64encode(data).decode()
            # unique_id yanına milisaniye ekleyerek tarayıcıyı her seferinde tazelemeye zorluyoruz
            unique_timestamp = int(time.time() * 1000)
            audio_html = f"""
                <audio autoplay key="audio_{unique_timestamp}">
                    <source src="data:audio/mp3;base64,{b64}#t={unique_timestamp}" type="audio/mp3">
                </audio>
            """
            st.markdown(audio_html, unsafe_allow_html=True)
    else:
        st.warning(f"🔈 Ses dosyası bulunamadı: {dosya_adi}.mp3")

# --- 3. TAM MÜFREDAT (GitHub'daki Mevcut Dosya İsimlerinize Göre Düzenlendi) ---
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
        {"h": "اَ", "s": "e"}, {"h": "بَ", "s": "be_ust"}, {"h": "تَ", "s": "te_ust"}, {"h": "ثَ", "s": "se_ust"},
        {"h": "جَ", "s": "ce"}, {"h": "حَ", "s": "ha_ust"}, {"h": "خَ", "s": "ha_k"}, {"h": "دَ", "s": "de"},
        {"h": "ذَ", "s": "zel_ust"}, {"h": "رَ", "s": "ra"}, {"h": "زَ", "s": "ze_ust"}, {"h": "سَ", "s": "se_u2"},
        {"h": "شَ", "s": "sin_n_ust"}, {"h": "صَ", "s": "sa"}, {"h": "ضَ", "s": "da"}, {"h": "طَ", "s": "ta"},
        {"h": "ظَ", "s": "za"}, {"h": "عَ", "s": "ayin_ust"}, {"h": "غَ", "s": "ga"}, {"h": "فَ", "s": "fe_ust"},
        {"h": "قَ", "s": "ka"}, {"h": "كَ", "s": "ke"}, {"h": "لَ", "s": "le"}, {"h": "مَ", "s": "me"},
        {"h": "نَ", "s": "ne"}, {"h": "وَ", "s": "ve"}, {"h": "هَ", "s": "he_ust"}, {"h": "يَ", "s": "ye_ust"}
    ],
    "3. Esre (İ-I)": [
        {"h": "اِ", "s": "i_ince"}, {"h": "بِ", "s": "bi_esre"}, {"h": "تِ", "s": "ti_esre"}, {"h": "ثِ", "s": "si_p_esre"},
        {"h": "جِ", "s": "ci_esre"}, {"h": "حِ", "s": "hi_esre"}, {"h": "خِ", "s": "khi_esre"}, {"h": "دِ", "s": "di_esre"},
        {"h": "ذِ", "s": "zi_p_esre"}, {"h": "رِ", "s": "ri_esre"}, {"h": "زِ", "s": "zi_esre"}, {"h": "سِ", "s": "si_esre"},
        {"h": "شِ", "s": "shi_esre"}, {"h": "صِ", "s": "si_k_esre"}, {"h": "ضِ", "s": "di_k_esre"}, {"h": "طِ", "s": "ti_k_esre"},
        {"h": "ظِ", "s": "zi_k_esre"}, {"h": "عِ", "s": "i_u_esre"}, {"h": "غِ", "s": "gi_esre"}, {"h": "فِ", "s": "fi_esre"},
        {"h": "قِ", "s": "ki_k_esre"}, {"h": "كِ", "s": "ki_esre"}, {"h": "لِ", "s": "li_esre"}, {"h": "مِ", "s": "mi_esre"},
        {"h": "نِ", "s": "ni_esre"}, {"h": "وِ", "s": "vi_esre"}, {"h": "هِ", "s": "hi_u2_esre"}, {"h": "يِ", "s": "yi_esre"}
    ],
    "4. Ötre (Ü-U)": [
        {"h": "اُ", "s": "u_otre"}, {"h": "بُ", "s": "bu_otre"}, {"h": "تُ", "s": "tu_otre"}, {"h": "ثُ", "s": "su_p_otre"},
        {"h": "جُ", "s": "cu_otre"}, {"h": "حُ", "s": "hu_u_otre"}, {"h": "خُ", "s": "hu_k_otre"}, {"h": "دُ", "s": "du_otre"},
        {"h": "ذُ", "s": "zu_p_otre"}, {"h": "رُ", "s": "ru_otre"}, {"h": "زُ", "s": "zu_otre"}, {"h": "سُ", "s": "su_otre"},
        {"h": "شُ", "s": "shu_otre"}, {"h": "صُ", "s": "su_k_otre"}, {"h": "ضُ", "s": "du_k_otre"}, {"h": "طُ", "s": "tu_k_otre"},
        {"h": "ظُ", "s": "zu_k_otre"}, {"h": "عُ", "s": "u_u_otre"}, {"h": "غُ", "s": "gu_otre"}, {"h": "فُ", "s": "fu_otre"},
        {"h": "قُ", "s": "ku_k_otre"}, {"h": "كُ", "s": "ku_otre"}, {"h": "لُ", "s": "lu_otre"}, {"h": "مُ", "s": "mu_otre"},
        {"h": "نُ", "s": "nu_otre"}, {"h": "وُ", "s": "vu_otre"}, {"h": "هُ", "s": "hu_u2_otre"}, {"h": "يُ", "s": "yu_otre"}
    ]
}

# --- 4. YAN MENÜ ---
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
    st.info("💡 Ses gelmezse 'Tekrar Dinle'ye basın. Tarayıcılar bazen ilk girişte sesi engeller.")

# --- 5. ANA EKRAN ---
liste = mufredat[st.session_state.bolum]

if st.session_state.alt_adim < len(liste):
    mevcut = liste[st.session_state.alt_adim]
    
    st.subheader(f"📖 {st.session_state.bolum}")
    st.progress((st.session_state.alt_adim + 1) / len(liste))
    
    # Harf Kutusu
    st.markdown(f'<div class="arapca-kutu">{mevcut["h"]}</div>', unsafe_allow_html=True)
    
    # Otomatik Ses Kontrolü
    ident = f"{st.session_state.bolum}_{st.session_state.alt_adim}"
    if st.session_state.calindi != ident:
        sesi_cal(mevcut['s'])
        st.session_state.calindi = ident

    # Butonlar
    c1, c2 = st.columns(2)
    with c1:
        if st.button("🔊 Tekrar Dinle", use_container_width=True):
            sesi_cal(mevcut['s'])
    with c2:
        is_last = st.session_state.alt_adim == len(liste) - 1
        btn_label = "🏁 Bölümü Bitir" if is_last else "➡️ Sonraki Harf"
        
        if st.button(btn_label, use_container_width=True, type="primary" if is_last else "secondary"):
            st.session_state.alt_adim += 1
            if "puan" not in st.session_state: st.session_state.puan = 0
            st.session_state.puan += 10
            st.rerun()
else:
    st.balloons()
    st.success(f"🎊 Tebrikler! {st.session_state.bolum} dersini başarıyla bitirdiniz.")
    st.write(f"Bu bölümden kazandığınız puan: {len(liste) * 10}")
    
    if st.button("Bölümü Sıfırla ve Tekrarla 🔄", use_container_width=True):
        st.session_state.alt_adim = 0
        st.session_state.calindi = ""
        st.rerun()

