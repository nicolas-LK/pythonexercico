from flask import Flask, render_template
import os

app = Flask(__name__)


# Criar automaticamente as pastas e arquivos necessários
def setup_files():
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    os.makedirs('static/img', exist_ok=True)

    if not os.path.exists('templates/index.html'):
        with open('templates/index.html', 'w') as f:
            f.write("""<!DOCTYPE html>
<html lang='pt-br'>
<head>
    <meta charset='UTF-8'>
    <meta name='viewport' content='width=device-width, initial-scale=1.0'>
    <title>Nosso Amor</title>
    <link rel='stylesheet' href='/static/style.css'>
</head>
<body>
    <div class='hearts-container'></div>
    <div class='content'>
        <h1>Nosso Amor ❤️</h1>
        <img src='https://i.postimg.cc/gk5521hn/SAVE-20250313-125307.jpg' alt='Imagem Especial' class='main-image'>
        <div class='gallery'>
            <img src='/static/img/img1.jpg' alt='Foto 1'>
            <img src='/static/img/img2.jpg' alt='Foto 2'>
            <img src='/static/img/img3.jpg' alt='Foto 3'>
        </div>
        <p>Desde o dia em que te conheci, minha vida se tornou mais especial. Obrigado por tudo! Te amo ❤️</p>
    </div>
    <script src='/static/script.js'></script>
</body>
</html>""")

    if not os.path.exists('static/style.css'):
        with open('static/style.css', 'w') as f:
            f.write("""body {
    margin: 0;
    padding: 0;
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    height: 100vh;
    background-color: #ffebf0;
    overflow: hidden;
    font-family: Arial, sans-serif;
    text-align: center;
}
.hearts-container {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    pointer-events: none;
}
.content {
    position: relative;
    z-index: 10;
    background: white;
    padding: 20px;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
}
.main-image {
    width: 80%;
    max-width: 400px;
    margin: 20px 0;
    border-radius: 10px;
    box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.2);
}
.gallery img {
    width: 150px;
    height: 150px;
    object-fit: cover;
    margin: 10px;
    border-radius: 10px;
}""")

    if not os.path.exists('static/script.js'):
        with open('static/script.js', 'w') as f:
            f.write("""document.addEventListener('DOMContentLoaded', function() {
    function createHeart() {
        const heart = document.createElement('div');
        heart.classList.add('heart');
        heart.style.left = Math.random() * 100 + 'vw';
        heart.style.animationDuration = Math.random() * 2 + 3 + 's';
        document.querySelector('.hearts-container').appendChild(heart);
        setTimeout(() => {
            heart.remove();
        }, 5000);
    }
    setInterval(createHeart, 300);
});""")


setup_files()


@app.route('/')
def home():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)  # Modificado para host='0.0.0.0' e port=5001
