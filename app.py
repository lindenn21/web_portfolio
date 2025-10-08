from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/works', methods=['GET', 'POST'])
def works():
    uppercase_result = None
    circle_result = None
    triangle_result = None
    rectangle_result = None

    if request.method == 'POST':
        form_type = request.form.get("form_type")
        if form_type == "uppercase":
            text = request.form.get("inputString")
            if text:
                uppercase_result = text.upper()

        elif form_type == "circle":
            radius = request.form.get("radius")
            try: 
                r = float(radius)
                circle_result = 3.14 * r ** 2
            except ValueError:
                circle_result = "Invalid Input"   
        
        elif form_type == "triangle":
           
            base = request.form.get("base")
            height = request.form.get("height")
                
        
            try:
                 b = float(base)
                 h = float(height)
                 triangle_result = 0.5 * b * h
            except ValueError:
                triangle_result = "Invalid Input"
        
        elif form_type == "rectangle":
            width = request.form.get("width")
            length = request.form.get("length")

            try:
                w = float(width)
                l = float(length)
                rectangle_result = w * l
            except ValueError:
                rectangle_result = "Invalid Input"
    return render_template('works.html', uppercase_result=uppercase_result, circle_result=circle_result, triangle_result=triangle_result, rectangle_result=rectangle_result)


@app.route('/contacts')
def contacts():
    return render_template('contacts.html')

if __name__ == "__main__":
    app.run(debug=True)
