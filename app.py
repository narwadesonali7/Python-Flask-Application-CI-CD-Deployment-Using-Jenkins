from flask import Flask
import os
app = Flask(__name__)

@app.route('/')
def hello_geek():
    return 'This is sonali successfully deployed python application through jenkins!!!!!!!!!, added webhook From jenkins server from sonali'
@app.route('/hi')
def hell():
    return '<h1>Hellooooooooo from Flask & Docker</h1>'

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
