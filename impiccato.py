# ===================== #
# IMPICCATO             #
# ===================== #
# importo il modulo random che mi servirà in seguito per scegliere casualmente la parola con cui giocare
import random
import os
from grafica import stages

# apro il file dizionario.txt contenente una serie lunghissima di parole e le inserisco in una lista da cui poi andrò a pescarne una random
with open("dizionario.txt", "r") as file:
    allText = file.read()
    word_list = list(map(str, allText.split()))
chosen_word = random.choice(word_list)
# inizializzo una variabile contenente le vite del giocatore (max. 6) che andranno a decrescere ad ogni errore
lives = 6

# definisco una lista vuota, e vado a riempirla con tanti "_" quante sono le lettere di chosen_word; mi servirà per rappresentare graficamente la situazione al giocatore
display = []
for i in range(len(chosen_word)):
    display.append("_")

# da qui in poi inizia il cuore del gioco; inserisco tutto in un while loop in modo da permettere all'utente di provare ad indovinare lettere finchè la chosen_word ha dei blanks "_"; il flag end_of_game mi servirà per capire quando la partita è finita e quando, quindi, bisognerà uscire dal while loop
end_of_game = False
# finchè end_of_game è settata su False il loop ciclerà (not nega la situazione normale di True)
while not end_of_game:
    # chiedo all'utente di scegliere una lettera casuale e la salvo nella variabile guess; dato che python è case sensitive mi assicuro che ogni lettera venga settata in lower case in modo che l'utente non mandi in crash il gioco in caso di errore accidentale
    guess = input("\nScegli una lettera: ").lower()
    os.system('clear')

    if guess in display:
        print(f"\nHai già scelto la lettera {guess}!\n")
    # vado a ciclare la chosen_word e salvo di volta in volta ogni lettera della parola nella variabile letter (per comodità), che andrò poi a confrontare con la lettera scelta dall'utente e contenuta nella variabile guess
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        # se letter e guess corrispondono, e cioè se l'utente ha indovinato la lettera, vado a sostituirla al "_" nella lista display, in modo da rappresentare a video successivamente la situazione al giocatore
        if letter == guess:
            display[position] = letter
    # se invece l'utente non ha indovinato, e quindi guess NON è presente in chosen_word, diminuisco il suo numero di vite di un'unità; ATTENZIONE: questo va fatto fuori dal ciclo for!!!
    if guess not in chosen_word:
        print(
            f"\nHai scelto la lettera {guess}, ma non fa parte della parola. Perdi una vita.\n")
        lives -= 1

    # questa non la conoscevo, ma serve in poche parole per trasformare la lista in stringa e avere quindi una grafica più carina
    print(f"{' '.join(display)}")
    # stampo infine anche la situazione dell'impiccagione, andando a pescare l'ASCII corrispondente dalla lista stages
    print(stages[lives])

    # questa parte finale serve per controllare se la partita è finita o meno; nel caso in cui non ci fossero più "_" nella chosen_word (ossia l'utente ha indovinato la parola senza consumare tutte le vite) flaggeremo end_of_game a True e questo ci farà uscire dal loop dopo aver stampato a video un messaggio di vittoria
    if "_" not in display:
        end_of_game = True
        print("\nGrande, hai vinto!!!")
    # nel caso in cui, invece, le vite dovessero scendere a zero end_of_game verrà flaggato a True anch'esso, in modo da poter uscire dal loop e verrà stampato un messaggio di sconfitta
    elif lives == 0:
        end_of_game = True
        print(
            f"\nHai perso tutte le tue vite! :( La parola corretta era '{chosen_word}'")
