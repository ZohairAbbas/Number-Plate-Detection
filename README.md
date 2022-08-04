# Number Plate Detection

## 📚 Dataset
The dataset used to train yolov5 dectection :  

[Pakistan Vehicle Number Plate Dataset](https://github.com/usmanweb/Pakistan-Vehicle-Number-Plate-Dataset "Pakistan Vehicle Number Plate Dataset")

[Pakistani_Vehicle_Dataset_SAZ](https://www.kaggle.com/datasets/abdulazizbaig/pakistani-vehicle-dataset-saz-vrs "Pakistani_Vehicle_Dataset_SAZ")

[Labeled licence plates dataset](https://www.kaggle.com/datasets/achrafkhazri/labeled-licence-plates-dataset "Labeled Licence Plate Dataset")



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

- Train custom data using yolov5
- Custom number plate detection using yolov5 and saving plates as cropped images
- Apply the extracted plate to EasyOCR and Custom OCR
- Get plates-text in an array format
- Integeration of FastAPI






