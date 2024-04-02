import requests

def upload_image(filename, server_url):
    with open(filename, 'rb') as f:
        files = {'image': f}
        response = requests.post(server_url, files=files)
        if response.status_code == 200:
            print("Image uploaded successfully")
        else:
            print("Failed to upload image:", response.text)

if __name__ == "__main__":
    filename = './cat.jpg'  # Replace with the path to your image file
    server_url = 'http://localhost:5000/upload'  # Replace with the server URL
    upload_image(filename, server_url)
