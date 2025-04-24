from flask import Flask, request, render_template
import google.generativeai as genai
import os
from dotenv import load_dotenv
import re

app = Flask(__name__)
load_dotenv()
genai.configure(api_key=os.getenv("API_KEY"))

model = genai.GenerativeModel("gemini-1.5-flash-latest")

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    response_title = ""
    
    if request.method == "POST":
        user_prompt = request.form["prompt"]
        full_prompt = f"""
Sen bir Python kodlama asistanısın. Kullanıcının verdiği isteğe göre:
1. Kodu açıklayan kısa ve öz bir başlık üret (ilk satırda, # ile yaz),
2. Ardından Python kodunu yaz.

İstek: {user_prompt}
        """

        try:
            result = model.generate_content(full_prompt)
            generated_code = result.text.strip()

            match = re.match(r"#\s*(.+)", generated_code)
            if match:
                response_title = match.group(1).strip()
                response = re.sub(r"^#\s*.+\n?", "", generated_code).strip()
            else:
                response_title = "Python Kodu"
                response = generated_code

        except Exception as e:
            response = f"Bir hata oluştu: {e}"
            response_title = "Hata"

    return render_template("index.html", response=response, response_title=response_title)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

