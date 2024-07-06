import os

from flask import (Flask, redirect, render_template, request,
                   send_from_directory, url_for, request, jsonify)
import Caribe as cb

app = Flask(__name__)


@app.route('/')
def index():
   print('Request for index page received')
   return render_template('index.html')

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.route('/hello', methods=['POST'])
def hello():
   name = request.form.get('name')

   if name:
       corrected_text = output=cb.caribe_corrector(name)
       print('Request for hello page received with name=%s' % corrected_text)
       #return render_template('hello.html', name = corrected_text)
   else:
       print('Request for hello page received with no name or blank name -- redirecting')
       #return render_template('hello.html')

# Define route for correcting text
@app.route('/correct', methods=['POST'])
def correct_text():
    data = request.json
    text = data.get('text', '')

    # Correct text using Caribe
    corrected_text = cb.caribe_corrector()
    # Return corrected text as JSON response
    return jsonify({'corrected_text': [corrected_text]})
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5001, debug=True)
