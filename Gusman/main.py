from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route("/gusman")
def gusman():
	return render_template("gusman.html", current_time=str(time.time()))

@app.route("/gusmanapp")
def gusmanapp():
	return render_template("gusmanapp.html", current_time=str(time.time()))

if __name__ == "__main__":
	app.run(debug=True)