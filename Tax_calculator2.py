# Questo programma calcola le tasse sul reddito:

# Inizializza costanti per le aliquote e per i limiti degli scaglioni
RATE1 = 0.10
RATE2 = 0.25
RATE1_SINGLE_LIMIT = 32000.0
RATE1_MARRIED_LIMIT = 64000.0

# Leggi il reddito e lo stato civile
entrate = float(input("Inserisci il tuo reddito: "))
status = input("Per favore, inserisci 's' per singolo o 'm' per sposato: ")

# Calcolo delle tasse
tax1 = 0.0
tax2 = 0.0

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

print("Per entrate lorde pari a: $%.2f \nLa tassa è $%.2f, di cui la parte tassata al %.2f%% è $%.2f e la parte tassata al %.2f%% è $%.2f \nAl netto : $%.2f" % (entrate, total_tax, RATE1 * 100, tax1, RATE2 * 100, tax2, net_income))
