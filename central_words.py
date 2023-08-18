#questo programma estrae le lettere centrali di una data parola.

#questo loop serve a rilanciare il programma quando finisce di essere eseguito
while True:
    parola = input("Enter something (or type 'exit' to quit): ")
#questa condizione termina il programma
    if parola.lower() == "exit":
        print("Exiting the program.")
        break
#codice
    posizione = len(parola) // 2

    if len(parola) % 2 == 1:
        risultato = parola[posizione]
    else:
        risultato = parola[posizione - 1] + parola[posizione]

    print("Result:", risultato)
