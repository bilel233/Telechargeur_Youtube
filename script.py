from pytube import YouTube          # bibliotheque d'imports pytube

def download_video(url,output_path='.'):
    """telecharge la video youtube et la met dans le repertoire
    ."""

    try:
        # on cree un objet youtube avec l'url de la video
        video = YouTube(url)

        # on selectionne la meilleure qualite disponible
        stream = video.streams.get_highest_resolution()

        # on telecharge la video dans le dossier de sortie specifie
        stream.download(output_path)

        print("Le telechargement s'est terminé avec succés.")
    except Exception as e:
        print("Erreur lors du telechargement",e)




