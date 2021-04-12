from flask import Flask, render_template
import unittest
import helloworld


class TestMethods(unittest.TestCase):
    def test_add(self):
        self.assertEqual(helloworld.testing('a'), 'a')


app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
    unittest.main()
