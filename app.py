from flask import Flask, request, jsonify
import boto3
from botocore.exceptions import ClientError
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
# Create Bedrock client
client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
    aws_access_key_id="",
    aws_secret_access_key=""
)

# default model id (can be overridden per-request by sending {"model": "..."})
default_model_id = "amazon.nova-lite-v1:0"

@app.route("/chat", methods=["POST"])
def chat():
    try:
        data = request.get_json() or {}

        # required: message text
        user_message = data.get("message")
        if not user_message:
            return jsonify({"error": "'message' field is required"}), 400

        # optional: model override (string) — fall back to default_model_id
        model_id = data.get("model", default_model_id)

        # optional: role for the message (user/system/assistant)
        role = data.get("role", "user")
        allowed_roles = {"user", "assistant", "system"}
        if role not in allowed_roles:
            return jsonify({"error": f"invalid role '{role}'. allowed: {sorted(list(allowed_roles))}"}), 400

        conversation = [
            {
                "role": role,
                "content": [{"text": user_message}],
            }
        ]

        response = client.converse(
            modelId=model_id,
            messages=conversation,
            inferenceConfig={
                "maxTokens": 100,
                "temperature": 0.5,
                "topP": 0.9
            }
        )

        response_text = response["output"]["message"]["content"][0]["text"]

        return jsonify({
            "status": "success",
            "reply": response_text
        })

    except ClientError as e:
        return jsonify({"error": str(e)}), 500

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=False, port=5000)