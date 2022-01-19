from flask.helpers import send_file
from application.main import app

# @app.route('/yeet')
# def yeet():
#     return send_file('/app/flag')

app.run(host='0.0.0.0', port=1337, debug=True, use_evalex=False)