from flask import Flask
from flask_restful import Resource, Api, reqparse
from classes.doc_classifier import classify


path_to_model = 'models/doc_classifier.pkl' # machine learning model


app = Flask(__name__)
api = Api(app)


class document_classification(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('text', type=str, required=True, help='Provide document summary')
        args = parser.parse_args(strict=True)
        return classify(args['text'], path_to_model)


api.add_resource(document_classification, '/document-classification')


if __name__ == '__main__':
    app.run(debug=True)