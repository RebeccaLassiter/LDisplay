from flask import Flask
app = Flask(__name__)


@app.route('/')
def getTrainData():
   apiKey="1ab5504549144498bb4fc7badfe76125"
   return "test4"

if __name__ == '__main__':
   app.run(debug = True)