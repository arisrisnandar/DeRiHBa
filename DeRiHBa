import streamlit as st
import cv2
import numpy as np
from PIL import Image
import tempfile

st.set_page_config(page_title="De RiBa - Detector of Riped Banana", page_icon="🍌")

st.title("🍌 De RiBa - Detector of Riped Banana")
st.markdown("### Aplikasi Deteksi Tingkat Kematangan Pisang")

# Sumber gambar
source = st.radio("Pilih sumber gambar:", ["Upload Gambar", "Gunakan Kamera"])

def detect_banana(image):
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    
    lower_ripe = np.array([20, 100, 100])
    upper_ripe = np.array([30, 255, 255])
    lower_unripe = np.array([50, 100, 100])
    upper_unripe = np.array([80, 255, 255])
    
    mask_ripe = cv2.inRange(hsv, lower_ripe, upper_ripe)
    mask_unripe = cv2.inRange(hsv, lower_unripe, upper_unripe)
    
    ripe_pixels = np.count_nonzero(mask_ripe)
    unripe_pixels = np.count_nonzero(mask_unripe)
    
    # Tentukan tingkat kematangan
    if ripe_pixels > unripe_pixels:
        diff = ripe_pixels - unripe_pixels
        if diff > 12000:
            label = "Sangat Matang [Grade: 7+]"
        elif diff > 6500:
            label = "Matang [Grade: 6]"
        elif diff > 6000:
            label = "Cukup/Hampir Matang [Grade: 5]"
        elif diff > 3500:
            label = "Kurang Matang [Grade: 4]"
        elif diff > 350:
            label = "Mentah [Grade: 3]"
        elif diff > 15:
            label = "Sangat Mentah [Grade: 2]"
        else:
            label = "Sangat Mentah [Grade: 1]"
    else:
        label = "Sangat Mentah [Grade: 1]"
    
    result = image.copy()
    cv2.putText(result, label, (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2)
    
    return result, mask_ripe, mask_unripe, label, ripe_pixels, unripe_pixels

if source == "Upload Gambar":
    uploaded = st.file_uploader("Pilih gambar pisang...", type=['jpg', 'jpeg', 'png'])
    if uploaded:
        bytes_data = uploaded.getvalue()
        image = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Gambar Asli")
        
        if st.button("Deteksi Kematangan"):
            result, mask1, mask2, label, ripe, unripe = detect_banana(image)
            
            with col2:
                st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption="Hasil Deteksi")
            
            st.success(f"**Hasil:** {label}")
            colm1, colm2 = st.columns(2)
            colm1.metric("Piksel Matang", f"{ripe:,}")
            colm2.metric("Piksel Mentah", f"{unripe:,}")

else:  # Kamera
    img = st.camera_input("Ambil foto pisang")
    if img:
        bytes_data = img.getvalue()
        image = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)
        
        result, mask1, mask2, label, ripe, unripe = detect_banana(image)
        
        col1, col2 = st.columns(2)
        with col1:
            st.image(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), caption="Gambar Asli")
        with col2:
            st.image(cv2.cvtColor(result, cv2.COLOR_BGR2RGB), caption="Hasil Deteksi")
        
        st.success(f"**Hasil:** {label}")
        colm1, colm2 = st.columns(2)
        colm1.metric("Piksel Matang", f"{ripe:,}")
        colm2.metric("Piksel Mentah", f"{unripe:,}")

st.markdown("---")
st.info("**Grade Kematangan:** 1-2: Sangat Mentah | 3: Mentah | 4: Kurang Matang | 5: Cukup Matang | 6: Matang | 7+: Sangat Matang")
