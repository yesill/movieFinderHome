from flask import Flask, render_template, request
from Arama import Arama
from Film import Film


"""arama nesnesi"""
arama = Arama()

""" <- flask -> """
app = Flask(__name__)

@app.route("/")
def page_index():
	return render_template('index.html')

@app.route("/search")
def page_search():
	aranan_film = str()
	#aranan film alinamazsa butun filmler arasndan random bir film onerilir.
	onerilen_film = arama.oneri(arama.searchParametresiz())

	try:
		aranan_film = request.args.get('search')
		#arama cubugu bos veya 1 harf ise
		if len(aranan_film) > 1:
			onerilen_film = arama.oneri(arama.search(aranan_film))
	except:
		pass

	#aranan film varsa
	if onerilen_film:
		return render_template('search.html',
								film_poster = onerilen_film.poster,
								film_name = onerilen_film.name,
								film_rate = onerilen_film.rate,
								film_director = onerilen_film.director,
								film_genre = onerilen_film.genre)
	#aranan film yoksa
	else:
		return render_template('search.html',
								film_poster = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR_e0Vi4b8M8uI5dg0esw9tL9itzJykhrALIQ&usqp=CAU",
								film_name = "bulunamadi..!",
								film_rate = "bulunamadi..!",
								film_director = "bulunamadi..!",
								film_genre = "bulunamadi..!")

@app.route("/genre")
def page_genre():

	genre = request.args.get('genre')
	onerilen_film = arama.searchGenre(genre)

	return render_template('genre.html',
								film_poster = onerilen_film.poster,
								film_name = onerilen_film.name,
								film_rate = onerilen_film.rate,
								film_director = onerilen_film.director,
								film_genre = onerilen_film.genre)


if __name__ == '__main__':
	app.run(debug=True)