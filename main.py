import math
import pictures
import los
import nlos_low
import nlos_high
# import matplotlib.pyplot as plt
# import numpy

# h_b = 15 m; R_k = 0,8 km;
# f_G = 1800 MHz; r_h = 1 i 2 m;
# h_bd = 12 m; h_m = 1,5;
# różne rodzaje zabudowy

def free_space_loss(R_k,f_G):
    return 32.4+20*math.log10(f_G*1000)+20*math.log10(R_k)


# plotX=numpy.arange(0.05,3,0.1)
# plotY=[]
# plotFree=[]

h_b=float(input("Wysokość umieszczenia anteny stacji bazowej [m]: "))
f_G=float(input("Częstotliwość fali z zakresu [0.9; 2], [GHz]: "))
if (f_G > 2.0) or (f_G < 0.9):
    input("Częstotliwość spoza zakresu! Naciśnij ENTER aby zakończyć program.")
    exit(1)

# for i in plotX:
#     plotFree.append(free_space_loss(i,f_G))

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
        print(f"Straty propagacji w warunkach LOS, odległość dalsza niż punkt załamania fali ({round(R_bk,2)} m):",round(los.away(R_k,R_bk,f_G,h_b,h_m),2),"dB")
        print(f"W porównaniu do strat w swobodnej przestrzeni:",round(free_space_loss(R_k,f_G),2),"dB")
        # for i in plotX:
        #     plotY.append(los.away(i,R_bk,f_G,h_b,h_m))
        # plt.plot(plotX,plotFree,color="black")
        # plt.plot(plotX,plotY)
        # plt.plot(R_k,los.away(R_k,R_bk,f_G,h_b,h_m),"or")
        # plt.xlabel("Odległość anten [km]")
        # plt.ylabel("Straty propagacji w warunkach LOS")
        # plt.show()

    else:
        print(f"Straty propagacji w warunkach LOS, odległość bliższa (bądź równa) niż punkt załamania fali ({round(R_bk,2)} m):",round(los.near(R_k,f_G,h_b),2),"dB")
        print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k,f_G),2),"dB")
    exit(0)

model=input("Typ trasy:"+pictures.models_merged+"\n\t>> ")[0].upper()
if not (model=="S" or model=="P" or model=="B" or model=="M"):
    input("Niepoprawny wybór trasy! Naciśnij ENTER aby zakończyć program.")
    exit(1)

height = False
if input("Typ zabudowy: [W]ysoka (>=10 pięter)/[N]iska: ").upper()[0] == "W":
    height = True


if not height:
    h_m=float(input("Wysokość umieszczenia anteny terminala ruchomego [m]: "))
    h_BD=float(input("Średnia wysokość budynków (szczególnie poprzedzającego terminal ruchomy) [m]: "))
    delta_h=h_b-h_BD
    if (delta_h<=-8) or (delta_h>=6):
        input("Różnica wysokości anteny stacji bazowej (h_b) i średniej wysokości budynków (h_BD) spoza zakresu (-8;6)! Naciśnij ENTER aby zakończyć program.")
        exit(1)
    r_h=float(input("Odległość anteny terminala względem najbliższego budynku na trasie propagacji [m]: "))
    match model:
        case "S":
            print("Straty propagacji dla trasy schodkowej w niskiej zabudowie:",round(nlos_low.staircase(R_k, f_G, delta_h, r_h, h_m, h_BD),2),"dB")
            print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k,f_G),2),"dB")
        case "P":
            print("Straty propagacji dla trasy schodkowej w niskiej zabudowie:",round(nlos_low.transverse(R_k, f_G, delta_h, r_h, h_m, h_BD),2),"dB")
            print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k,f_G),2),"dB")
        case "B":
            print("Straty propagacji dla trasy schodkowej w niskiej zabudowie:",round(nlos_low.lateral(R_k, f_G, delta_h, r_h, h_m, h_BD),2),"dB")
            print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k,f_G),2),"dB")
        case "M":
            print("Straty propagacji dla trasy schodkowej w niskiej zabudowie:",round(nlos_low.merged(R_k, f_G, delta_h, r_h, h_m, h_BD), 2), "dB")
            print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k, f_G), 2), "dB")
    exit(0)

match model:
    case "S":
        print("Straty propagacji dla trasy schodkowej w wysokiej zabudowie:",round(nlos_high.staircase(R_k,f_G,h_b),2),"dB")
        print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k,f_G),2),"dB")
    case "P":
        print("Straty propagacji dla trasy schodkowej w wysokiej zabudowie:",round(nlos_high.transverse(R_k,f_G,h_b),2),"dB")
        print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k,f_G),2),"dB")
    case "B":
        print("Straty propagacji dla trasy schodkowej w wysokiej zabudowie:",round(nlos_high.lateral(R_k,f_G,h_b),2),"dB")
        print(f"W porównaniu do strat w swobodnej przestrzeni:", round(free_space_loss(R_k,f_G),2),"dB")
exit(0)