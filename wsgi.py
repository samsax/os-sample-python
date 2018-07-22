from flask import Flask, url_for
application = Flask(__name__)

@application.route("/")
def hello():
    return "First Attemp!"

@application.route('/articles')
def api_articles():
    return 'List of ' + url_for('api_articles')

@application.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

if __name__ == "__main__":
    application.run()
