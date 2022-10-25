from flask import Flask, render_template
import os


app = Flask(__name__, static_url_path='/static')
app.config['DEBUG'] = True


@app.route('/')
def index():
    images = list()
    for x in os.listdir('static/images'):
        if x.endswith(".jpg"):
            images.append(x)
    return render_template('index.html', images = images)


if __name__ == '__main__':
    app.run()
