
from app import app
from app.models.newsModel import db, News
from flask import render_template, request, redirect


@app.route('/news', methods=['GET'])
def berita():
    listKonten = News.query.all()
    print(listKonten)
    return render_template('news.html', data=enumerate(listKonten, 1))


@app.route('/newspage', methods=['POST', 'GET'])
def newsPage():
    if request.method == 'POST':
        title = request.form['title']
        konten = request.form['konten']
        imaage = request.form['imaage']
        try:
            newsKonten = News(title=title,
                              konten=konten, imaage=imaage)

            db.session.add(newsKonten)
            db.session.commit()
        except Exception as e:
            print("Failed to add data.")
            print(e)
    listKonten = News.query.all()
    print(listKonten)
    return render_template("newsPage.html", data=enumerate(listKonten, 1))


@app.route('/createnews', methods=['POST', 'GET'])
def createNews():
    return render_template("createNews.html")


@app.route('/updatenews/<int:id>')
def updateForm(id):
    konten = News.query.filter_by(id=id).first()
    return render_template("updateNews.html", data=konten)


@app.route('/updatenews', methods=['POST'])
def updateNews():
    if request.method == 'POST':
        id = request.form['id']
        title = request.form['title']
        konten = request.form['konten']
        imaage = request.form['imaage']
        try:
            news = News.query.filter_by(id=id).first()
            news.title = title
            news.konten = konten
            news.imaage = imaage
            db.session.commit()
        except Exception as e:
            print("Failed to update data")
            print(e)
        return redirect("/newspage")


@app.route('/delete/<int:id>')
def delete(id):
    try:
        news = News.query.filter_by(id=id).first()
        db.session.delete(news)
        db.session.commit()
    except Exception as e:
        print("Failed delete mahasiswa")
        print(e)
    return redirect("/newspage")
