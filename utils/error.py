from flask import jsonify


def not_found():
    error = {
        'errors': {
            'userMessage': 'Sorry, the requested resource does not exist',
            'internalMessage': 'Not found in the database',
            'code': 1,
        }
    }
    return jsonify(error)
