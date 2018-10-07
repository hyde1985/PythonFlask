from flask import Flask

app = Flask(__name__)
app.config.from_object('config')


@app.route('/book/search/<q>/<page>')
def search(q, page):
    # isbn13 13个0-9的数字组成
    # isbn10 10个0-9数字组成，含有-
    isbn_or_key = 'key'
    if len(q) == 13 and q.isdigit():
        isbn_or_key = 'isbn'
    short_q = q.replace('-', '')
    if "-" in q and len(short_q) == 10 and short_q.isdigit():
        isbn_or_key = 'isbn'


if __name__ == '__main__':
    app.run(debug=app.config['DEBUG'])
