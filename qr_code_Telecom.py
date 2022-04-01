import qrcode
img = qrcode.make("https://www.youtube.com/c/TELCOMATraining/playlists")
img.save("Telecoma_playlist_QRcode.jpg")