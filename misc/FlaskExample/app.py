from flask import Flask, render_template, request      
import sys
app = Flask(__name__)

@app.route("/")
def home():
	return render_template("index.html")



@app.route('/success', methods = ['POST'])  
def success():   
    if request.method == 'POST':
        li = request.form.getlist('subject')
        return render_template("list.html",li =  li)

if __name__ == "__main__":
	app.run(debug=True)
