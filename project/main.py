from flask import Flask

main = Flask(__name__)

from routes.home import *
from routes.lobby import *
from routes.personagens import *

if __name__ == '__main__':
    main.run(debug=True)