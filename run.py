from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run()
