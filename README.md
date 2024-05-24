# Automatic Toll Tax Deduction Using License Plate Detection
The objective of our project is to automate the toll tax collecting procedure through the use of licence plate detection technologies. This method improves toll-collecting operations' efficiency by doing away with the necessity for human toll payments.
## Key Components
1. **License Plate Recognition (LPR):** License Plate Recognition (LPR) makes it possible for licence plates to be automatically detected and recognised. LPR systems take video snapshots of passing cars at toll plazas using cameras and by using object detection algorithms and OCR technologies, they decode the licence plate from the frames of the video. With the use of this technology, cars may be identified without the need for human interaction or stoppage, resulting in a smooth and effective toll tax deduction procedure.
   
2. **Aadhar Linkage:** Our method assumes the vehicle RC (Registration Certificate) number to be linked with Aadhar. The Income-tax Act makes it mandatory for every PAN card holder to intimate his Aadhar Number so that the Aadhar and PAN can be linked. Therefore by linking the RC numbers to Aadhar, we can directly deduct money from one’s bank account as soon as their vehicle passes a toll road. It also enables us to confirm the identities of vehicle owners and keep a centralised database of toll transactions, thereby guaranteeing accuracy and accountability in toll tax deductions.

3. **Bank Account Deduction:** The method deducts appropriate toll tax from the associated bank account after detecting the licence plate and linking it to Aadhar. To ensure the quick and precise processing of toll payments, bank account deduction is enabled via secure electronic payment channels.
   
## Workflow
1. **Licence Plate Detection:** The LPR system takes video of the lane for fixed intervals (10-15 seconds) without any gap. While recording for the next interval, the current recording is then processed frame by frame (60 fps) to recognise the vehicles passing in that duration (using the YOLO object detection algorithm) and then extracting the license plate text of that vehicle (using the OCR algorithms). The license plate texts are processed to remove false positives and duplicate records and then stored in a CSV file.

2. **Bank Account Selection:** The CSV file is then passed on to the vehicle records to get the associated Aadhar number and then select the bank account to deduct the respective toll amount from it.
   
3. **Toll Amount Deduction:** After obtaining the bank account number, the toll amount is deducted from it corresponding to the type of vehicle (for example: car, motorcycle, bus, truck etc.) since each vehicle type has a different toll amount.

## Requirements:
1. Python3.12.2 2. mysql8.3.0
3. Googlecolab
4. Pythonlibraries:
  - filterpy
  - scikit-image
  - lap
  - easyocr
  - ultralytics
  - roboflow
  - shutil
  - pandas
  - mysql.connector
  - opencv-python
  - csv
  - faker
6. Pgadmin4
7. PostgresSQL16
8. Postman
9. Django

## Algorithms Used
1. **YOLOv8 (You Only Look Once):** The YOLO model’s 8th version is renowned for its real-time performance and high accuracy. With the use of anchor boxes (bounding boxes for objects of different shapes and sizes) and multi-scale prediction (detect objects of different sizes and aspect ratios effectively) in a deep convolutional neural network architecture, YOLOv8 predicts bounding boxes and class probabilities at the same time, processing whole pictures in a single pass. In the project, the COCO (Common Objects in Context) dataset is used to train the YOLO model which is used to detect vehicles in the video frames. The model is further trained with a license plate dataset which is used to detect license plates from the detected vehicles.
    
2. **EasyOCR:** EasyOCR is a Python library that offers a simple and effective way to extract text from pictures. It requires very little setup and preparation to reliably detect and recognise text in a variety of languages and fonts through the use of optical character recognition (OCR) techniques combined with deep learning models. In the project, EasyOCR is used to recognise the text from the detected license plates along with the confidence scores.

3. **SORT (Simple Online and Realtime Tracking):** SORT is a real-time tracking algorithm for 2D multiple object tracking in video sequences. It is designed for online tracking applications where only past and current frames are available and the method produces object identities on the fly. The algorithm is used to track the vehicles in different frames and assigns them an identity which is later used to club the actual license plate text amongst the predicted ones.
