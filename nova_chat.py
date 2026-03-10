import boto3
from botocore.exceptions import ClientError

# Step 1: Create Bedrock Runtime client
client = boto3.client(
    service_name="bedrock-runtime",
    region_name="us-east-1",
    aws_access_key_id="",
    aws_secret_access_key=""
)

# Step 2: Select model
model_id = "amazon.nova-lite-v1:0"

# Step 3: Your message
user_message = "Describe the purpose of a 'hello world'."

# Step 4: Conversation format
conversation = [
    {
        "role": "user",
        "content": [
            {"text": user_message}
        ],
    }
]

try:
    # Step 5: Call the model
    response = client.converse(
        modelId=model_id,
        messages=conversation,
        inferenceConfig={
            "maxTokens": 100,
            "temperature": 0.5,
            "topP": 0.9
        }
    )

    # Step 6: Print response
    response_text = response["output"]["message"]["content"][0]["text"]
    print("\nModel Response:")
    print(response_text)

except ClientError as e:
    print("AWS Client Error:", e)

except Exception as e:
    print("General Error:", e)