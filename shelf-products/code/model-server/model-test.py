import PIL.Image as Image
from ultralytics import YOLO

# create main method
if __name__ == '__main__':
    # Load your YOLOv8
    model = YOLO('../yolov8/train6/weights/best.pt')
    results = model('../../data/yolov8-b/test/images/20231030_073112_jpg.rf.889b4bf54054a064d71ec4b7894c24aa.jpg')
    print(results)

    for r in results:
        im_array = r.plot()  # plot a BGR numpy array of predictions
        im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
        im.save('results.jpg')  # save image

