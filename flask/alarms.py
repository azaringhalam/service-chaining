#!/usr/bin/python
from flask import Flask, jsonify
from flask import abort
from flask import make_response
from flask import request
from flask import url_for
#from flask.ext.httpauth import HTTPBasicAuth
import os

app = Flask(__name__)

@app.route('/alarms/api', methods=['POST'])
def create_alarm():
    if not request.json:
        abort(400)
    if( (request.json['current'] == 'alarm') and  (request.json['previous'] == 'ok') ):
        os.system('/root/trial/update_chain_3')
        print request.json['current'], request.json['previous'], request.json['alarm_id'], 'alarm raised: scale-out 2->3 instances'
        return jsonify({'task': u'Ceilometer alarm raised - scale-out 2 -> 3 instances'}), 201
    elif( (request.json['current'] == 'ok') and  (request.json['previous'] == 'alarm') ):
        os.system('/root/trial/update_chain_2')
        print request.json['current'], request.json['previous'], request.json['alarm_id'], 'alarm cleared: scale-in 3->2 instances'
        return jsonify({'task': u'Ceilometer alarm cleared - scale-in 3 -> 2 instances'}), 201
    else:
        print 'Unknown state transition'
    return jsonify({'task': u'Ceilometer alarm generated'}), 201

if __name__ == '__main__':
    app.run(host="10.10.13.102", port=8197, debug=True)

