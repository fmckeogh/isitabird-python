
from flask import Flask, Response
import time

app = Flask(__name__)


@app.route('/')
def index():
    def generate():
        yield 'waiting 5 seconds\n'

        for i in range(1, 101):
            time.sleep(0.05)

            if i % 10 == 0:
                yield '{}%\n'.format(i)

        yield 'done\n'
    return Response(generate(), mimetype='text/plain')

app.run()
