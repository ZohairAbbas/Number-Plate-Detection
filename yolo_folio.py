from detect import run
import easyocr
import cv2
import os
import numpy as np
from detecto import core, utils
import functools


def detectandread(img_source):
    run(weights='runs/train/exp/weights/best.pt', imgsz=(640, 640),
        conf_thres=0.6, source="static/" + img_source, save_crop=True)

    folder_count = 0  # type: int

    input_path = "runs/detect"  # type: str
    for folders in os.listdir(input_path):
        folder_count += 1  # increment counter

    print("\n\nThere are {0} folders\n\n".format(folder_count))

    if folder_count == 1:
        folder_count = ''

    # EasyOCR

    plate = []
    path = 'runs/detect/exp' + str(folder_count) + '/crops/number plate/'
    for ann_path in os.listdir(path):
        img = cv2.imread(path + ann_path, 0)
        region_threshold = 0.1
        # Full image dimensions
        width = img.shape[1]
        height = img.shape[0]

        # Apply ROI filtering and OCR

        roi = [height, width, height, width]
        reader = easyocr.Reader(['en'])
        ocr_result = reader.readtext(img)

        rectangle_size = img.shape[0] * img.shape[1]

        for result in ocr_result:
            length = np.sum(np.subtract(result[0][1], result[0][0]))
            height = np.sum(np.subtract(result[0][2], result[0][1]))

            if length * height / rectangle_size > region_threshold:
                plate.append(result[1])

    print("\n\nEasyOCR results: \nNumber Plate: {}\n\n".format(plate))

    # Detecto

    model = core.Model.load('model_weights.pth', ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
                                                  'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])

    # inference on test images
    plate1 = []

    def compare(rect1, rect2):
        if abs(rect1[1] - rect2[1]) > 30:
            return rect1[1] - rect2[1]
        else:
            return rect1[0] - rect2[0]

    for ann_path in os.listdir(path):
        image = utils.read_image(path + ann_path)
        image = cv2.resize(image, (800, 700))

        kernel = np.array([[0, -1, 0], [-1, 3, -1], [0, 1, 0]])
        image = cv2.filter2D(src=image, ddepth=-1, kernel=kernel)
        predictions = model.predict(image)
        labels, boxes, scores = predictions
        thresh = 0.75
        filtered_indices = np.where(scores > thresh)
        filtered_boxes = boxes[filtered_indices]
        num_list = filtered_indices[0].tolist()
        filtered_labels = [labels[i] for i in num_list]

    boundingBoxes = sorted(filtered_boxes, key=functools.cmp_to_key(compare))

    summ = 0
    for rect in filtered_boxes:
        x, y, w, h = rect
        summ += h

    length = len(filtered_boxes)
    avgh = summ // length

    results = ''
    for box in boundingBoxes:
        x, y, w, h = box
        for i in range(0, len(filtered_boxes)):

            x2, y2, w2, h2 = filtered_boxes[i]
            if(x == x2 and y == y2):
                results = results + filtered_labels[i]

    plate1.append(results)

    print("\n\nCustom Model results: \nNumber Plate: {}\n\n".format(plate1))
    return plate, plate1
