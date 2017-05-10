from flask import Flask
from flask import render_template
from prometheus_metrics import setup_metrics
app = Flask(__name__)
setup_metrics(app)

@app.route("/")
def Main_Page():
    return render_template('Main_Page.html')
	
@app.route("/Sub_Page1")
def Sub_Page1():
    return render_template('Sub_Page1.html')
	
@app.route("/Sub_Page2")
def Sub_Page2():
    return render_template('Sub_Page2.html')
	
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
