from flask import Flask, render_template, request, redirect
from model.model import load_model, predict_skin_disease

app = Flask(__name__)


model = load_model()  # Implement this function in your model.py file

@app.route('/')
def index():
    return render_template('home.html')
"""
@app.route('/upload', methods=['POST'])
def upload():
    if request.method == 'POST':
        # Get the uploaded image file
        uploaded_file = request.files['file']

        if uploaded_file.filename != '':
            # Perform prediction on the uploaded image using your model
            prediction = predict_skin_disease(uploaded_file, model)  # Implement this function in your model.py file

            # Render the prediction result in the HTML template
            return render_template('index.html', prediction=prediction)

    return render_template('index.html', prediction="Error processing image")
"""
@app.route("/about")
def upload():
    return render_template("about-us.html")

@app.route("/login")
def login():
    return render_template("login.html")

'''@app.route("/upload")
def upload():
    return render_template("Upload.html")'''

@app.route("/service")
def service():
    return render_template("service.html")

@app.route("/appointment")
def appointment():
    return render_template("appointment.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/maps", methods=["GET"])
def maps():
    return redirect("https://www.google.com/maps/d/edit?mid=1YW6OIJ8KGnGC1GS9raPg-ZchGQGqAIs&ll=7.691795640657155%2C80.63993923368832&z=9", code=302)

if __name__ == '__main__':
    app.run(debug=True)
