from flask import Flask
import os 

app = Flask(__name__)

@app.route('/staging')
def home():
    my_custom_var = os.environ.get('SECRET_KEY')
    return 'This is a Staging Server, Server Details: '  + my_custom_var

if __name__ == '__main__':
    app.run()
    # app.run(debug=True, port=8081)
