from flask import Flask, request, Response

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    html = """
    <html>
        <body>
            <h1>Welcome</h1>
            <p><a href="/profile?name=guest">View Profile</a></p>

            <form action="/profile" method="get">
                <input name="name" value="guest">
                <input type="submit" value="Load Profile">
            </form>
        </body>
    </html>
    """
    return Response(html, mimetype="text/html")


@app.route("/profile", methods=["GET"])
def profile():
    name = request.args.get("name", "guest")

    html = f"""
    <html>
        <body>
            <h1>User Profile</h1>
            <p>Welcome {name}</p>
        </body>
    </html>
    """
    return Response(html, mimetype="text/html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5150)
