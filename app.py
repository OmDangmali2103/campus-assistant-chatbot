from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    message = request.form["message"].lower()

    if "admission" in message:
        return "Admissions are open for BCA, BBA and BSc."

    elif "course" in message:
        return "We offer BCA, BBA and BSc Computer Science."

    elif "library" in message:
        return "Library timings are 8 AM to 8 PM."

    elif "fees" in message or "fee" in message:
        return "BCA Fees: ₹60,000/year"

    elif "contact" in message:
        return "Phone: 02012345678"

    else:
        return "Sorry! I didn't understand. Please ask about Admission, Courses, Library, Fees or Contact."


if __name__ == "__main__":
    app.run(debug=True)