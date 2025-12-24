import streamlit as st
import os, base64, time, random

# --- 1. AYARLAR VE PROFESYONEL TASARIM ---
st.set_page_config(page_title="Elif-Ba Akademi", page_icon="🌙", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap');
    
    /* Ana Arka Plan */
    .stApp {
        background: linear-gradient(to bottom, #f0f8ff, #e6e9f0);
    }

    /* Arapça Harf Kutusu */
    .arapca-kutu {
        text-align: center; 
        font-size: 180px; 
        background-color: #ffffff; 
        border: 4px solid #d4af37; /* Altın Sarısı Çerçeve */
        border-radius: 30px; 
        padding: 40px;
        color: #2c3e50; 
        font-family: 'Amiri', serif;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15); /* Derinlik Gölgesi */
        direction: rtl; 
        line-height: 1.2; 
        margin-bottom: 30px;
        transition: transform 0.3s ease; /* Animasyon */
    }
    
    /* Kutuya mouse gelince büyüme efekti */
    .arapca-kutu:hover {
        transform: scale(1.02);
        box-shadow: 0 15px 35px rgba(212, 175, 55, 0.3);
    }

    /* İlerleme Çubuğu Rengi */
    .stProgress > div > div > div > div {
        background-color: #27ae60; /* İslami Yeşil */
    }

    /* Buton Stilleri */
    .stButton > button {
        border-radius: 12px;
        font-weight: bold;
        border: none;
        transition: 0.3s;
    }
    </style>
    """, unsafe_allow_html=True)

if "bolum" not in st.session_state:
    st.session_state.update({"bolum": "1. Yalın Harfler", "alt_adim": 0, "calindi": ""})

# --- DEBUG: DOSYA KONTROLÜ ---
with st.sidebar:
    st.title("🌙 Akademi Paneli")
    if os.path.exists("sesler"):
        dosyalar = os.listdir("sesler")
        st.success(f"✅ Sistem Aktif: {len(dosyalar)} ders dosyası yüklü.")
    else:
        st.error("🚨 HATA: 'sesler' klasörü bulunamadı!")

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
        st.warning(f"⚠️ Ses Dosyası Eksik: {dosya_adi}.mp3")

# --- 3. MÜFREDAT (10 Seviye Tam Liste) ---
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
        {"h": "اَ", "s": "e"}, {"h": "بَ", "s": "be_ustun"}, {"h": "تَ", "s": "te_ustun"}, {"h": "ثَ", "s": "se_ustun"},
        {"h": "جَ", "s": "cim_ustun"}, {"h": "حَ", "s": "ha_ustun"}, {"h": "خَ", "s": "hi_ustun"}, {"h": "دَ", "s": "dal_ustun"},
        {"h": "ذَ", "s": "zel_ustun"}, {"h": "رَ", "s": "re_ustun"}, {"h": "زَ", "s": "ze_ustun"}, {"h": "سَ", "s": "sin_ustun"},
        {"h": "شَ", "s": "sin_noktali_ustun"}, {"h": "صَ", "s": "sad_ustun"}, {"h": "ضَ", "s": "dad_ustun"}, {"h": "طَ", "s": "ti_ustun"},
        {"h": "ظَ", "s": "zi_ustun"}, {"h": "عَ", "s": "ayin_ustun"}, {"h": "غَ", "s": "gayin_ustun"}, {"h": "فَ", "s": "fe_ustun"},
        {"h": "قَ", "s": "kaf_ustun"}, {"h": "كَ", "s": "kef_ustun"}, {"h": "لَ", "s": "lam_ustun"}, {"h": "مَ", "s": "mim_ustun"},
        {"h": "نَ", "s": "nun_ustun"}, {"h": "وَ", "s": "vav_ustun"}, {"h": "هَ", "s": "he_ustun"}, {"h": "يَ", "s": "ye_ustun"}
    ],
    "3. Esre (İ-I)": [
        {"h": "اِ", "s": "i_ince"}, {"h": "بِ", "s": "be_esre"}, {"h": "تِ", "s": "te_esre"}, {"h": "ثِ", "s": "se_esre"},
        {"h": "جِ", "s": "cim_esre"}, {"h": "حِ", "s": "ha_esre"}, {"h": "خِ", "s": "hi_esre"}, {"h": "دِ", "s": "dal_esre"},
        {"h": "ذِ", "s": "zel_esre"}, {"h": "رِ", "s": "re_esre"}, {"h": "زِ", "s": "ze_esre"}, {"h": "سِ", "s": "sin_esre"},
        {"h": "شِ", "s": "sin_noktali_esre"}, {"h": "صِ", "s": "sad_esre"}, {"h": "ضِ", "s": "dad_esre"}, {"h": "طِ", "s": "ti_esre"},
        {"h": "ظِ", "s": "zi_esre"}, {"h": "عِ", "s": "ayin_esre"}, {"h": "غِ", "s": "gayin_esre"}, {"h": "فِ", "s": "fe_esre"},
        {"h": "قِ", "s": "kaf_esre"}, {"h": "كِ", "s": "kef_esre"}, {"h": "لِ", "s": "lam_esre"}, {"h": "مِ", "s": "mim_esre"},
        {"h": "نِ", "s": "nun_esre"}, {"h": "وِ", "s": "vav_esre"}, {"h": "هِ", "s": "he_esre"}, {"h": "يِ", "s": "ye_esre"}
    ],
    "4. Ötre (Ü-U)": [
        {"h": "اُ", "s": "u_otre"}, {"h": "بُ", "s": "bu_otre"}, {"h": "تُ", "s": "tu_otre"}, {"h": "ثُ", "s": "se_otre"},
        {"h": "جُ", "s": "cim_otre"}, {"h": "حُ", "s": "ha_otre"}, {"h": "خُ", "s": "hi_otre"}, {"h": "دُ", "s": "dal_otre"},
        {"h": "ذُ", "s": "zel_otre"}, {"h": "رُ", "s": "re_otre"}, {"h": "زُ", "s": "ze_otre"}, {"h": "سُ", "s": "sin_otre"},
        {"h": "شُ", "s": "sin_noktali_otre"}, {"h": "صُ", "s": "sad_otre"}, {"h": "ضُ", "s": "dad_otre"}, {"h": "طُ", "s": "ti_otre"},
        {"h": "ظُ", "s": "zi_otre"}, {"h": "عُ", "s": "ayin_otre"}, {"h": "غُ", "s": "gayin_otre"}, {"h": "فُ", "s": "fe_otre"},
        {"h": "قُ", "s": "kaf_otre"}, {"h": "كُ", "s": "kef_otre"}, {"h": "لُ", "s": "lam_otre"}, {"h": "مُ", "s": "mim_otre"},
        {"h": "نُ", "s": "nun_otre"}, {"h": "وُ", "s": "vav_otre"}, {"h": "هُ", "s": "he_otre"}, {"h": "يُ", "s": "ye_otre"}
    ],
    "5. Cezm (Birleştirme)": [
        {"h": "اَبْ", "s": "eb_cezm"}, {"h": "اَتْ", "s": "et_cezm"}, {"h": "اَثْ", "s": "es_p_cezm"},
        {"h": "اَجْ", "s": "ec_cezm"}, {"h": "اَحْ", "s": "eh_cezm"}, {"h": "اَخْ", "s": "eh_k_cezm"},
        {"h": "اَدْ", "s": "ed_cezm"}, {"h": "اَذْ", "s": "ez_p_cezm"}, {"h": "اَرْ", "s": "er_cezm"},
        {"h": "اَزْ", "s": "ez_cezm"}, {"h": "اَسْ", "s": "es_cezm"}, {"h": "اَشْ", "s": "es_sh_cezm"},
        {"h": "اَصْ", "s": "es_sad_cezm"}, {"h": "اَضْ", "s": "ed_dad_cezm"}, {"h": "اَطْ", "s": "et_ti_cezm"},
        {"h": "اَظْ", "s": "ez_zi_cezm"}, {"h": "اَعْ", "s": "ea_cezm"}, {"h": "اَغْ", "s": "eg_cezm"},
        {"h": "اَفْ", "s": "ef_cezm"}, {"h": "اَقْ", "s": "ek_kaf_cezm"}, {"h": "اَكْ", "s": "ek_kef_cezm"},
        {"h": "اَلْ", "s": "el_cezm"}, {"h": "اَمْ", "s": "em_cezm"}, {"h": "اَنْ", "s": "en_cezm"},
        {"h": "اَوْ", "s": "ev_cezm"}, {"h": "اَهْ", "s": "eh_he_cezm"}, {"h": "اَىْ", "s": "ey_cezm"}
    ],
    "6. Şedde (Çift Okuma)": [
        {"h": "اَبَّ", "s": "eb_be_sedde"}, {"h": "اَتَّ", "s": "et_te_sedde"}, {"h": "اَثَّ", "s": "es_se_p_sedde"},
        {"h": "اَجَّ", "s": "ec_ce_sedde"}, {"h": "اَحَّ", "s": "eh_ha_sedde"}, {"h": "اَخَّ", "s": "eh_hi_sedde"},
        {"h": "اَدَّ", "s": "ed_de_sedde"}, {"h": "اَذَّ", "s": "ez_zel_sedde"}, {"h": "اَرَّ", "s": "er_ra_sedde"},
        {"h": "اَزَّ", "s": "ez_ze_sedde"}, {"h": "اَسَّ", "s": "es_se_sedde"}, {"h": "اَشَّ", "s": "es_sa_sedde"},
        {"h": "اَصَّ", "s": "es_sad_sedde"}, {"h": "اَضَّ", "s": "ed_dad_sedde"}, {"h": "اَطَّ", "s": "et_ti_sedde"},
        {"h": "اَظَّ", "s": "ez_zi_sedde"}, {"h": "اَعَّ", "s": "ea_ayin_sedde"}, {"h": "اَغَّ", "s": "eg_gayin_sedde"},
        {"h": "اَفَّ", "s": "ef_fe_sedde"}, {"h": "اَقَّ", "s": "ek_kaf_sedde"}, {"h": "اَكَّ", "s": "ek_kef_sedde"},
        {"h": "اَلَّ", "s": "el_lam_sedde"}, {"h": "اَمَّ", "s": "em_mim_sedde"}, {"h": "اَنَّ", "s": "en_nun_sedde"},
        {"h": "اَوَّ", "s": "ev_vav_sedde"}, {"h": "اَهَّ", "s": "eh_he_sedde"}, {"h": "اَيَّ", "s": "ey_ye_sedde"}
    ],
    "7. Tenvin (İki Üstün - En/An)": [
        {"h": "اً", "s": "elif_tenvin"}, {"h": "بً", "s": "be_tenvin"}, {"h": "تً", "s": "te_tenvin"}, {"h": "ثً", "s": "se_p_tenvin"},
        {"h": "جً", "s": "cim_tenvin"}, {"h": "حً", "s": "ha_tenvin"}, {"h": "خً", "s": "hi_tenvin"}, {"h": "دً", "s": "dal_tenvin"},
        {"h": "ذً", "s": "zel_p_tenvin"}, {"h": "رً", "s": "ra_tenvin"}, {"h": "زً", "s": "ze_tenvin"}, {"h": "سً", "s": "sin_tenvin"},
        {"h": "شً", "s": "sin_n_tenvin"}, {"h": "صً", "s": "sad_tenvin"}, {"h": "ضً", "s": "dad_tenvin"}, {"h": "طً", "s": "ti_tenvin"},
        {"h": "ظً", "s": "zi_p_tenvin"}, {"h": "عً", "s": "ayin_tenvin"}, {"h": "غً", "s": "gayin_tenvin"}, {"h": "فً", "s": "fe_tenvin"},
        {"h": "قً", "s": "kaf_tenvin"}, {"h": "كً", "s": "kef_tenvin"}, {"h": "لً", "s": "lam_tenvin"}, {"h": "مً", "s": "mim_tenvin"},
        {"h": "نً", "s": "nun_tenvin"}, {"h": "وً", "s": "vav_tenvin"}, {"h": "هً", "s": "he_tenvin"}, {"h": "يً", "s": "ye_tenvin"}
    ],
    "8. Tenvin (İki Esre - İn/In)": [
        {"h": "اٍ", "s": "elif_tenvin_esre"}, {"h": "بٍ", "s": "be_tenvin_esre"}, {"h": "تٍ", "s": "te_tenvin_esre"}, {"h": "ثٍ", "s": "se_p_tenvin_esre"},
        {"h": "جٍ", "s": "cim_tenvin_esre"}, {"h": "حٍ", "s": "ha_tenvin_esre"}, {"h": "خٍ", "s": "hi_tenvin_esre"}, {"h": "دٍ", "s": "dal_tenvin_esre"},
        {"h": "ذٍ", "s": "zel_p_tenvin_esre"}, {"h": "رٍ", "s": "ra_tenvin_esre"}, {"h": "زٍ", "s": "ze_tenvin_esre"}, {"h": "سٍ", "s": "sin_tenvin_esre"},
        {"h": "شٍ", "s": "sin_n_tenvin_esre"}, {"h": "صٍ", "s": "sad_tenvin_esre"}, {"h": "ضٍ", "s": "dad_tenvin_esre"}, {"h": "طٍ", "s": "ti_tenvin_esre"},
        {"h": "ظٍ", "s": "zi_p_tenvin_esre"}, {"h": "عٍ", "s": "ayin_tenvin_esre"}, {"h": "غٍ", "s": "gayin_tenvin_esre"}, {"h": "فٍ", "s": "fe_tenvin_esre"},
        {"h": "قٍ", "s": "kaf_tenvin_esre"}, {"h": "كٍ", "s": "kef_tenvin_esre"}, {"h": "لٍ", "s": "lam_tenvin_esre"}, {"h": "مٍ", "s": "mim_tenvin_esre"},
        {"h": "نٍ", "s": "nun_tenvin_esre"}, {"h": "وٍ", "s": "vav_tenvin_esre"}, {"h": "هٍ", "s": "he_tenvin_esre"}, {"h": "يٍ", "s": "ye_tenvin_esre"}
    ],
    "9. Tenvin (İki Ötre - Ün/Un)": [
        {"h": "اٌ", "s": "elif_tenvin_otre"}, {"h": "بٌ", "s": "be_tenvin_otre"}, {"h": "تٌ", "s": "te_tenvin_otre"}, {"h": "ثٌ", "s": "se_p_tenvin_otre"},
        {"h": "جٌ", "s": "cim_tenvin_otre"}, {"h": "حٌ", "s": "ha_tenvin_otre"}, {"h": "خٌ", "s": "hi_tenvin_otre"}, {"h": "دٌ", "s": "dal_tenvin_otre"},
        {"h": "ذٌ", "s": "zel_p_tenvin_otre"}, {"h": "رٌ", "s": "ra_tenvin_otre"}, {"h": "زٌ", "s": "ze_tenvin_otre"}, {"h": "سٌ", "s": "sin_tenvin_otre"},
        {"h": "شٌ", "s": "sin_n_tenvin_otre"}, {"h": "صٌ", "s": "sad_tenvin_otre"}, {"h": "ضٌ", "s": "dad_tenvin_otre"}, {"h": "طٌ", "s": "ti_tenvin_otre"},
        {"h": "ظٌ", "s": "zi_p_tenvin_otre"}, {"h": "عٌ", "s": "ayin_tenvin_otre"}, {"h": "غٌ", "s": "gayin_tenvin_otre"}, {"h": "فٌ", "s": "fe_tenvin_otre"},
        {"h": "قٌ", "s": "kaf_tenvin_otre"}, {"h": "كٌ", "s": "kef_tenvin_otre"}, {"h": "لٌ", "s": "lam_tenvin_otre"}, {"h": "مٌ", "s": "mim_tenvin_otre"},
        {"h": "نٌ", "s": "nun_tenvin_otre"}, {"h": "وٌ", "s": "vav_tenvin_otre"}, {"h": "هٌ", "s": "he_tenvin_otre"}, {"h": "يٌ", "s": "ye_tenvin_otre"}
    ],
    "10. Med Harfi Elif (Uzatma)": [
        {"h": "اَا", "s": "elif_med"}, {"h": "بَا", "s": "be_med"}, {"h": "تَا", "s": "te_med"}, {"h": "ثَا", "s": "se_p_med"},
        {"h": "جَا", "s": "cim_med"}, {"h": "حَا", "s": "ha_med"}, {"h": "خَا", "s": "hi_med"}, {"h": "دَا", "s": "dal_med"},
        {"h": "ذَا", "s": "zel_p_med"}, {"h": "رَا", "s": "ra_med"}, {"h": "زَا", "s": "ze_med"}, {"h": "سَا", "s": "sin_med"},
        {"h": "شَا", "s": "sin_n_med"}, {"h": "صَا", "s": "sad_med"}, {"h": "ضَا", "s": "dad_med"}, {"h": "طَا", "s": "ti_med"},
        {"h": "ظَا", "s": "zi_p_med"}, {"h": "عَا", "s": "ayin_med"}, {"h": "غَا", "s": "gayin_med"}, {"h": "فَا", "s": "fe_med"},
        {"h": "قَا", "s": "kaf_med"}, {"h": "كَا", "s": "kef_med"}, {"h": "لَا", "s": "lam_med"}, {"h": "مَا", "s": "mim_med"},
        {"h": "نَا", "s": "nun_med"}, {"h": "وَا", "s": "vav_med"}, {"h": "هَا", "s": "he_med"}, {"h": "يَا", "s": "ye_med"}
    ]
}

# --- 4. ARAYÜZ VE TEST MODU ---
with st.sidebar:
    st.title("🌙 Akademi Paneli")
    
    # Bölüm Seçimi
    secilen = st.selectbox("Ders Seçin:", list(mufredat.keys()))
    
    if secilen != st.session_state.bolum:
        st.session_state.bolum = secilen
        st.session_state.alt_adim = 0
        st.session_state.calindi = ""
        if "test_liste" in st.session_state:
            del st.session_state["test_liste"]
        st.rerun()

    st.divider()
    # Test Modu
    test_modu = st.checkbox("🎯 Hızlı Test Modu (Karışık)")
    
    st.divider()
    # Puan Durumu
    puan = st.session_state.get('puan', 0)
    st.markdown(f"""
        <div style="background-color:#27ae60; padding:10px; border-radius:10px; text-align:center; color:white;">
            <strong>🏆 Toplam Puan:</strong><br>
            <span style="font-size:24px;">{puan}</span>
        </div>
    """, unsafe_allow_html=True)

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
    
    # Arapça Kutusu
    st.markdown(f'<div class="arapca-kutu">{mevcut["h"]}</div>', unsafe_allow_html=True)
    
    # Otomatik Ses
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
    st.success(f"🎉 Tebrikler! {st.session_state.bolum} tamamlandı.")
    st.info(f"Toplam Puanınız: {st.session_state.get('puan', 0)}")
    if st.button("🔄 Başa Dön", use_container_width=True):
        st.session_state.alt_adim = 0
        if "test_liste" in st.session_state:
            del st.session_state["test_liste"]
        st.rerun()
