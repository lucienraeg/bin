from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def main():
	return "Hey man."

if __name__ == "__main__":
	app.run()