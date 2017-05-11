import glob
import shlex
import subprocess
import sys
import uuid

from flask import Flask, request, send_file


app = Flask(__name__)

@app.route('/')
def index():
    url = request.args.get('url', '')

    if not url.strip():
        return '''
        <form action="/" method="get">
          URL: <input type="text" name="url">
          <input type="submit" value="Download PDF">
        </form>
        '''

    else:
        filename = '/tmp/{}.pdf'.format(uuid.uuid4())
        command = '/app/bin/wkhtmltopdf "{}" "{}"'.format(url, filename)
        process = subprocess.Popen(shlex.split(command),
                                   stdout=subprocess.DEVNULL,
                                   stderr=subprocess.DEVNULL)
        process.wait()
        return send_file(filename,
                         as_attachment=True,
                         mimetype='application/pdf')
