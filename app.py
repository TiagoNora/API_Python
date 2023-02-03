from flask import Flask, jsonify
import requests
import json

app = Flask(__name__)


class Info:
    def __init__(self, icao, callsign, longitude, latitude, squawk):
        self.icao = icao
        self.callsign = callsign
        self.longitude = longitude
        self.latitude = latitude
        self.squawk = squawk


@app.route('/airplane/<icao>', methods=['GET'])
def getInfoFromAPI(icao):
    jsonResponse = makeCallToApi(icao)
    states = jsonResponse['states'][0]
    icao = states[0]
    callsign = states[1]
    longitude = states[5]
    latitude = states[6]
    squawk = states[14]
    infoObject = Info(icao, callsign, longitude, latitude, squawk)
    build = {'icao': icao, 'callsign': callsign, 'longitude': longitude, 'latitude': latitude, 'squawk': squawk}
    return jsonify(build)
    return json.dumps(infoObject.__dict__)


def makeCallToApi(icao):
    link = "https://opensky-network.org/api/states/all?icao24=" + icao;
    response = requests.get(link)
    jsonResponse = response.json()
    return jsonResponse


if __name__ == '__main__':
    app.run()
