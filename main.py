from flask import Flask

firesire = Flask(__name__)

@firesire.route('/')
def index():
    return 'index page'




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    firesire.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
