# 🌊 AquaGuard AI — Smart Water Usage Advisor 
AI-powered assistant promoting sustainable water usage  
Built using **Python + Flask + TF-IDF semantic retrieval**

---

## 📝 Overview
AquaGuard AI is a lightweight AI chatbot that provides **smart, contextual water-saving recommendations**.  
It helps students, families, and communities learn **how to reduce daily water consumption** through personalized suggestions.

No external APIs required — the app runs fully locally.

---

## 🎯 Objectives
✔ Promote sustainable water usage habits  
✔ Raise awareness of water scarcity challenges  
✔ Support United Nations SDG Goals  
✔ Provide an easy, smart, and interactive assistant

---

## 🌍 SDG Alignment
This project supports:
- **SDG 6 — Clean Water and Sanitation**
- **SDG 12 — Responsible Consumption and Production**
- **SDG 13 — Climate Action**

---

## 🚀 Features
- 🤖 AI-powered recommendations using TF-IDF retrieval
- 🌐 Clean and simple Flask-based web UI
- 📁 Easy to update knowledge base
- ⚡ Fast and works offline
- 🧠 Mini-RAG concept without external APIs

---

## 🛠️ Tech Stack
- Python 3.x
- Flask
- Scikit-learn
- HTML + CSS

---

## 📂 Project Structure
```
AquaGuard-AI/
│── app.py
│── knowledge_base.txt
│── requirements.txt
│── templates/
│     └── index.html
│── static/
│     └── screenshots/ (optional)
│── README.md
```

---

## 📦 Installation

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/aquaguard-ai.git
cd aquaguard-ai
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

If missing, create requirements.txt:
```
flask
scikit-learn
```

---

## ▶️ Run the App
```bash
python app.py
```

Visit in browser:
```
http://127.0.0.1:5000/
```

---

## 💬 Usage Guide
1. Type any question related to water conservation  
2. System retrieves top relevant suggestions  
3. You receive personalized water-saving advice  
4. Modify knowledge_base.txt anytime to change results

Examples:
```
How can I save water while brushing?
Best ways to take bath without wasting water?
```

---

## 🧠 How the AI Works
AquaGuard AI uses a simplified version of RAG (Retrieval-Augmented Generation):

1️⃣ Convert stored sentences into TF-IDF vectors  
2️⃣ Convert user query into a vector  
3️⃣ Compute cosine similarity  
4️⃣ Return top 2–3 matched tips

This design:
- Uses no API keys
- Works fully offline
- Runs fast on any system

---

## 📁 Knowledge Base
Located in:
```
knowledge_base.txt
```

Add tips freely, e.g.:
```
Fix leaking taps immediately to save up to 500L per week.
Use bucket baths instead of showers.
Close taps while brushing teeth.
Reuse kitchen water for plants.
```

Restart app to refresh.

---


---

## 🧩 Future Enhancements
- PDF-based RAG retrieval
- Water usage calculator
- SQLite-based usage tracking
- Full chatbot UI
- IBM Granite integration
- IoT flow meter simulation
- Mobile App version (React Native / Flutter)

---

## 👩‍💻 Contributing
Pull requests are welcome — open an issue to discuss ideas!

---

## 📝 License
MIT License — free to use, modify, and share.

---

## 🙌 Credits
Built by **Dhanushya M**  
For **1M1B + IBM SkillsBuild AI & Sustainability Internship**  
Supervised learning + innovation project

---

### ⭐ Support the Project
If you like it:  
🌟 Star the repository  
🔀 Fork to extend  
🗣 Share with others
