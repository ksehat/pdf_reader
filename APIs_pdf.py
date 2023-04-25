from flask import Flask, request, jsonify, Response
import json
from waitress import serve

app = Flask(__name__)


@app.route('/', methods=['POST'])
def home():
    if (request.method == 'POST'):
        data = json.loads(request.data)
        if data['pdf_name'] == 'AIR SAFETY REPORT':

            return pdf_dict









        try:
            return jsonify({'data': (result.to_json(orient='records', force_ascii=False))}).json
        except:
            return Response(
                "Error in scraper",
                status=400,
            )


# host_IP = f'{input("Please inset IP:")}'
# host_port = f'{input("Please inset port:")}'
if __name__ == '__main__':
    serve(app, host='192.168.40.155', port='3000')
