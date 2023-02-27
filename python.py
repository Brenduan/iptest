from flask import Flask, request, render_template
import requests
from requests.auth import HTTPBasicAuth

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ip_address = request.remote_addr
        fraudguard_url = 'https://api.fraudguard.io/v2/ip/' + ip_address
        response = requests.get(fraudguard_url, verify=True, auth=HTTPBasicAuth('JJO8GulD3bAdnkEC', '7C05VpP8zssGpNWd'))
        return render_template('result.html', ip=ip_address, result=response.text)
    else:
        return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)
