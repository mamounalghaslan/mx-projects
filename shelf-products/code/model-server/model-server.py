from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from PIL import Image
from ultralytics import YOLO


app = Flask(__name__)
CORS(app)

# Load your YOLOv8
model = YOLO('../yolov8/train6/weights/best.pt')


@app.route('/detect', methods=['POST'])
def detect_objects():
    try:
        # image is in form-data
        image = request.files['image']

        # convert to PIL image
        image = Image.open(image)

        results = model(image)

        for r in results:
            im_array = r.plot()  # plot a BGR numpy array of predictions
            im = Image.fromarray(im_array[..., ::-1])  # RGB PIL image
            im.save('results.jpg')  # save image

        response = jsonify({'result': 'success'})
        response.headers.add('Access-Control-Allow-Origin', '*')

        # return the image using send_file and allow CORS
        return send_file('results.jpg', mimetype='image/jpg')

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(debug=True)
    # print the local address to access the server


