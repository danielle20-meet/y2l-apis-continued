from flask import Flask, render_template, request,json
import requests
app = Flask(__name__)
headers = {'Authorization': 'Key 97c16fcd44fa4cb38d8c65279ddca434'}
api_url = "https://api.clarifai.com/v2/models/aaa03c23b3724a16a56b629203edc62c/outputs"
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/study_image', methods = ['POST'])
def study_image():
    image_url = request.form['url-input']
    # At this point you have the image_url value from the front end
    # Your job now is to send this information to the Clarifai API
    # and read the result
    data ={"inputs": [
      {
        "data": {
          "image": {
            "url":image_url
          }
        }
      }
    ]}
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    string=response.content
    string=str(string, "utf-8")
    l=string.split("id")
    l1=l[1:]

    return render_template('home.html', results=l1)

if __name__ == '__main__':
    app.run(debug=True)