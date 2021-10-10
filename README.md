# DesmosImageRenderer
Plots Images in Desmos.

![Screenshot 2021-10-10 124547](https://user-images.githubusercontent.com/83541306/136709336-70d703d5-a45d-4767-ac6e-389169cfb6c6.png)
<h1 align="center">Preview Image </h1>


Install requirements
```sh
pip install -r requirements.txt
```
Clone Repository
```sh
git clone https://github.com/cartesiancanvas/DesmosImageRenderer.git
```
Put the Image that you want to plot in the same directory.
Open the backend.py file and provide the image name.
Open the index.js file and change colour and style of lines.
```sh
image_name="imagename.png" #Provide required Image
color: 'Provide the hex code of your desirable colour.' , lineStyle: Desmos.Styles.SOLID/DASHED/DOTTED 
```
Run backend
```sh
python backend.py
```
The output should be like this:
```sh
* Serving Flask app "backend" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```
Open index.html in the browser .In console write:
```sh
init()
```
It might take a while to render images which has a lot of lines.


