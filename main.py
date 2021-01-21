from flask import Flask, request, jsonify, render_template
from urllib.parse import unquote_plus
import sqlite3

from gen_data import main

main()


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/data')
def get_data():
    item_name = request.args.get('itemname')

    if item_name == "":
        return jsonify([])
    try:
        with sqlite3.connect('important.db') as conn:
            c = conn.cursor()
            c.execute(
                f'SELECT * FROM ITEMS WHERE apparel LIKE "%{item_name}%" OR material LIKE "%{item_name}%"')
            data = [i[1:] for i in c.fetchall()]

    except Exception:
        return jsonify([])

    return jsonify(data)


if __name__ == "__main__":
    app.run()
