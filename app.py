# from flask import Flask, request, redirect, url_for
# import requests

# app = Flask(__name__)

# @app.route('/your_form_url', methods=['GET', 'POST'])
# def submit():
#     if request.method == 'POST':
#         data = {
#             'field1': request.form['field1'],
#             'field2': request.form['field2'],
#             # add more fields if needed
#         }

#         # Make a POST request to your API
#         response = requests.post('your_api_url', json=data)

#         # If the request is successful, redirect the user to another page
#         if response.status_code == 200:
#             return redirect(url_for('success'))
#         else:
#             return 'There was a problem with your submission. Please try again.'

#     return 'Your Form HTML'

# @app.route('/success')
# def success():
#     return 'Your data was submitted successfully!'

# if __name__ == '__main__':
#     app.run(debug=True)

import http.server
import socketserver
import requests

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/submit':
            print("Success!")
            return
        self.send_response(404)
        self.end_headers()

with socketserver.TCPServer(("", 8000), MyHandler) as httpd:
    print("serving at port", 8000)
    httpd.serve_forever()