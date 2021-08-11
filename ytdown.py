from pytube import YouTube
import sys

def banner():
    print()
    print("         _________ ______   _______           _       ")
    print("|\     /|\__   __/(  __  \ (  ___  )|\     /|( (    /|")
    print("( \   / )   ) (   | (  \  )| (   ) || )   ( ||  \  ( |")
    print(" \ (_) /    | |   | |   ) || |   | || | _ | ||   \ | |")
    print("  \   /     | |   | |   | || |   | || |( )| || (\ \) |")
    print("   ) (      | |   | |   ) || |   | || || || || | \   |")
    print("   | |      | |   | (__/  )| (___) || () () || )  \  |")
    print("   \_/      )_(   (______/ (_______)(_______)|/    )_)")
    print()
    print("Per comodita' il file verrà scaricato nella cartella di questo programma")
    print("\t\t--Urolit")


def getinput():
    print()
    print("Inserisci il link > ")
    toreturn = input()
    if len(toreturn) < 5:
        print("\nInput non valido :<")
        sys.exit(0)
    return toreturn


def askformato():
    print()
    print("Vuoi scaricare il video o solo l'audio? ( V / A ) >")
    formato = input()
    if formato.upper() == "V":
        return "video"
    elif formato.upper() == "A":
        return "audio"
    else:
        print("VIDEO O AUDIO ! RISPONDI CON ' V ' OPPURE CON ' A '  !!")
        print("AAAAAAAAAAAAAA!!")
        sys.exit(0)


def gettag():
    print("Pensaci un attimo e dimmi quale vuoi scaricare")
    print("Poi inserisci il numero di tag > ")
    tag = int(input())
    return tag


def main():
    banner()
    video = YouTube(getinput())
    formato = askformato()
    try:
        s = str(video.streams.all)
        lista = s.split(">,")
        for x in range(len(lista)):
            if formato in lista[x]:
                print(lista[x])
    except:
        print("\nErrore indefinito >_<")
        sys.exit(0)

    # prendo il tag da scaricare per poi avviare il download
    try:
        tag = gettag()
        print("Loading...")
        video.streams.get_by_itag(tag).download()
    except:
        print("Errore indefinito pt.2 \t T_T")

    print("Done !!")


main()