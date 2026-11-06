from varasto import Varasto


def tulosta_alkutila(mehua, olutta):
    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")


def testaa_setterit(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")


def testaa_virheelliset_luonnit():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    print(Varasto(-100.0))

    print("Varasto(100.0, -50.7)")
    print(Varasto(100.0, -50.7))


def testaa_lisays(nimi, varasto, maara):
    print(f"{nimi}: {varasto}")
    print(f"lisaa_varastoon({maara})")
    varasto.lisaa_varastoon(maara)
    print(f"{nimi}: {varasto}")


def testaa_otto(nimi, varasto, maara):
    print(f"{nimi}: {varasto}")
    print(f"ota_varastosta({maara})")
    saatiin = varasto.ota_varastosta(maara)
    print(f"saatiin {saatiin}")
    print(f"{nimi}: {varasto}")


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    tulosta_alkutila(mehua, olutta)
    testaa_setterit(mehua)
    testaa_virheelliset_luonnit()

    testaa_lisays("Olutvarasto", olutta, 1000.0)
    testaa_lisays("Mehuvarasto", mehua, -666.0)
    testaa_otto("Olutvarasto", olutta, 1000.0)
    testaa_otto("Mehuvarasto", mehua, -32.9)


if __name__ == "__main__":
    main()
