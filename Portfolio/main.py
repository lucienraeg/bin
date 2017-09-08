from flask import Flask, render_template
import time

app = Flask(__name__)

@app.route("/")
def main():
	return render_template("index.html", current_time=str(time.time()))

if __name__ == "__main__":
	app.run(debug=True)