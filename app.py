from flask import Flask
import psycopg2

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World from Hitomi Imai in 3308'

@app.route('/db_test')
def testing():
    conn = psycopg2.connect("postgresql://lab10_render_example_user:G5dC179D1ioxdA6j1h6OFxFjr3FQMyXO@dpg-cqj0td8gph6c738vfho0-a/lab10_render_example")
    conn.close()
    return "Database Connection Successful"
