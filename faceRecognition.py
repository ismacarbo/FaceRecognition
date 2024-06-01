import numpy as np # Libreria per il miglioramento delle strutture dati
import face_recognition as fr # Libreria per la ricognizione facciale
import cv2 # Libreria cv2

# Inizializza la cattura video dalla webcam
video_capture = cv2.VideoCapture(0)

# Crea gli encoding delle foto per la base della ricognizione
isma = fr.load_image_file("isma.jpg")
isma_encoding = fr.face_encodings(isma)[0]

facceNote = [isma_encoding]
nomiFacceNote = ["Isma"]

while True: 
    ret, frame = video_capture.read()  # Inserisce nella variabile frame il frame attuale

    rgb_frame = frame[:, :, ::-1]  # Siccome cv2 usa colori BGR, converto in RGB

    posizioneFacce = fr.face_locations(rgb_frame)  # Ottengo la posizione delle facce
    encodingFacce = fr.face_encodings(rgb_frame, posizioneFacce)  # Ottengo gli encoding delle facce trovate

    for (top, right, bottom, left), encodingFaccia in zip(posizioneFacce, encodingFacce):
        matches = fr.compare_faces(facceNote, encodingFaccia)

        nome = "Sconosciuto"

        # Ottengo la distanza tra la faccia rilevata e le facce note
        distanzaFacce = fr.face_distance(facceNote, encodingFaccia)

        # Con NumPy ottengo l'indice della faccia più vicina
        indiceMigliore = np.argmin(distanzaFacce)
        if matches[indiceMigliore]:
            nome = nomiFacceNote[indiceMigliore]

        # Disegno il rettangolo intorno alla faccia
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Disegno il rettangolo per il nome
        cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
        
        # Definisco il font
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        # Inserisco il nome nel rettangolo
        cv2.putText(frame, nome, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

    # Mostro il risultato in una finestra
    cv2.imshow('Webcam_facerecognition', frame)

    # Premere 'q' per uscire
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Rilascia la cattura video e chiude tutte le finestre
video_capture.release()
cv2.destroyAllWindows()
