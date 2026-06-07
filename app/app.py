from flask import Flask, request, jsonify
import logging
import uuid

app = Flask(__name__)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

orders = []

@app.route("/")
def home():
    logging.info("Home endpoint called")
    return jsonify({"message": "Retail Application Running"})


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/orders", methods=["GET"])
def get_orders():
    logging.info("Fetching orders")
    return jsonify(orders)


@app.route("/orders", methods=["POST"])
def create_order():
    data = request.json

    order = {
        "id": str(uuid.uuid4()),
        "item": data.get("item"),
        "quantity": data.get("quantity")
    }

    orders.append(order)

    logging.info(f"Order created: {order}")

    return jsonify(order), 201


@app.route("/error")
def error():
    try:
        1/0
    except Exception as e:
        logging.error(f"Application Error: {str(e)}")
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)