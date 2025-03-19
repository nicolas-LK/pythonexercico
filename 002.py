import os
import qrcode
from flask import Flask, render_template_string

app = Flask(__name__)

# 🔹 Configuração da página personalizada
TARGET_DATE = "2025-12-28 23:59:59"  # Data para contagem regressiva
IMAGE_URL ='https://i.postimg.cc/gk5521hn/SAVE-20250313-125307.jpg'  # Substitua pelo link correto
MESSAGE = "3 MESES NAMORANDO A MULHER MAIS LINDA E PERFEITA DESSE MUNDO. EU TE AMO, MINHA PRINCESA!"  # Mensagem personalizada

# 🔹 Criar pasta 'static' caso não exista
if not os.path.exists('static'):
    os.makedirs('static')

# 🔹 Gerar QR Code e salvar na pasta 'static'
qr = qrcode.make("http://127.0.0.1:5000/")
qr.save("static/qrcode.png")  # Salvar localmente na pasta 'static'

# 🔹 Página HTML dinâmica
template = """
<!DOCTYPE html>
<html lang="pt">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Surpresa Especial</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            text-align: center;
            background-color: #f4f4f4;
            margin: 0;
            padding: 20px;
        }
        h1 {
            color: #333;
        }
        img {
            width: 300px;
            border-radius: 10px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        #countdown {
            font-size: 24px;
            font-weight: bold;
            color: red;
        }
    </style>
    <script>
        function countdown() {
            var targetDate = new Date("{{ target_date }}").getTime();
            var x = setInterval(function() {
                var now = new Date().getTime();
                var distance = targetDate - now;

                var days = Math.floor(distance / (1000 * 60 * 60 * 24));
                var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
                var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
                var seconds = Math.floor((distance % (1000 * 60)) / 1000);

                document.getElementById("countdown").innerHTML = days + "d " + hours + "h " + minutes + "m " + seconds + "s ";
                if (distance < 0) {
                    clearInterval(x);
                    document.getElementById("countdown").innerHTML = "Tempo esgotado!";
                }
            }, 1000);
        }
    </script>
</head>
<body onload="countdown()">
    <h1>{{ message }}</h1>
    <img src="{{ image_url }}" alt="Imagem Personalizada">
    <h2>Contagem Regressiva para nosso aniversário de um 1 ano juntos:</h2>
    <p id="countdown"></p>
    <h2>Escaneie o QR Code:</h2>
    <img src="{{ url_for('static', filename='qrcode.png') }}" alt="QR Code">
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template, target_date=TARGET_DATE, image_url=IMAGE_URL, message=MESSAGE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

