from flask import Flask, request, jsonify
import io, sys
import numpy as np
import cv2
from PIL import Image
import torch
import base64
import RRDBNet_arch as arch


# Config
app = Flask(__name__)
device = torch.device('cpu')
model_path = 'RRDB_ESRGAN_x4.pth'

# Load the model
model = arch.RRDBNet(3, 3, 64, 23, gc=32)
model.load_state_dict(torch.load(model_path), strict=True)
model.eval()
model = model.to(device)

# Super resolution function
def super_res(img):
    # print(img_processed)
    img = img * 1.0 / 255
    img_processed = torch.from_numpy(np.transpose(img[:, :, [2, 1, 0]], (2, 0, 1))).float()
    print("Done preprocessing")
    img_LR = img_processed.unsqueeze(0)
    print("Mounting image to device")
    img_LR = img_LR.to(device)

    print("Starting pytorch compute")
    with torch.no_grad():
        # This is what takes forever
        output = model(img_LR).data.squeeze().float().cpu().clamp_(0, 1).numpy()
        print("step 1 done")
    output = np.transpose(output[[2, 1, 0], :, :], (1, 2, 0))
    print("step 2 done")
    output = (output * 255.0).round()
    print("step 3 done")
    return output

# Remove background for images with alpha channels
def remove_background(img):
    print("Hit this function")
    img = img.convert('RGBA')
    datas = img.getdata()
    newData = []
    for item in datas:
        if item[0] == 0 or item[1] == 0 or item[2] == 0:
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)
    img.putdata(newData)
    return img

# Test route
@app.route('/test' , methods=['GET','POST'])
def test():
	print("log: got at test" , file=sys.stderr)
	return jsonify({'status':'succces'})

# Image processing route
@app.route('/image', methods=['POST'])
def process_image():
    # Get the image file
    file = request.files['image'].read()
    # print(file)
    alpha = False

    npimg = np.fromstring(file, np.uint8)
    img = cv2.imdecode(npimg ,cv2.IMREAD_UNCHANGED)
    if img.shape[2] == 4:
        alpha = True
        img = cv2.cvtColor(img, cv2.COLOR_RGBA2RGB)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    print("Complete conversions, starting super resolution")
    result = super_res(img)
    
    result = Image.fromarray(result.astype("uint8"))
    print(result)
    if alpha:
        result = remove_background(result)
    rawBytes = io.BytesIO()
    result.save(rawBytes, "PNG")
    rawBytes.seek(0)
    img_base64 = base64.b64encode(rawBytes.read())
    return jsonify({'status':str(img_base64)})

# Authorize CORS
@app.after_request
def after_request(response):
    print("log: setting cors" , file = sys.stderr)
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

if __name__ == "__main__":
    app.run()