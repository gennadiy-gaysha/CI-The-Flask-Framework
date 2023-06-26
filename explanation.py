# When we install a package, it plugs into the code that we've
# already written.We can use as much or as little of that package's
# functionality as you need.

# A framework, however, inverts that control. In a framework, most of
# the code is already written, and we have to plug your code into it.

# Flask is a web-based micro framework than uses Python. Which means
# that we don't get a lot of features out of the box, like we would with
# a larger framework such as Django for instance. Flask doesn't come with
# a default database engine, but the appeal of it, is its simplicity.

# после инсталяции веб фреймворка Flask импортируем класс Flask:
from flask import Flask

# создаем экземпляр нашего приложения через конструктор класса Flask:
#
# веб-сервер, на котором находится наше веб-приложение все запросы
# от пользователей приложения будет передавать этому объекту через
# протокол, который называется web-server gateway interface - WSGI
# Экземпляр приложения - это объект класса Flask

app = Flask(__name__)

# С помощью переменной __name__ фреймворк Flask сможет определить пути
# к корневому каталогу, чтобы оттуда брать файл ресурсов

# Пользователи нашего приложения отправляют запрос на сервер, который
# перенаправляет запросы нашему экземпляру-приложению.
# Наш экземпляр должен понять, какой же код должен быть выполнен, чтобы
# обработать эти обращения по url-адресу.
# ПОЭТОМУ: он должен хранить отображения адресов url в функции на языке
# Python.
# Ассоциацию между адресом url и функцией называют маршрутом.
# Чтобы определить маршрут в приложении используя Flask, можно
# воспользоваться декоратором @app.route. Этот декоратор зарегистрирует
# декорированную функцию как маршрут

# Декораторы в Python используются для регистрации функций в качестве обработчика
# событий

# Пример для главной страницы нашего веб-приложения ("/") - url главной страницы

# В этом коде мы регистрируем обработчик событий-запросов к корневому url, т. е.
# @app.route('/') регистрирует обработчик событий при обращении к ссылке (стр. 37, 38)
# и ф-я index будет выполняться при обращении к главной станице нашего сайта


@app.route("/")
def index():
    return '<h1>"Hello world"</h1>'

# index() - это ф-я представления, или view function

# Пример обработки url, которая включает в себя параметр, который пользователь
# вводит руками и передает в программу (имя пользователя)


@app.route("/user/<name>")
def user(name):
    return '<h1>"Hello, %s"</h1>' % name
# Теперь по обращению на этот url ("/user/<name>"), мы получаем вывод на экран
# с помощью этого представления


# Экземпляр приложения имеет метод run, который запускает интегрированный веб-сервер,
# который используется только для веб разработки (не для продакшн решения)

if __name__ == '__main__':
    app.run(debug=True)
