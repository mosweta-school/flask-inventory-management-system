from flask import Flask

from inventory.routes import inventory_bp
from external.routes import external_bp

app = Flask(__name__)

app.register_blueprint(inventory_bp)
app.register_blueprint(external_bp)


@app.route("/health", methods=["GET"])
def health():
    return {
        "status": "healthy",
        "service": "Inventory Management API",
        "version": "1.0.0"
    }, 200


if __name__ == "__main__":
    app.run(debug=True)