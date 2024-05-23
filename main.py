import math
import pictures
import los
import nlos_low
import nlos_high

def free_space_loss(R_k,f_G):
    return 32.4+20*math.log10(f_G*1000)+20*math.log10(R_k)


h_b=float(input("Wysokość umieszczenia anteny stacji bazowej [m]: "))
f_G=float(input("Częstotliwość fali z zakresu [0.9; 2], [GHz]: "))
if (f_G > 2.0) or (f_G < 0.9):
    input("Częstotliwość spoza zakresu! Naciśnij ENTER aby zakończyć program.")
    exit(1)

R_k=float(input("Odleglość między antenami [0.05;3] [km]: "))
if(R_k < 0.05) and (R_k > 3.0):
    input("Odleglość spoza zakresu. Naciśnij ENTER aby zakończyć program.")
    exit(1)

LOS=True
if input("[L]OS/[N]LOS: ").upper()[0]=="N":
    LOS=False

if LOS:
    h_m=float(input("Wysokość umieszczenia anteny terminala ruchomego [m]: "))
    R_bk=(4*h_b*h_m)/(1000*1/f_G)
    away=False
    if R_k>R_bk:
        print(f"Straty propagacji w warunkach LOS, odległość dalsza niż punkt załamania fali ({round(R_bk,2)} m):",round(los.away(R_k,R_bk,f_G,h_b,h_m),2))
        print(f"W porównaniu do strat w swobodnej przestrzeni:",round(free_space_loss(R_k,f_G),2))
    else:
        print(f"Straty propagacji w warunkach LOS, odległość bliższa (bądź równa) niż punkt załamania fali ({round(R_bk,2)} m):",round(los.near(R_k,f_G,h_b),2))
        print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k,f_G),2))
    exit(0)

model=input("Typ trasy:"+pictures.models_merged+"\n\t>> ")[0].upper()
if not (model=="S" or model=="P" or model=="B"):
    input("Niepoprawny wybór trasy! Naciśnij ENTER aby zakończyć program.")
    exit(1)

height = False
if input("Typ zabudowy: [W]ysoka (>=10 pięter)/[N]iska: ").upper()[0] == "W":
    height = True


# dla NLOS niskiego:
if not height:
    h_m=float(input("Wysokość umieszczenia anteny terminala ruchomego [m]: "))
    h_BD=float(input("Średnia wysokość budynków (szczególnie poprzedzającego terminal ruchomy) [m]: "))
    delta_h=h_b-h_BD
    if (delta_h<=-8) or (delta_h>=6):
        input("Różnica wysokości anteny stacji bazowej (h_b) i średniej wysokości budynków (h_BD) spoza zakresu (-8;6)! Naciśnij ENTER aby zakończyć program.")
        exit(1)
    r_h=float(input("Odległość między budynkami [m]: "))/2
    match model:
        case "S":
            print("Straty propagacji dla trasy schodkowej w niskiej zabudowie:",round(nlos_low.staircase(R_k, f_G, delta_h, r_h, h_m, h_BD),2))
            print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k,f_G),2))
        case "P":
            print("Straty propagacji dla trasy schodkowej w niskiej zabudowie:",round(nlos_low.transverse(R_k, f_G, delta_h, r_h, h_m, h_BD),2))
            print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k,f_G),2))
        case "B":
            print("Straty propagacji dla trasy schodkowej w niskiej zabudowie:",round(nlos_low.lateral(R_k, f_G, delta_h, r_h, h_m, h_BD),2))
            print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k,f_G),2))
    exit(0)

match model:
    case "S":
        print("Straty propagacji dla trasy schodkowej w wysokiej zabudowie:",round(nlos_high.staircase(R_k,f_G,h_b),2))
        print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k,f_G),2))
    case "P":
        print("Straty propagacji dla trasy schodkowej w wysokiej zabudowie:",round(nlos_high.transverse(R_k,f_G,h_b),2))
        print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k,f_G),2))
    case "B":
        print("Straty propagacji dla trasy schodkowej w wysokiej zabudowie:",round(nlos_high.lateral(R_k,f_G,h_b),2))
        print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k,f_G),2))
exit(0)