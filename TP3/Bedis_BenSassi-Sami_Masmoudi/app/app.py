
from datetime import datetime as dt
from flask import Flask, jsonify
from flask_cors import CORS
import string




app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/date')
def today():
    # Get actual time
    today = dt.now()

    # Format time as desired
    today_str = today.strftime('%A %d %B %Y')

    # Capitalize day and month tokens
    today_str  = string.capwords(today_str )
    
    return jsonify({'date': today_str})


app.run(host='0.0.0.0', port=5000, debug=True)




