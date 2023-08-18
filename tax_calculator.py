# Questo programma calcola le tasse sul reddito:
# Questo loop serve a rilanciare il programma quando finisce di essere eseguito
while True:
    entrate = input("Inserisci il tuo reddito, altrimenti, 'exit' per uscire: ")
    # Questa condizione termina il programma
    if entrate.lower() == "exit":
        print("Exiting the program.")
        break

    status = input("Per favore, inserisci 's' per singolo o 'm' per sposato: ")

    # Inizializza costanti per le aliquote e per i limiti degli scaglioni
    RATE1 = 0.10
    RATE2 = 0.25
    RATE1_SINGLE_LIMIT = 32000.0
    RATE1_MARRIED_LIMIT = 64000.0

    # Converti l'input delle entrate in un numero in virgola mobile
    entrate = float(entrate)

    # Calcolo delle tasse
    tax1 = 0.0
    tax2 = 0.0

    if status != "exit":
        if status == "s":
            if entrate <= RATE1_SINGLE_LIMIT:
                tax1 = RATE1 * entrate
            else:
                tax1 = RATE1 * RATE1_SINGLE_LIMIT
                tax2 = RATE2 * (entrate - RATE1_SINGLE_LIMIT)
        else:
            if entrate <= RATE1_MARRIED_LIMIT:
                tax1 = RATE1 * entrate
            else:
                tax1 = RATE1 * RATE1_MARRIED_LIMIT
                tax2 = RATE2 * (entrate - RATE1_MARRIED_LIMIT)

        total_tax = tax1 + tax2
        net_income = entrate - total_tax

        print("Per entrate lorde pari a: $%.2f \nLa tassa è $%.2f, di cui la parte tassata al %.2f%% è: $%.2f \ne la parte tassata al %.2f%% è: $%.2f \nAl netto: $%.2f" % (entrate, total_tax, RATE1 * 100, tax1, RATE2 * 100, tax2, net_income))
