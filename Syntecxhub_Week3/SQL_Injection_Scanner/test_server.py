from flask import Flask, request
app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        user = request.form.get("username", "")
        triggers = ["'", '"', "--", "union", "select"]
        if any(t.lower() in user.lower() for t in triggers):
            return """
            <h2>Database Error</h2>
            <p>Warning: You have an error in your SQL syntax;
            check the manual that corresponds to your MySQL server version.</p>
            """, 500
        return f"<h2>Welcome, {user}!</h2>"
    return """
    <html>
      <body>
        <h2>Login Form</h2>
        <form method="POST">
            <input type="text" name="username" placeholder="Username">
            <input type="submit" value="Login">
        </form>
      </body>
    </html>
    """
if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)