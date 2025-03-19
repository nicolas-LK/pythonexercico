import os
from flask import Flask, render_template_string

app = Flask(__name__)

# 🔹 Configuração da página personalizada
TARGET_DATE = "2025-12-28 23:59:59"  # Data para contagem regressiva
MESSAGE = "3 MESES NAMORANDO A MULHER MAIS LINDA E MARAVILHOSA DESSE MUNDO. EU TE AMO, MINHA PRINCESA! ❤️"  # Mensagem personalizada com coração

# 🔹 Criar pasta 'static' caso não exista
if not os.path.exists('static'):
    os.makedirs('static')

# 🔹 Página HTML dinâmica
template = """
<!DOCTYPE html>
<html lang=\"pt\">
<head>
    <meta charset=\"UTF-8\">
    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
    <title>Surpresa Especial</title>
    <style>
        body {
            font-family: 'Georgia', serif;
            text-align: center;
            background-color: #F8E1F4; /* Rosa claro */
            color: #6A4C9C; /* Lavanda */
            margin: 0;
            padding: 20px;
        }
        h1 {
            font-family: 'Brush Script MT', cursive;
            color: #FF1493; /* Pink vibrante */
            font-size: 3em;
            text-shadow: 2px 2px 5px rgba(0, 0, 0, 0.2);
        }
        #countdown {
            font-family: 'Arial Black', sans-serif;
            font-size: 2.5em;
            font-weight: bold;
            color: #FF4500; /* Cor vibrante para suspense */
        }
        .carousel {
            display: flex;
            justify-content: center;
            align-items: center;
            width: 100%;
            height: 300px;
            overflow: hidden;
            margin: 20px auto;
            position: relative;
        }
        .carousel-container {
            display: flex;
            animation: scroll 30s linear infinite; /* Efeito contínuo */
        }
        .carousel img {
            width: 100%;
            height: 300px;
            object-fit: cover;
            border-radius: 10px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
        }
        @keyframes scroll {
            0% {
                transform: translateX(0);
            }
            100% {
                transform: translateX(-100%); /* Move a área de visualização para a esquerda */
            }
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
    <h1>{{ message }} ❤️</h1>
    <h2>Contagem Regressiva para nosso aniversário de 1 ano juntos:</h2>
    <p id="countdown"></p>

    <!-- Carrossel de Imagens -->
    <div class="carousel">
        <div class="carousel-container">
            <img src="https://i.postimg.cc/d14n5PMG/01.jpg" alt="Imagem 1">
            <img src="https://i.postimg.cc/zf1rrWy0/02.avif" alt="Imagem 2">
            <img src="https://i.postimg.cc/g2sff5Pk/03.jpg" alt="Imagem 3">
            <img src="https://i.postimg.cc/8Chrpht5/04.avif" alt="Imagem 4">
            <img src="https://i.postimg.cc/Gt6d3WZG/05.jpg" alt="Imagem 5">
            <img src="https://i.postimg.cc/N00s4k7y/06.jpg" alt="Imagem 6">
            <img src="https://i.postimg.cc/D06pBLcZ/07.avif" alt="Imagem 7">
            <img src="https://i.postimg.cc/d1pGv1tB/08.jpg" alt="Imagem 8">
            <img src="https://i.postimg.cc/0NLNyJDb/09.avif" alt="Imagem 9">
            <img src="https://i.postimg.cc/25vDT9LS/11.jpg" alt="Imagem 10">
            <img src="https://i.postimg.cc/TYSFSq6L/12.jpg" alt="Imagem 11">
            <img src="https://i.postimg.cc/rwsWdx0J/13.jpg" alt="Imagem 12">
            <img src="https://i.postimg.cc/43hW9r7B/14.jpg" alt="Imagem 13">
        </div>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(template, target_date=TARGET_DATE, message=MESSAGE)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
