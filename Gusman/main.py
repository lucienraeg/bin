from flask import Flask, render_template, request
import time
import sys

app = Flask(__name__)

reports = []

@app.route("/", methods=["GET", "POST"])
def index():
	if request.method == "GET":
		return render_template("index.html", current_time=str(time.time()))
	elif request.method == "POST":
		if report_name in request.form:
			report_id = len(reports)
			report_name = request.form["report_name"]
		else:
			raise "oh no"

@app.route("/output", methods=["GET"])
def output():
	return render_template("output.html", current_time=str(time.time()), reports=reports)

@app.route("/gusman")
def gusman():
	return render_template("gusman.html", current_time=str(time.time()))

if __name__ == "__main__":
	app.run(debug=True)
	print(reports)