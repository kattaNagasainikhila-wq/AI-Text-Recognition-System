import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

image = cv2.imread("sample.jpeg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

text = pytesseract.image_to_string(gray)
data = pytesseract.image_to_data(gray, output_type=pytesseract.Output.DICT)

confidences = []

for conf in data["conf"]:
    try:
        conf = int(conf)
        if conf > 0:
            confidences.append(conf)
    except:
        pass

if len(confidences) > 0:
    avg_conf = sum(confidences)/len(confidences)
    print(f"\nConfidence Score: {avg_conf:.2f}%")

print("\nExtracted Text:\n")
print(text)

with open("output.txt","w",encoding="utf-8") as file:
    file.write(text)

print("\nText saved successfully!")