from flask import Flask
from flask_restful import Api
from errors import handle_bad_request
from workflow.workflow import ApiEdad


app = Flask(__name__)
api = Api(app)
app.register_error_handler(400, handle_bad_request)


api.add_resource(ApiEdad, "/api/edad")


if __name__ == "__main__":
    app.run(debug=True, port=5000, host="0.0.0.0")
