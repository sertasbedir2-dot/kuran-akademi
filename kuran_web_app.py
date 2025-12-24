import streamlit as st
import os, base64, time, random

# --- 1. AYARLAR VE CSS TASARIMI (HARFLER İÇİN BALYOZ YÖNTEMİ) ---
st.set_page_config(page_title="Elif-Ba Akademi", page_icon="🌙", layout="centered")

st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Amiri:wght@400;700&display=swap');
    
    /* Ana Arka Plan */
    .stApp {
        background: linear-gradient(to bottom, #fdfbf7, #e6e9f0);
    }

    /* --- BUTON TASARIMLARI --- */

    /* 1. TÜM BUTONLAR GENEL AYAR */
    .stButton > button {
        border-radius: 20px;
        border: 3px solid #d4af37;
        transition: 0.2s;
        width: 100%;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }

    /* 2. BEYAZ BUTONLAR (ARAPÇA HARFLERİN OLDUĞU KUTULAR) */
    /* Primary (Kırmızı) olmayan butonları hedefler */
    .stButton > button:not([kind="primary"]) {
        background-color: white;
        color: #2c3e50;
        height: 160px !important; /* Yükseklik sabitlendi */
        padding: 0px !important;
        display: flex;
        align-items: center;
        justify-content: center;
    }

    /* BALYOZ: Harfleri Zorla Büyüt */
    .stButton > button:not([kind="primary"]) * {
        font-family: 'Amiri', serif !important;
        font-size: 95px !important;  /* DEVASA HARF BOYUTU */
        line-height: 1.2 !important;
        font-weight: bold !important;
        margin: 0 !important;
        padding-top: 10px !important; /* Görsel ortalama */
    }

    /* Beyaz Buton Hover */
    .stButton > button:not([kind="primary"]):hover {
        background-color: #fcf3cf; 
        border-color: #b7950b;
        transform: scale(1.02);
    }

    /* Beyaz Buton Focus (Renk takılmasını önler) */
    .stButton > button:not([kind="primary"]):focus:not(:active) {
        background-color: white !important;
        border-color: #d4af37 !important;
        color: #2c3e50 !important;
        box-shadow: none !important;
    }

    /* 3. KIRMIZI BUTONLAR (KONTROL: İLERİ / TEKRAR DİNLE) */
    .stButton > button[kind="primary"] {
        background-color: #ff4b4b !important;
        color: white !important;
        border: none !important;
        height: 70px !important;
    }
    
    /* Kırmızı butonun içindeki yazıyı normal boyutta tut */
    .stButton > button[kind="primary"] * {
        font-family: sans-serif !important;
        font-size: 24px !important;
        line-height: normal !important;
    }

    /* Kırmızı Buton Hover */
    .stButton > button[kind="primary"]:hover {
        background-color: #ff3333 !important;
        transform: scale(1.03);
        box-shadow: 0 5px 15px rgba(255, 75, 75, 0.4);
    }

    /* Kırmızı Buton Focus */
    .stButton > button[kind="primary"]:focus:not(:active) {
        background-color: #ff4b4b !important;
        color: white !important;
        box-shadow: none !important;
    }

    /* Çalışma Modu Gösterge Kutusu */
    .arapca-kutu {
        text-align: center; 
        font-size: 180px; 
        background-color: #ffffff; 
        border: 4px solid #d4af37; 
        border-radius: 30px; 
        padding: 40px;
        color: #2c3e50; 
        font-family: 'Amiri', serif;
        box-shadow: 0 10px 30px rgba(0,0,0,0.15);
        direction: rtl; 
        line-height: 1.2; 
        margin-bottom: 30px;
    }

    /* İlerleme Çubuğu Rengi */
    .stProgress > div > div > div > div {
        background-color: #27ae60; 
    }
    </style>
    """, unsafe_allow_html=True)

# Session State Başlatma
if "bolum" not in st.session_state:
    st.session_state.update({
        "bolum": "1. Yalın Harfler", 
        "alt_adim": 0, 
        "calindi": "", 
        "quiz_hedef": None,
        "quiz_secenekler": [],
        "puan": 0
    })

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
        # Ses dosyası yoksa hata verme, sessizce geç
        pass

# --- 3. MÜFREDAT ---
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
    ],
    "11. Med Harfi Ye (İnce Uzatma)": [
        {"h": "اِي", "s": "elif_med_ye"}, {"h": "بِي", "s": "be_med_ye"}, {"h": "تِي", "s": "te_med_ye"}, {"h": "ثِي", "s": "se_p_med_ye"},
        {"h": "جِي", "s": "cim_med_ye"}, {"h": "حِي", "s": "ha_med_ye"}, {"h": "خِي", "s": "hi_med_ye"}, {"h": "دِي", "s": "dal_med_ye"},
        {"h": "ذِي", "s": "zel_p_med_ye"}, {"h": "رِي", "s": "ra_med_ye"}, {"h": "زِي", "s": "ze_med_ye"}, {"h": "سِي", "s": "sin_med_ye"},
        {"h": "شِي", "s": "sin_n_med_ye"}, {"h": "صِي", "s": "sad_med_ye"}, {"h": "ضِي", "s": "dad_med_ye"}, {"h": "طِي", "s": "ti_med_ye"},
        {"h": "ظِي", "s": "zi_p_med_ye"}, {"h": "عِي", "s": "ayin_med_ye"}, {"h": "غِي", "s": "gayin_med_ye"}, {"h": "فِي", "s": "fe_med_ye"},
        {"h": "قِي", "s": "kaf_med_ye"}, {"h": "كِي", "s": "kef_med_ye"}, {"h": "لِي", "s": "lam_med_ye"}, {"h": "مِي", "s": "mim_med_ye"},
        {"h": "نِي", "s": "nun_med_ye"}, {"h": "وِي", "s": "vav_med_ye"}, {"h": "هِي", "s": "he_med_ye"}, {"h": "يِي", "s": "ye_med_ye"}
    ],
    "12. Med Harfi Vav (Ötreli Uzatma)": [
        {"h": "اُو", "s": "elif_med_vav"}, {"h": "بُو", "s": "be_med_vav"}, {"h": "تُو", "s": "te_med_vav"}, {"h": "ثُو", "s": "se_p_med_vav"},
        {"h": "جُو", "s": "cim_med_vav"}, {"h": "حُو", "s": "ha_med_vav"}, {"h": "خُو", "s": "hi_med_vav"}, {"h": "دُو", "s": "dal_med_vav"},
        {"h": "ذُو", "s": "zel_p_med_vav"}, {"h": "رُو", "s": "ra_med_vav"}, {"h": "زُو", "s": "ze_med_vav"}, {"h": "سُو", "s": "sin_med_vav"},
        {"h": "شُو", "s": "sin_n_med_vav"}, {"h": "صُو", "s": "sad_med_vav"}, {"h": "ضُو", "s": "dad_med_vav"}, {"h": "طُو", "s": "ti_med_vav"},
        {"h": "ظُو", "s": "zi_p_med_vav"}, {"h": "عُو", "s": "ayin_med_vav"}, {"h": "غُو", "s": "gayin_med_vav"}, {"h": "فُو", "s": "fe_med_vav"},
        {"h": "قُو", "s": "kaf_med_vav"}, {"h": "كُو", "s": "kef_med_vav"}, {"h": "لُو", "s": "lam_med_vav"}, {"h": "مُو", "s": "mim_med_vav"},
        {"h": "نُو", "s": "nun_med_vav"}, {"h": "وُو", "s": "vav_med_vav"}, {"h": "هُو", "s": "he_med_vav"}, {"h": "يُو", "s": "ye_med_vav"}
    ]
}

# --- 4. ARAYÜZ ---
with st.sidebar:
    st.title("🌙 Akademi Paneli")
    
    # Bölüm Seçimi
    secilen = st.selectbox("Ders Seçin:", list(mufredat.keys()))
    
    if secilen != st.session_state.bolum:
        st.session_state.bolum = secilen
        st.session_state.alt_adim = 0
        st.session_state.calindi = ""
        st.session_state.quiz_hedef = None # Mod değişirse quiz sıfırla
        st.rerun()

    st.divider()
    
    # MOD SEÇİMİ
    mod = st.radio("Mod Seçimi:", ["📖 Çalışma Modu", "🎮 Sınav Modu (Quiz)"])
    
    st.divider()
    # Puan Durumu
    puan = st.session_state.get('puan', 0)
    st.markdown(f"""
        <div style="background-color:#27ae60; padding:10px; border-radius:10px; text-align:center; color:white;">
            <strong>🏆 Toplam Puan:</strong><br>
            <span style="font-size:24px;">{puan}</span>
        </div>
    """, unsafe_allow_html=True)
    
    # İMZA KISMI (Burayı düzenlemeyi unutma!)
    st.divider()
    st.info("👨‍💻 Geliştirici: SERTAŞ BEDİR \n\n 📅 Versiyon: 1.3 (Final Gold)")


# --- ANA EKRAN MANTIĞI ---
ders_listesi = mufredat[st.session_state.bolum]

# ================================
# MOD 1: ÇALIŞMA MODU
# ================================
if mod == "📖 Çalışma Modu":
    st.subheader(f"📖 {st.session_state.bolum}")
    
    if st.session_state.alt_adim < len(ders_listesi):
        mevcut = ders_listesi[st.session_state.alt_adim]
        st.progress((st.session_state.alt_adim + 1) / len(ders_listesi))
        
        # Arapça Kutusu
        st.markdown(f'<div class="arapca-kutu">{mevcut["h"]}</div>', unsafe_allow_html=True)
        
        # Otomatik Ses
        ident = f"{st.session_state.bolum}_{st.session_state.alt_adim}"
        if st.session_state.calindi != ident:
            sesi_cal(mevcut['s'])
            st.session_state.calindi = ident

        c1, c2 = st.columns(2)
        with c1:
            if st.button("🔊 Tekrar Dinle", use_container_width=True, type="primary"): 
                sesi_cal(mevcut['s'])
                
        with c2:
            if st.button("➡️ Sonraki Harf", use_container_width=True, type="primary"):
                st.session_state.alt_adim += 1
                st.session_state.puan += 5 # Çalışma puanı
                st.rerun()
    else:
        st.balloons()
        st.success(f"🎉 Tebrikler! {st.session_state.bolum} tamamlandı.")
        if st.button("🔄 Başa Dön", use_container_width=True, type="primary"):
            st.session_state.alt_adim = 0
            st.rerun()

# ================================
# MOD 2: SINAV MODU (QUIZ OYUNU)
# ================================
else:
    st.subheader(f"🎮 Sesi Bul: {st.session_state.bolum}")
    st.info("🔊 Sesi dinle ve doğru harfi bul!")
    
    # Yeni soru oluştur
    if st.session_state.quiz_hedef is None:
        hedef = random.choice(ders_listesi)
        # Yanlış seçenekler (Kendisi hariç 2 tane)
        yanlislar = random.sample([x for x in ders_listesi if x != hedef], 2)
        secenekler = [hedef] + yanlislar
        random.shuffle(secenekler)
        
        st.session_state.quiz_hedef = hedef
        st.session_state.quiz_secenekler = secenekler
        
        # Sesi Çal
        sesi_cal(hedef['s'])

    # Sesi Tekrar Çal Butonu (Kırmızı)
    if st.button("🔊 Sesi Tekrar Dinle", use_container_width=True, type="primary"):
        sesi_cal(st.session_state.quiz_hedef['s'])

    st.write("") # Boşluk

    # Seçenekleri Göster (3 Buton Yan Yana)
    cols = st.columns(3)
    for i, secenek in enumerate(st.session_state.quiz_secenekler):
        with cols[i]:
            # Beyaz butonlar (CSS ile harfler devasa yapıldı)
            if st.button(secenek["h"], key=f"q_{i}", use_container_width=True):
                if secenek == st.session_state.quiz_hedef:
                    st.balloons()
                    st.success("✅ DOĞRU CEVAP!")
                    st.session_state.puan += 20
                    time.sleep(1) # Kutlama süresi
                    st.session_state.quiz_hedef = None # Yeni soru için sıfırla
                    st.rerun()
                else:
                    st.error("❌ Yanlış, tekrar dene!")
                    st.session_state.puan = max(0, st.session_state.puan - 5)
