import cv2
import numpy as np
import json
from flask import Flask
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

#https://stackoverflow.com/users/12094894/simon-crane
#https://stackoverflow.com/users/4323741/burhan-rashid

#credits to above for this numpy encoder
class NumpyEncoder(json.JSONEncoder):
    """ Special json encoder for numpy types """
    def default(self, obj):
        if isinstance(obj, (np.int_, np.intc, np.intp, np.int8,
                            np.int16, np.int32, np.int64, np.uint8,
                            np.uint16, np.uint32, np.uint64)):
            return int(obj)
        elif isinstance(obj, (np.float_, np.float16, np.float32,
                              np.float64)):
            return float(obj)
        elif isinstance(obj, (np.ndarray,)):
            return obj.tolist()
        return json.JSONEncoder.default(self, obj)


def auto_canny(image, sigma=0.33):
	v = np.median(image)
	# apply automatic Canny edge detection using the computed median
	lower = int(max(0, (1.0 - sigma) * v))
	upper = int(min(255, (1.0 + sigma) * v))
	edged = cv2.Canny(image, lower, upper)
	# return the edged image
	return edged


image_name="girl.jfif" #Provide required Image
img = cv2.imread(image_name)
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (3,3), 0) 
edge = auto_canny(img_blur)



contours, hierarchy = cv2.findContours(edge, 
    cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  #pass CHAIN_APPROX_NONE to store all the boundary points. 


@app.route("/")
def index():
    return json.dumps(contours,cls=NumpyEncoder)  


app.run()    
  