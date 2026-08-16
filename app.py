from flask import Flask
app = Flask(__name__)
@app.route("/")
def home():
  return ""
  <html>
	<head>
  <title>My docker demo website</title>
  </head>
  <body>
  <h1>My demo website</h1>
  <p>Hello! this website is runnig inside a docker container on azure</p>
  </body>
  </html>
  if __name__ "__main__":
    app.run(host = "0.0.0.0", port = 8000)
