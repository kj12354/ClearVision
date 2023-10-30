import cv2
import pytesseract
from gtts import gTTS
import os
import spacy

# Load the spaCy English model
nlp = spacy.load("en_core_web_sm")


# Function to extract text from a video frame
def extract_text_from_frame(frame):
    # Perform OCR on the frame to extract text
    text = pytesseract.image_to_string(frame)
    return text


# Function to process and convert text to speech
def text_to_speech(text):
    # Process text with spaCy
    doc = nlp(text)

    # Extract and join only the recognized entities
    entities = " ".join(entity.text for entity in doc.ents)

    tts = gTTS(entities, lang='en')
    tts.save('output.mp3')
    os.system('start output.mp3')  # Adjust for your operating system's audio player


if __name__ == "__main__":
    # Initialize the video capture from a camera
    capture = cv2.VideoCapture(0)

    while True:
        ret, frame = capture.read()  # Read a frame from the camera

        if not ret:
            print("Error capturing a frame from the camera.")
            break

        # Extract text from the frame
        extracted_text = extract_text_from_frame(frame)

        if extracted_text:
            print("Extracted Text: ", extracted_text)
            text_to_speech(extracted_text)

        # Display the video feed
        cv2.imshow('Text Reader', frame)

        if not cv2.waitKey(1) & 0xFF != ord('q'):
            break

    # Release the video capture and close all OpenCV windows
    capture.release()
    cv2.destroyAllWindows()


# Scapy Packet Sniffing Function
def packet_sniffer(pkt):
    if ARP in pkt:
        print("ARP Packet Detected: ", pkt.summary())


# Start packet sniffing
sniff(filter="arp", prn=packet_sniffer)
