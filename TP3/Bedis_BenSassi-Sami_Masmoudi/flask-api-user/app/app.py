
from datetime import datetime as dt
import locale
from flask import Flask, jsonify
from flask_cors import CORS
import string
import logging




app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

logging.basicConfig(filename='./logs/app.log', level=logging.INFO, 
                   format='%(asctime)s %(levelname)s: %(message)s')


@app.route('/date')
def today():
    # Get actual time
    app.logger.info('Main page loaded')
    locale.setlocale(locale.LC_TIME, "fr_FR.UTF-8")
    today = dt.now()

    # Format time as desired
    today_str = today.strftime('%A %d %B %Y')

    # Capitalize day and month tokens
    today_str  = string.capwords(today_str )
    
    return jsonify({'date': today_str})


app.run(host='0.0.0.0', port=5000, debug=True)




