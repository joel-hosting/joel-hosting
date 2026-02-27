from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Joel Hosting</title>
        <style>
            body {
                background-color: #0f172a;
                color: white;
                font-family: Arial;
                text-align: center;
                padding: 40px;
            }
            h1 {
                color: #38bdf8;
                font-size: 40px;
            }
            .card {
                background: #1e293b;
                padding: 20px;
                margin: 20px auto;
                width: 300px;
                border-radius: 10px;
            }
            a {
                display: inline-block;
                margin-top: 20px;
                padding: 10px 20px;
                background: #22c55e;
                color: white;
                text-decoration: none;
                border-radius: 5px;
            }
        </style>
    </head>
    <body>
        <h1>🚀 Joel Hosting</h1>
        <p>Creación de páginas web profesionales</p>

        <div class="card">
            <h2>Plan Básico</h2>
            <p>$25 USD</p>
        </div>

        <div class="card">
            <h2>Plan Profesional</h2>
            <p>$50 USD</p>
        </div>

        <a href="https://wa.me/18294257569">📲 Contáctame por WhatsApp</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run()
