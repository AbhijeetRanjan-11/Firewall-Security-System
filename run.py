from flask import Flask, request, render_template
from app.firewall import scan_ip
from app.xml_handler import to_xml

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    ip = request.form['ip']
    result = scan_ip(ip)
    result_xml = to_xml(result)
    return result_xml, 200, {'Content-Type': 'application/xml'}

if __name__ == '__main__':
    app.run(debug=True)
