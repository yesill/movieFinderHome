class Film():

    number = str()
    name = str()
    year = str()
    runtime = str()
    rate = str()
    director = str()
    genre = str()
    summary = str()
    poster = str()

    def __init__(self,number,name,year,runtime,rate,director,genre,summary,poster):
        self.number = number
        self.name = name
        self.year = year
        self.runtime = runtime
        self.rate = rate
        self.director = director
        self.genre = genre
        self.summary = summary
        self.poster = poster