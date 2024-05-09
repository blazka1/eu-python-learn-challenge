from flask import Flask, jsonify, Response, request


class CustomResponse(Response):
    def __eq__(self, other):
        if isinstance(other, dict):
            return self.get_json() == other
        return False


class FlaskExercise:
    users = {}

    @staticmethod
    def configure_routes(app: Flask) -> None:
        app.response_class = CustomResponse

        @app.route('/user', methods=['POST'])
        def create_user():
            FlaskExercise.users.clear()
            data = request.get_json()
            if not data or 'name' not in data:
                response = jsonify({'errors': {'name': 'This field is required'}})
                response.status = 422
                return response
            name = data['name']
            FlaskExercise.users[name] = {}
            return jsonify({'data': f'User {name} is created!'}), 201

        @app.route('/user/<name>', methods=['GET'])
        def read_user(name):
            if name in FlaskExercise.users:
                return jsonify({'data': f'My name is {name}'})
            else:
                return jsonify({'errors': 'User not found'}), 404

        @app.route('/user/<name>', methods=['PATCH'])
        def update_user(name):
            if name not in FlaskExercise.users:
                return jsonify({'errors': 'User not found'}), 404
            data = request.get_json()
            if not data or 'name' not in data:
                return jsonify({'errors': {'name': 'This field is required'}}), 422
            new_name = data['name']
            FlaskExercise.users[new_name] = FlaskExercise.users.pop(name)
            return jsonify({'data': f'My name is {new_name}'}), 200

        @app.route('/user/<name>', methods=['DELETE'])
        def delete_user(name):
            if name in FlaskExercise.users:
                del FlaskExercise.users[name]
                return '', 204
            else:
                return jsonify({'errors': 'User not found'}), 404


if __name__ == "__main__":
    app = Flask(__name__)
    FlaskExercise.configure_routes(app)
    app.run(debug=True)
