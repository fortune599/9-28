from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def temp():
    print"\n\n\n"
    print "this the apperrino"
    print app
    print "this is username"
    print request.args
    return render_template("input.html")

@app.route("/auth")
def author():
    print"\n\n\n"
    print "this the apperrino"
    print app
    print "this is username"
    print request.args['username']
    return "KOAAAAAAAAA"

if __name__ == "__main__":
    app.debug = True
    app.run()
