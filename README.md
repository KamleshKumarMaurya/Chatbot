# 🤖 AI Chatbot using Amazon Nova

This project is an **AI-powered chatbot application** built using **Amazon Nova (via Amazon Bedrock), Python, and Angular**.

The chatbot processes user queries and generates intelligent responses using **Amazon Nova language models**.
The backend communicates with Amazon Bedrock APIs, while the Angular frontend provides a user-friendly chat interface.

---

# 🚀 Features

* AI-powered chatbot
* Natural language understanding
* Integration with Amazon Nova models
* REST API based architecture
* Interactive Angular chat UI
* Real-time conversation support
* Scalable architecture

---

# 🛠 Tech Stack

| Technology      | Purpose              |
| --------------- | -------------------- |
| Python          | Backend API          |
| Amazon Bedrock  | AI model access      |
| Amazon Nova     | Large Language Model |
| Angular         | Frontend UI          |
| REST API        | Communication layer  |
| AWS SDK (Boto3) | Bedrock integration  |

---

# 🧠 AI Model

This chatbot uses **Amazon Nova** through **Amazon Bedrock**.

The model processes natural language input and generates contextual responses.

Example model used:

```text id="x7tezz"
amazon.nova-lite-v1:0
```

---

# 📂 Project Structure

```text id="4mq2jl"
Chatbot
│
├── backend-python
│   ├── app.py
│   ├── requirements.txt
│
├── frontend-angular
│   ├── src
│   ├── package.json
│
└── README.md
```

---

# ⚙️ Backend Setup (Python)

### 1️⃣ Clone the repository

```bash id="xngdws"
git clone https://github.com/KamleshKumarMaurya/Chatbot.git
```

---

### 2️⃣ Install dependencies

```bash id="y9yzy7"
pip install -r requirements.txt
```

---

### 3️⃣ Configure AWS Credentials

Configure credentials for **Amazon Bedrock access**.

Example:

```bash id="0eh2a6"
aws configure
```

Enter:

* AWS Access Key
* AWS Secret Key
* Region (example: us-east-1)

---

### 4️⃣ Run backend server

```bash id="tnq5sz"
python app.py
```

Server runs at:

```text id="te6p0d"
http://localhost:5000
```

---

# ⚙️ Frontend Setup (Angular)

Navigate to frontend directory

```bash id="1hknb2"
cd frontend-angular
```

Install dependencies

```bash id="g83p8u"
npm install
```

Run Angular app

```bash id="ykrhpk"
ng serve
```

Frontend runs at

```text id="ygz1ec"
http://localhost:4200
```

---

# 🔄 Chatbot Workflow

1️⃣ User enters a message in the Angular UI

2️⃣ Angular sends request to Python backend

3️⃣ Backend calls Amazon Bedrock API

4️⃣ Amazon Nova model generates response

5️⃣ Response is returned to frontend

6️⃣ Chat response is displayed to the user

---

# 📡 Example API

### Chat Request

```text id="p8m8gr"
POST /chat
```

Request body

```json id="vgysck"
{
 "message": "Hello"
}
```

Response

```json id="kdxp36"
{
 "reply": "Hello! How can I help you today?"
}
```

---

# 🔒 Security Best Practices

* Never commit AWS credentials to GitHub
* Use environment variables
* Use `.env` files for secrets
* Enable IAM role permissions

---

# 📈 Future Improvements

* Conversation history
* Multi-user chat support
* Voice-based chatbot
* Streaming AI responses
* Deployment on AWS

---

# 👨‍💻 Author

Kamlesh Kumar Maurya

Software Developer

Skills:

* Java
* Spring Boot
* Angular
* Ionic
* Python
* PostgreSQL
