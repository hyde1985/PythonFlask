from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


@app.route('/hello')
def hello():
    return 'Hello World'


# app.add_url_rule('/hello', view_func=hello)

if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
