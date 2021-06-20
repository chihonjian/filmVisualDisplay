from flask import Flask,render_template




def main():
    app = Flask(__name__)


    @app.route('/')
    def hello_world():
        return render_template("index.html")

    app.run()

if __name__ == '__main__':
    main()
