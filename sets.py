import media
import remix

jaar = media.DjSet("Nicolas Jaar",
"Nicolas Jaar Boiler Room NYC DJ Set at Clown & Sunset Takeover",
"http://graphics8.nytimes.com/images/2013/10/13/magazine/13jaar1/mag-13jaar-t_CA0-articleLarge.jpg",
"https://www.youtube.com/watch?v=IUjWumGIqe8")

hopkins = media.DjSet("Jon Hopkins",
"Jon Hopkins Boiler Room LIVE Show",
"https://i.ytimg.com/vi/YBNgn8T0GWY/maxresdefault.jpg",
"https://www.youtube.com/watch?v=1t3fk4QPlD4")

fake = media.DjSet("Nathan Fake",
"Nathan Fake live in the Boiler Room",
"http://photo.partyflock.nl/images/144508/medium/501655.jpg",
"https://www.youtube.com/watch?v=nT2znG8cpnI")

sets = [jaar, hopkins, fake]

remix.open_movies_page(sets)
