############################################

# creer un programme avec une interface utilisateur simple
# et la possibilite de telecharger des videos youtubes dans differents formats.

############################################

import script           # import du module script
import tkinter as tk
from tkinter import ttk

print("==================================")

#script.download_video("https://www.youtube.com/watch?v=5TDxf4QXDlc&ab_channel=oneek1","./SUPINFO")

print("==================================")

# on creee la fenetre principale

root = tk.Tk()
# on cree et place les elements dans la fenetre
root.title("Youtube Video Downloader")
url_label = ttk.Label(root, text="URL de la vidéo:")
url_label.grid(row=0, column=0, pady=10, padx=10, sticky="w")

url_entry = ttk.Entry(root, width=40)
url_entry.grid(row=0, column=1, pady=10, padx=10, sticky="w")

output_label = ttk.Label(root, text="Chemin de destination:")
output_label.grid(row=1, column=0, pady=10, padx=10, sticky="w")

output_entry = ttk.Entry(root, width=40)
output_entry.grid(row=1, column=1, pady=10, padx=10, sticky="w")

download_button = ttk.Button(root, text="Télécharger", command=script.download_video)
download_button.grid(row=2, column=0, columnspan=2, pady=20)

status_label = ttk.Label(root, text="")
status_label.grid(row=3, column=0, columnspan=2, pady=10)

# Lancer la boucle principale

try:
    root.geometry("600x300")
    root.mainloop()
except Exception as e:
    print("erreur dans la boucle principale",e)


