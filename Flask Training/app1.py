import math
from flask import Flask, redirect, render_template, request, url_for

app1 = Flask(__name__)


@app1.route("/calC", methods=["POST", "GET"])
def calC():
    if request.method == "GET":
        return render_template("calC.html", r=None)
    else:
        try:
            a = float(request.form["a"])
            b_raw = request.form.get("b")
            b = float(b_raw) if (b_raw and b_raw.strip() != "") else 0.0

            opt = request.form.get("operation")
            if opt == "add":
                r = a + b
            elif opt == "sub":
                r = a - b
            elif opt == "mul":
                r = a * b
            elif opt == "div":
                r = "Error: Division by Zero" if b == 0 else a / b

            elif opt == "pow":
                r = math.pow(a, b)
            elif opt == "sqrt":
                r = "Error: Negative Root" if a < 0 else math.sqrt(a)
            elif opt == "sin":
                r = math.sin(math.radians(a))  # Calculates using degrees
            elif opt == "cos":
                r = math.cos(math.radians(a))  # Calculates using degrees
            else:
                r = "Unknown Operation"

        except (ValueError, TypeError, OverflowError):
            r = "Error: Invalid Input"

        return render_template("calC.html", r=r)


if __name__ == "__main__":
    app1.run(debug=True)
