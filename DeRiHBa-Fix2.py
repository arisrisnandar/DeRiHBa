import cv2
import numpy as np

########################################################################################
import argparse
#Modul argparse mempermudah menuliskan antarmuka baris perintah (command-line).
########################################################################################
import imutils
#imutils
#Serangkaian fungsi yang memudahkan untuk membuat fungsi dasar image processing 
#seperti: terjemahan, rotasi, pengubahan ukuran, skeletonization.
#Tapi untuk menampilkan gambar, juga bisa dengan Matplotlib lebih mudah bersinergi 
#dengan OpenCV dan Python 2.7 dan Python 3.
########################################################################################
import time
#untuk menangani tugas yang berhubungan dengan waktu
########################################################################################
########################################################################################
import os
#import adalah kata kunci dalam Python yang memungkinkan kita menggunakan kode 
#dari file Python yang berbeda, baik yang ditulis oleh Anda atau orang lain.
#Dalam hal ini kami mengimpor modul yang disertakan dengan Python 
#pada modul sistem operasi (os).
#import OS memberi  banyak fungsi, kelas, dll yang berhubungan dengan 
#sistem operasi #seperti menampilkan isi direktori, mendapatkan ukuran file, 
#dan sejumlah operasi lainnya.
##############################

cap = cv2.VideoCapture(0)

while(1):

    # Pilih setiap frame yang akan dibuat dalam 3 frame
    _, frame = cap.read()

    # Konversi warna RGB ke HSV (BGR to HSV)
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Definisi range warna kematangan pisang tanduk (HSV)
    #define_riped_banana_color = np.array([threshold,minimum,maksimum])
    lower_ripe = np.array([20,100,100])
    upper_ripe = np.array([30,255,255])
    lower_unripe = np.array([50,100,100])
    upper_unripe = np.array([80,255,255])

    # Threshold the HSV image 
    # untuk nilai mentah dan matang terendah & tertinggi 
    #warna matang terendah & tertinggi
    mask1 = cv2.inRange(hsv, lower_ripe, upper_ripe)
    #warna mentah terendah & tertinggi
    mask2 = cv2.inRange(hsv, lower_unripe, upper_unripe)
    
    # Proses masking Bitwise-AND mask dan gambar original 
    res1 = cv2.bitwise_and(frame,frame, mask=mask1)
    res2 = cv2.bitwise_and(frame,frame, mask=mask2)
       
    kuning = np.count_nonzero(mask1)
    hijau = np.count_nonzero(mask2)     
    
    
    if(kuning>hijau):
        if(kuning-hijau>12000):
            print("Sangat Matang [Grade: 7+]")
            label = "Sangat Matang [Grade: 7+]" 
            cv2.putText(frame, "Sangat Matang [Grade: 7+]", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
            #cv2.putText(frame, "Sangat Matang [Grade: 7+]", (10, text_offset_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        elif(kuning-hijau>6500):
            print("Matang [Grade: 6]")
            label = "Matang [Grade: 6]"
            cv2.putText(frame, "Matang [Grade: 6]", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
            #cv2.putText(frame, "Matang [Grade: 6]", (10, text_offset_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        elif(kuning-hijau>6000):
            print("Cukup/Hampir Matang [Grade: 5]")
            label = "Cukup/Hampir Matang [Grade: 5]"
            #cv2.putText(frame, "Cukup/Hampir Matang [Grade: 5]", (10, text_offset_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
            cv2.putText(frame, "Cukup/Hampir Matang [Grade: 5]", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        elif(kuning-hijau>3500):
            print("Kurang Matang [Grade: 4]")
            label = "Kurang Matang [Grade: 4]"
            #cv2.putText(frame, "Kurang Matang [Grade: 4]", (10, text_offset_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
            cv2.putText(frame, "Kurang Matang [Grade: 4]", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        elif(kuning-hijau>350):
            print("Mentah [Grade: 3]")
            label = "Mentah [Grade: 3]"
            cv2.putText(frame, 'Mentah [Grade: 3]', (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        elif(kuning-hijau>15):
            print("Sangat Mentah [Grade: 2]")
            label = "Sangat Mentah [Grade: 2]"
            # set the text start position
            text_offset_x = 10
            text_offset_y = frame.shape[0] - 25
            #make the coords of the box with a small padding of two pixels
            #box_coords = ((text_offset_x, text_offset_y), (text_offset_x + text_width + 2, text_offset_y - text_height - 2))
            #cv2.rectangle(img, box_coords[0], box_coords[1], rectangle_bgr, cv2.FILLED)
            #cv2.putText(img, text, (text_offset_x, text_offset_y), font, fontScale=font_scale, color=(0, 0, 0), thickness=1)
            #cv2.putText(frame, "Sangat Mentah [Grade: 2]", (text_offset_x, text_offset_y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 255, 255))
            #cv2.putText(frame, "Sangat Mentah [Grade: 2]", (10, text_offset_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
            cv2.putText(frame, "Sangat Mentah [Grade: 2]", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
    else:
        print("Sangat Mentah [Grade: 1]")
        label = "Sangat Mentah [Grade: 1]"
        cv2.putText(frame, "Sangat Mentah [Grade: 1]", (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        #cv2.putText(frame, "Sangat Mentah [Grade: 1]", (10, text_offset_y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255))
        #Show results
        # tampilkan hasilnya pada frame

    cv2.imshow('De RiBa=Detector of Riped Banana  (Q/q=keluar)',frame)
    #cv2.imshow('Original', frame)
    cv2.imshow('res1',res1)
    cv2.imshow('res2',res2)
    
    key = cv2.waitKey(1) & 0xFF
    # tekan tombol "q" atau "Q" untuk keluar
    if key == ord("q") or key == ord("Q"):
        break
cv2.destroyAllWindows()