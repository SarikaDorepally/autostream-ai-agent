# 🚀 AutoStream AI Agent – Social-to-Lead Workflow

## 📌 Overview

This project implements a **Conversational AI Agent** that transforms user conversations into qualified business leads.

Built as part of the **ServiceHive (Inflx) assignment**, the agent goes beyond a simple chatbot by:

* Understanding user intent
* Retrieving accurate product information (RAG)
* Identifying high-intent users
* Triggering backend lead capture actions

---

## 🎯 Key Features

### 🧠 Intent Detection

Classifies user input into:

* Greeting
* Product Inquiry (pricing, features)
* High-Intent Lead (ready to sign up)

---

### 📚 RAG (Retrieval-Augmented Generation)

* Uses a **local knowledge base (JSON)**
* Retrieves accurate responses for:

  * Pricing plans
  * Features
  * Policies

---

### ⚙️ Lead Capture Workflow

When high intent is detected:

1. Collects:

   * Name
   * Email
   * Platform (YouTube, Instagram, etc.)
2. Triggers tool:

```python
mock_lead_capture(name, email, platform)
```

---

### 🔄 State Management

* Maintains conversation context across multiple turns
* Ensures:

  * No premature tool execution
  * Smooth multi-step interaction
  * Reset after completion

---

## 🏗️ System Architecture

The system is designed in a modular way:

* **Intent Module** → Classifies user input
* **RAG Module** → Retrieves relevant information from knowledge base
* **Agent Logic** → Controls conversation flow
* **State Manager** → Stores user progress and context
* **Tool Layer** → Executes lead capture

This separation ensures scalability and easy integration with real-world systems.

---

## 🛠️ Tech Stack

* **Language:** Python 3
* **Framework:** Modular Agent Design (LangChain-ready structure)
* **LLM Ready:** Compatible with GPT / Gemini / Claude
* **Storage:** JSON-based knowledge base
* **Execution:** CLI-based conversational interface

---

## ▶️ How to Run

```bash
pip install -r requirements.txt
python main.py
```

---

## 💬 Example Conversation

```
User: Hi  
Bot: Hello! 👋 How can I help you with AutoStream?

User: What is your pricing?  
Bot: 
Basic Plan: $29/month...
Pro Plan: $79/month...

User: I want to try Pro plan  
Bot: What's your name?

User: Sarika  
User: sarika@gmail.com  
User: YouTube  

✅ Lead captured successfully!
```

---

## 📦 Project Structure

```
autostream-agent/
│
├── main.py
├── agent.py
├── intent.py
├── rag.py
├── tools.py
├── memory.py
├── requirements.txt
├── README.md
└── data/
    └── knowledge.json
```

---

## 📲 WhatsApp Integration (Concept)

To deploy this agent on WhatsApp:

1. Use **Twilio WhatsApp API**
2. Create a backend server (Flask / FastAPI)
3. Set up a webhook to receive messages
4. Pass incoming messages to the agent
5. Send responses back via Twilio

This enables real-time conversational automation on messaging platforms.

---

## 🧪 Evaluation Alignment

This implementation satisfies all assignment requirements:

* ✔ Intent detection
* ✔ RAG-based responses
* ✔ Lead capture workflow
* ✔ State management
* ✔ Tool execution logic
* ✔ Clean modular code structure

---

## 🚀 Future Improvements

* Replace rule-based intent detection with LLM-based classification
* Integrate vector database (FAISS) for semantic RAG
* Deploy using LangGraph for production-grade workflows
* Add UI (Streamlit / Web App)
* Integrate real CRM APIs

---

## 👩‍💻 Author

Sarika Dorepally

---

## 📌 Conclusion

This project demonstrates a real-world **Agentic AI workflow**, combining:

* Reasoning
* Retrieval
* Action execution

It reflects how modern AI systems can convert conversations into measurable business outcomes.
