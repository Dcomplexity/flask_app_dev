from flask import Flask
from flask import render_template
from re import escape
app = Flask(__name__)

@app.route('/')
def index():
    return "Index Page. Test the docker"

@app.route('/hello')
def hello():
    return "Hello Deng Chuang. You need to work hard now. What to do is to justify your time."

@app.route('/hello/')
@app.route('/hello/<name>')
def hello_name(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % escape(username)

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % escape(subpath)

@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
