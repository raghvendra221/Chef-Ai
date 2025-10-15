# 🍳 AI Master Chef

**AI Master Chef** is an intelligent web application that generates cooking recipes using AI (Gemini API).  
Users can type any dish name or available ingredients, and the AI will provide a detailed recipe — all served with an elegant, glassy UI and chef animation.

---

## 🚀 Features

- 🧠 **AI-Powered Recipes:** Uses Google Gemini to generate custom recipes.  
- 🧑‍🍳 **Chef Animation & Intro:** Friendly animated chef introduces each recipe.  
- 🪞 **Modern Glassmorphism UI:** Smooth blurred background and dynamic design.  
- 📸 **Image Upload Preview:** Users can preview uploaded food images before submission.  
- 💾 **Session-Based Output:** Keeps recent recipe responses for the session.  
- ⚙️ **Environment Security:** Uses `.env` to store API keys safely.

---

## 🧩 Tech Stack

| Layer | Technology Used |
|-------|------------------|
| Frontend | HTML, CSS (Glassmorphism UI), JavaScript |
| Backend | Django (Python) |
| AI Model | Google Gemini API |
| Database | SQLite (default Django DB) |
| Others | dotenv for environment variables |

---

## 📁 Project Structure

AI-Master-Chef/
├── chef/                     # Main Django app (handles forms, AI logic, and templates)
│   ├── migrations/           # Database migrations
│   ├── static/               # Static assets (CSS, JS, images)
│   │   └── chef/css/style.css
│   ├── templates/chef/       # HTML templates
│   │   └── home.html
│   ├── forms.py              # Django form for recipe input
│   ├── views.py              # View logic for GET/POST requests
│   ├── langchain.py          # Contains Gemini AI integration logic
│   └── models.py             # (Optional) Database models
│
├── media/                    # Stores uploaded images
│
├── chefdjango/               # Django project configuration
│   ├── settings.py           # Settings (API, static/media, etc.)
│   ├── urls.py               # URL routing
│   └── wsgi.py               # WSGI entry point
│
├── .env                      # API key and secret variables
├── .gitignore                # Ignored files and folders (e.g., .env, __pycache__)
├── README.md                 # Project documentation
├── manage.py                 # Django management script
└── requirements.txt           # Python dependencies

⚙️ Installation & Setup (Run Locally)

Follow these steps to set up the project on your local machine 👇

1️⃣ Clone the Repository
git clone https://github.com/puneetyadav/AI-Master-Chef.git
cd AI-Master-Chef

2️⃣ Create and Activate Virtual Environment
python -m venv venv
venv\Scripts\activate   # (On Windows)
# or
source venv/bin/activate  # (On macOS/Linux)

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Set Up Environment Variables

Create a file named .env in the root folder:

GOOGLE_API_KEY="your-gemini-api-key-here"

5️⃣ Run Migrations
python manage.py migrate

6️⃣ Start the Development Server
python manage.py runserver


Now open your browser and go to 👉 http://127.0.0.1:8000/

🧠 How It Works

User enters a dish name or ingredients in the form.

The backend sends this input to Gemini AI model.

The AI returns:

A short intro about the dish 🍽️

List of ingredients 🥦

Step-by-step instructions 👨‍🍳

Optional tips or serving suggestions ✨

The result is displayed beautifully below the form with a friendly chef animation.

🧾 Environment Variables
Variable	Description
GOOGLE_API_KEY	Your Gemini API key from Google AI Studio
📸 Preview

(Add screenshots or GIFs of your app here)

Example:

![App Screenshot](https://your-screenshot-link.com/demo.png)

👨‍💻 Author

Puneet Yadav
💼 GitHub: @puneetyadav

📧 Email: puneetyadav@example.com

🛡️ License

This project is open-source and available under the MIT License
.
