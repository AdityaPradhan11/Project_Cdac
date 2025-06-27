from flask import Flask, request
import base64
import json

app = Flask(__name__)

@app.route("/", methods=["POST"])
def validate_image_type():
    envelope = request.get_json()
    if not envelope or 'message' not in envelope:
        return "Invalid Pub/Sub message", 400

    pubsub_message = envelope['message']
    if 'data' in pubsub_message:
        data = base64.b64decode(pubsub_message['data']).decode("utf-8")
        file_data = json.loads(data)
        filename = file_data['name']
        if filename.endswith('.jpg') or filename.endswith('.jpeg') or filename.endswith('.png'):
            print(f"✅ Valid image uploaded: {filename}")
        else:
            print(f"❌ Invalid file type uploaded: {filename}")
    else:
        print("No data in message")

    return "OK", 200
