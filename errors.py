from jsonschema import ValidationError

def handle_bad_request(e):
    if isinstance(e.description, ValidationError):
        original_error = e.description
        return {"error": original_error.message}, 400
    