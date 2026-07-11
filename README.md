# 🎵 Ragam Guru — Carnatic Music AI Chatbot

<div align="center">

**An expert AI chatbot for Carnatic classical music powered by Groq (LLaMA 3.3 70B) + Gradio**

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/YOUR_USERNAME/carnatic-ragam-ai/blob/main/carnatic_ragam_ai.ipynb)

</div>

---

## ✨ Features

- 🎼 **Ragam Identification** — Ask "What ragam is _Entharo Mahanubhavulu_?" and get an instant, detailed answer
- 📚 **Ragam Details** — Full arohana, avarohana, vadi, samvadi, mood, rasa, time of day, and famous compositions
- 🕉️ **Carnatic Concepts** — Explain Melakartha system, gamaka, shruti, tala, and more
- 🎬 **Film Song Ragas** — Identify ragams of popular Tamil/Telugu/Kannada film songs
- 💬 **Multi-turn Chat** — Contextual conversation history maintained throughout the session
- ⚡ **Streaming Responses** — Real-time streaming via Groq API for fast, smooth UX

---

## 🚀 Quick Start

### 1. Get a Free Groq API Key
1. Go to [console.groq.com](https://console.groq.com)
2. Sign up for free
3. Generate an API key

### 2. Run Locally

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/carnatic-ragam-ai.git
cd carnatic-ragam-ai

# Install dependencies
pip install -r requirements.txt

# Set your API key
cp .env.example .env
# Edit .env and add your GROQ_API_KEY

# Run the app
python app.py
```

Open your browser at `http://localhost:7860`

### 3. Run on Google Colab
Click the **Open in Colab** badge above, then:
1. Add your Groq API key to Colab Secrets as `GROQ_API_KEY`
2. Run all cells
3. Click the Gradio public link

---

## 📁 Project Structure

```
carnatic-ragam-ai/
├── app.py                      # Main Gradio app (UI + Groq chat)
├── ragam_data.py               # Carnatic ragam knowledge base (100+ ragas)
├── requirements.txt            # Python dependencies
├── render.yaml                 # Render deployment config
├── .env.example                # API key template
├── .gitignore                  # Git ignore rules
├── README.md                   # This file
└── carnatic_ragam_ai.ipynb     # Google Colab notebook
```

---

## 🚢 Deploy to Render

### Step-by-Step

1. **Push to GitHub**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: Carnatic Ragam AI"
   git branch -M main
   git remote add origin https://github.com/YOUR_USERNAME/carnatic-ragam-ai.git
   git push -u origin main
   ```

2. **Create a Render Web Service**
   - Go to [render.com](https://render.com) → **New** → **Web Service**
   - Connect your GitHub repository

3. **Configure the Service**
   | Setting | Value |
   |---|---|
   | Runtime | Python |
   | Build Command | `pip install -r requirements.txt` |
   | Start Command | `python app.py` |

4. **Add Environment Variable**
   - In the Render dashboard → **Environment** tab
   - Add: `GROQ_API_KEY` = `your_groq_api_key_here`

5. **Deploy!**
   - Click **Deploy Web Service**
   - Your app will be live at `https://carnatic-ragam-ai.onrender.com`

> **Note:** On Render's free tier, the service spins down after 15 minutes of inactivity. The first request after inactivity may take 30–60 seconds to respond.

---

## 🎵 Ragas in the Database

**72 Melakartha Ragas (selected):**
Kanakangi, Shankarabharanam, Kalyani, Kharaharapriya, Natabhairavi, Harikambhoji, Mayamalavagowla, Todi, Charukeshi, Kiravani...

**Major Janya Ragas:**
Bhairavi, Mohanam, Hamsadhwani, Hindolam, Bilahari, Anandabhairavi, Abhogi, Saveri, Sindhu Bhairavi, Kambhoji, Sri, Amritavarshini, Suddha Dhanyasi, Reethigowla, Varali, Madhyamavati, Kedaram, Nilambari, Vasanta, Revati, Panthuvarali, Bhupalam, Arabhi, Navarasa Kannada, Desh, Behag, Kamaas, Bageshri...

---

## 💬 Example Conversations

| You ask | Ragam Guru responds |
|---|---|
| "What ragam is Entharo Mahanubhavulu?" | Sri Ragam — arohana, avarohana, significance... |
| "Tell me about Kalyani" | 65th Melakartha, S R2 G3 M2 P D2 N3 S, evening raga... |
| "Which ragas evoke sadness?" | Bhairavi, Hindolam, Sahana, Sindhu Bhairavi... |
| "What is the Melakartha system?" | 72 parent scales of Carnatic music explained... |
| "Difference between Bhairavi and Sindhu Bhairavi?" | Detailed comparison of arohana, mood, usage... |

---

## 🛠️ Technology Stack

| Component | Technology |
|---|---|
| AI Model | LLaMA 3.3 70B (via Groq) |
| Frontend | Gradio 4.x |
| Backend | Python 3.11 |
| Deployment | Render |
| Dev/Demo | Google Colab |

---

## 📜 About Carnatic Music

Carnatic music is one of the two main subgenres of Indian classical music, predominantly performed in South India (Tamil Nadu, Andhra Pradesh, Karnataka, Kerala). It is fundamentally based on the concept of **ragam** (melodic framework) and **talam** (rhythmic framework).

The **72 Melakartha system** is the mathematical framework of 72 parent scales from which hundreds of derived (janya) ragas are created, developed by the musicologist Venkatamakhi in the 17th century.

---

## 📄 License

MIT License — free to use, modify, and distribute.

---

<div align="center">
Made with ❤️ for Carnatic music lovers | Powered by Groq · LLaMA 3.3 · Gradio
</div>
