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
├── chef/                     
│   ├── migrations/           
│   ├── static/               
│   │   └── chef/css/style.css
│   ├── templates/chef/       
│   │   └── home.html
│   ├── forms.py              
│   ├── views.py              
│   ├── langchain.py          
│   └── models.py             
│
├── media/                    
│
├── chefdjango/               
│   ├── settings.py           
│   ├── urls.py               
│   └── wsgi.py               
│
├── .env                      
├── .gitignore                
├── README.md                 
├── manage.py                 
└── requirements.txt          

<h2>⚙️ Installation & Setup (Run Locally)</h2>

Follow these steps to set up the project on your local machine 👇

1️⃣ Clone the Repository
git clone https://github.com/puneetyadav/AI-Master-Chef.git
cd AI-Master-Chef

2️⃣ Create and Activate Virtual Environment
 <br>python -m venv venv
<br>venv\Scripts\activate   # (On Windows)
## or
source venv/bin/activate  # (On macOS/Linux)

3️⃣ Install Dependencies
<br>pip install -r requirements.txt

4️⃣ Set Up Environment Variables

<br>Create a file named .env in the root folder:

<br>GOOGLE_API_KEY="your-gemini-api-key-here"

5️⃣ Run Migrations
<br>python manage.py migrate

6️⃣ Start the Development Server
<br>python manage.py runserver


Now open your browser and go to 👉 http://127.0.0.1:8000/

<h2>🧠 How It Works</h2>

<h3>User enters a dish name or ingredients in the form.

The backend sends this input to Gemini AI model.

The AI returns:

A short intro about the dish 🍽️

List of ingredients 🥦

Step-by-step instructions 👨‍🍳

Optional tips or serving suggestions ✨

The result is displayed beautifully below the form with a friendly chef animation.</h3>


## Screenshot

<img src="Screenshot 2025-10-15 233717.png">


