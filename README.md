# Number Plate Detection
This project aims to detect number plate of a vehicle in a image or video and extract the number plate text using Optical Character Recognation(OCR). This system is implemented by using [yolov5](https://github.com/ultralytics/yolov5 "yolov5"), [EasyOCR](https://github.com/JaidedAI/EasyOCR "EasyOCR") and a Custom OCR model. 

## 📚 Dataset
The dataset used to train [yolov5](https://github.com/ultralytics/yolov5 "yolov5") dectection :  

[Pakistan Vehicle Number Plate Dataset](https://github.com/usmanweb/Pakistan-Vehicle-Number-Plate-Dataset "Pakistan Vehicle Number Plate Dataset")

[Pakistani_Vehicle_Dataset_SAZ](https://www.kaggle.com/datasets/abdulazizbaig/pakistani-vehicle-dataset-saz-vrs "Pakistani_Vehicle_Dataset_SAZ")

[Labeled licence plates dataset](https://www.kaggle.com/datasets/achrafkhazri/labeled-licence-plates-dataset "Labeled Licence Plate Dataset")

Used [Roboflow](https://roboflow.com/ "Roboflow") to annotate/label our data.

## 🛠️ Installation & Usage

1. Clone the repository

```bash
git clone https://github.com/ZohairAbbas/Number-Plate-Detection.git
```

2. Change the working directory

```bash
cd Number-Plate-Detection
```

3. Install dependencies

```bash
pip install -r requirements.txt
```

4. Run the app

```bash
python -m uvicorn api:app --reload
```

## 🔭 Project architecture

The pipeline in the project is as follows:  

- Train custom data using [yolov5](https://github.com/ultralytics/yolov5 "yolov5")
- Custom number plate detection using [yolov5](https://github.com/ultralytics/yolov5 "yolov5") and saving plates as cropped images
- Apply the extracted plate to [EasyOCR](https://github.com/JaidedAI/EasyOCR "EasyOCR") and Custom OCR
- Get plates-text in an array format
- Integeration of FastAPI

## 💎 Results

![images](https://github.com/ZohairAbbas/Number-Plate-Detection/blob/main/data/111.jpeg) 


## 🤝 Contributors 
<a href="https://github.com/ZohairAbbas/Number-Plate-Detection/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ZohairAbbas/Number-Plate-Detection" />
</a>





