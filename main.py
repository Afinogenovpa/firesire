from flask import Flask, render_template


firesire = Flask(__name__)


@firesire.route('/')
def index():
    return render_template('index.html')

#@firesire.route('/<username>')
#def users():
#    return 'User %s' % username


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    firesire.debug = True
    firesire.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
