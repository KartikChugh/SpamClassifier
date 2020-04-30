from flask_frozen import Freezer
from server import app

freezer = Freezer(app)

# @freezer.register_generator
# def predict():
#     yield '/predict/index.html'

if __name__ == '__main__':
    freezer.freeze()