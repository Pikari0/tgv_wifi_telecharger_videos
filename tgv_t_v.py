import requests

catalogue = requests.get("https://wifi.sncf/router/api/videos/catalog").json()

for i in range(len(catalogue)):
    print(i,catalogue[i]['id'])

choix = int(input("Catégorie : "))

for video in catalogue[choix]['videos']:
    print("Téléchargement de %s " %video['id'])
    url = video['files']['fr']['video']
    video = requests.get("https://wifi.sncf%s"%url)
    print(video)
    nom = url.split('/')
    nom = nom[len(nom)-1]
    print("Écriture de %s"%nom)
    fichier = open(nom,"wb")
    fichier.write(video.content)
    fichier.close()
    
