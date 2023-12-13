from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image
from ultralytics import YOLO


app = Flask(__name__)
CORS(app, resources={r"/detect": {"origins": "*"}})

# Load the YOLOv8 - make sure to adjust the path accordingly
model = YOLO('../model-training/yolov8/train6/weights/best.pt')


# POST request - detect objects in image
@app.route('/detect', methods=['POST'])
def detect_objects():
    print('request received')
    try:
        # image is in form-data
        image = request.files['image']

        # convert to PIL image
        image = Image.open(image)

        # resize image
        image = image.resize((640, 640))

        # detect objects
        results = model.predict(image, classes=[0, 1])

        for r in results:
            im_array = r.plot()  # plot a BGR numpy array of predictions
            im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
            im.save('results.jpg')  # save image

        return send_file('results.jpg', mimetype='image/jpg')

    except Exception as e:
        return jsonify({'error': str(e)})


# Run the server on local machine
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
    # print the local address to access the server


