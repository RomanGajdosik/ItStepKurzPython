from flask import Flask, request, jsonify

app = Flask(__name__)

# Zoznam dostupných zájazdov
trips = [
    {"id": 1, "destination": "Pariz", "price": 350},
    {"id": 2, "destination": "Rim", "price": 400},
    {"id": 3, "destination": "Lisabon", "price": 450}
]


@app.route('/trips', methods=['GET'])
def get_trips():
    return jsonify(trips)


@app.route('/trips/search', methods=['GET'])
def search_trips():
    destination = request.args.get('destination', '').lower()
    filtered_trips = [trip for trip in trips if destination in trip["destination"].lower()]
    return jsonify(filtered_trips)


@app.route('/book', methods=['POST'])
def book_trip():
    data = request.json
    trip_id = data.get("trip_id")
    name = data.get("name")
    people = data.get("people")

    trip = next((trip for trip in trips if trip["id"] == trip_id), None)

    if not trip:
        return jsonify({"error": "Zajazd s danzm ID neexistuje."}), 400

    total_price = trip["price"] * people
    message = f"Zajazd do {trip['destination']} pre {people} osoby uspesne rezervovany pre {name}. Cena spolu: {total_price} €."

    return jsonify({"message": message})


if __name__ == '__main__':
    app.run(debug=True)