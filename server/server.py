from flask import Flask, request

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return 'No image uploaded', 400
    
    image = request.files['image']
    image.save('uploaded_image.jpg')  # Save the image to disk
    
    return 'Image uploaded successfully', 200

if __name__ == '__main__':
    app.run(debug=True)
