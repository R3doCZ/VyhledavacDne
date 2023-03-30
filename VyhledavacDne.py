import datetime as dt
import tkinter as tk
import tkcalendar as tkc

#Dnešní datum
StartDen = dt.datetime.now().day
StartMesic = dt.datetime.now().month
StartRok = dt.datetime.now().year
KalendarOtevren = False

#Funkce pro vyhledání vybraného dne a zobrazení v Labelu
def Vyhledat(Den, Mesic, Rok):
    while True:
        Den+=1
        if (Den>28 and Mesic==2 and Rok%4!=0) or (Den>29 and Mesic==2 and Rok%4==0):    #Únor má méně dnů
            Den=0
            Mesic+=1
        elif (Mesic==4 or Mesic==6 or Mesic==9 or Mesic==11) and Den>30:   #Pro měsíce co nemají 31 dnů
            Den=0
            Mesic+=1
        elif Den>31:    #Pro zbytek měsíců
            Den=0
            Mesic+=1
        if Mesic>12:
            Mesic=0
            Rok+=1
        try:
            Weekday = dt.datetime(Rok, Mesic, Den).strftime("%A")   #Získání jména dne pomocí data, celý název %A (Friday atd.)
        except:
            pass
        if Den==VybranyDen.get() and Weekday==VyberDenJmenoMoznosti[VyberDenJmenoMoznostiCzech.index(VybranyDenJmeno.get())]:    #break v moment kdy Den a Název Dne odpovídá
            break
        
    DatumLabel["text"]=f"Nejbližší '{VybranyDenJmeno.get()} {VybranyDen.get()}.' je {Den:02}.{Mesic:02}.{Rok:04}"

#Funkce pro vytvoření okna pro kalendář s kalendářem a potvrzovacím tlačítkem
def Kalendar():
    global CalLevel, Calendar, KalendarOtevren
    if KalendarOtevren == False:
        CalLevel = tk.Toplevel()
        CalLevel.title("Výběr poč. data")
        CalLevel.resizable(tk.FALSE, tk.FALSE)
        CalLevel.protocol("WM_DELETE_WINDOW", KalendarZavrit)
        Calendar = tkc.Calendar(CalLevel, date_pattern="dd.mm.yyyy", selectmode="day")
        Calendar.pack()
        CalVyber = tk.Button(CalLevel, text="Vybrat datum", font=("16"), command=KalendarVyber)
        CalVyber.pack(padx=10, pady=5, fill=tk.X, expand=True)
        KalendarOtevren = True

#Funkce pro uložení vybraného data z kalendáře, a zavření okna kalendáře
def KalendarVyber():
    global StartDen, StartMesic, StartRok
    KalendarDatum = Calendar.get_date()
    StartDen = int(KalendarDatum[:2])
    StartMesic = int(KalendarDatum[3:5])
    StartRok = int(KalendarDatum[6:])
    #Vepsání do Entry
    StartDatum["state"]=tk.NORMAL
    StartDatum.delete(0, tk.END)
    StartDatum.insert(0, KalendarDatum)
    StartDatum["state"]=tk.DISABLED
    KalendarZavrit()
    
def KalendarZavrit():
    global KalendarOtevren
    CalLevel.destroy()
    KalendarOtevren = False


main = tk.Tk()
main.title("Vyhledávač dne")
main.geometry("300x225")
main.resizable(tk.FALSE, tk.FALSE)

StartFrame = tk.LabelFrame(main, text="Počáteční datum")    #Frame pro startovní datum
StartFrame.pack(padx=5, pady=5)
VyberFrame = tk.LabelFrame(main, text="Hledaný den")        #Frame pro výběr hledaného dne
VyberFrame.pack(padx=5, pady=5)

#Startovací datum Entry řádek
StartDatum = tk.Entry(StartFrame, justify="center")
StartDatum.grid(row=0, column=0, padx=5, pady=5)
StartDatum.insert(0, f"{StartDen:02}.{StartMesic:02}.{StartRok:04}")
StartDatum["state"]=tk.DISABLED

#Tlačítko na kalendář
CalButton = tk.Button(StartFrame, text="Kalendář", command=Kalendar)
CalButton.grid(row=0, column=1, padx=5, pady=5)

#Seznam výběru jména dnu
VyberDenJmenoMoznosti = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
VyberDenJmenoMoznostiCzech = ["Pondělí", "Úterý", "Středa", "Čtvrtek", "Pátek", "Sobota", "Neděle"]
VybranyDenJmeno = tk.StringVar()
VybranyDenJmeno.set(VyberDenJmenoMoznostiCzech[0])
VyberDenJmeno = tk.OptionMenu(VyberFrame, VybranyDenJmeno, *VyberDenJmenoMoznostiCzech)
VyberDenJmeno.grid(row=0, column=0, padx=5, pady=5)

#Seznam výběru dnu
VyberDenMoznosti=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
VybranyDen = tk.IntVar()
VybranyDen.set(1)
VyberDen = tk.OptionMenu(VyberFrame, VybranyDen, *VyberDenMoznosti)
VyberDen.grid(row=0, column=1, padx=5, pady=5)

#Tlačítko na funkci Vyhledat s startovacím dnem,měsícem a rokem
VyhledatBtn = tk.Button(main, text="Vyhledat den", font="18", command=lambda:Vyhledat(StartDen, StartMesic, StartRok))
VyhledatBtn.pack(padx=5, pady=5)

#Label pro zobrazení nalezeného data
DatumLabel = tk.Label(main, text="Nejbližší '______ __.' je __.__.____", font="16")
DatumLabel.pack(padx=5, pady=5)

main.mainloop()
