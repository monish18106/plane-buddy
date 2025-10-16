from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

# Plane detail pages (10 total)
@app.route('/boeing747')
def boeing747():
    return render_template('boeing747.html')

@app.route('/concorde')
def concorde():
    return render_template('concorde.html')

@app.route('/douglasdc3')
def douglasdc3():
    return render_template('douglasdc3.html')

@app.route('/cessna182')
def cessna182():
    return render_template('cessna182.html')

@app.route('/cirrussr22')
def cirrussr22():
    return render_template('cirrussr22.html')

@app.route('/antonov225')
def antonov225():
    return render_template('antonovan225.html')

@app.route('/piperj3')
def piperj3():
    return render_template('piperj3.html')

@app.route('/lockheedc130')
def lockheedc130():
    return render_template('lockheedc130.html')

@app.route('/f4phantom')
def f4phantom():
    return render_template('mcdonneef4.html')

@app.route('/x15')
def x15():
    return render_template('x15.html')

@app.route('/tracking')
def track():
    return render_template('tracking.html')

@app.route('/api/flights')
def flights():
    try:
        # OpenSky anonymous public API (works without credentials)
        url = "https://opensky-network.org/api/states/all?lamin=-60&lomin=-180&lamax=85&lomax=180"
        resp = requests.get(url, timeout=10)
        data = resp.json()
        flights = []

        if data.get("states"):
            for st in data["states"]:
                if st[5] and st[6]:
                    flights.append({
                        "icao24": st[0],
                        "callsign": st[1] or "Unknown",
                        "origin_country": st[2],
                        "longitude": st[5],
                        "latitude": st[6],
                        "altitude": st[7],
                        "velocity": st[9],
                        "heading": st[10],
                        "on_ground": st[8]
                    })

        print(f"Fetched {len(flights)} flights")
        return jsonify({"flights": flights})

    except Exception as e:
        print("Error:", e)
        return jsonify({"flights": []})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
