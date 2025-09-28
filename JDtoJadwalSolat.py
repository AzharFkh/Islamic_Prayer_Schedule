import math

def acot(x):
    return math.atan(1 / x) if x != 0 else math.pi / 2

def sudut_deklinasi(JD):
    """Hitung sudut deklinasi (delta) dalam derajat"""
    T = 2.0 * math.pi * (JD - 2451545.0) / 365.25
    delta = (0.37877
             + 23.264 * math.sin(math.radians(57.297 * T - 79.547))
             + 0.3812 * math.sin(math.radians(2 * 57.297 * T - 82.682))
             + 0.17132 * math.sin(math.radians(3 * 57.297 * T - 59.722)))
    return delta

def waktu_transit(JD, longitude, timezone):
    """Hitung waktu transit (jam lokal)"""
    U = (JD - 2451545) / 36525
    L0 = 280.46607 + 36000.7698 * U
    L0_rad = math.radians(L0)

    ET = (-(1789 + 237 * U) * math.sin(L0_rad)
          - (7146 - 62 * U) * math.cos(L0_rad)
          + (9934 - 14 * U) * math.sin(2 * L0_rad)
          - (29 + 5 * U) * math.cos(2 * L0_rad)
          + (74 + 10 * U) * math.sin(3 * L0_rad)
          + (320 - 4 * U) * math.cos(3 * L0_rad)
          - 212 * math.sin(4 * L0_rad)) / 1000.0

    return 12 + timezone - (longitude / 15) - (ET / 60)

def HA(h, L, delta):
    """Hour angle (radian)"""
    return math.acos(
        (math.sin(math.radians(h)) - math.sin(math.radians(L)) * math.sin(math.radians(delta)))
        / (math.cos(math.radians(L)) * math.cos(math.radians(delta)))
    )

def to_hhmm(time_decimal):
    """Ubah jam desimal ke format HH:MM"""
    jam = int(time_decimal)
    menit = int(round((time_decimal - jam) * 60))
    if menit == 60:
        jam += 1
        menit = 0
    return f"{jam:02d}:{menit:02d}"

def jadwal_solat(JD, latitude, longitude, timezone, altitude=0, KA=1, h_subuh=-20, h_isya=-18):
    """
    Hitung waktu sholat (Subuh, Terbit, Zuhur, Ashar, Maghrib, Isya)
    :param JD: Julian Day
    :param latitude: lintang (positif = LU, negatif = LS)
    :param longitude: bujur (derajat)
    :param timezone: zona waktu (jam dari UTC)
    :param altitude: ketinggian lokasi (meter)
    :param KA: konstanta ashar (1 = Syafi'i, 2 = Hanafi)
    :param h_subuh: altitude matahari untuk Subuh (°)
    :param h_isya: altitude matahari untuk Isya (°)
    """
    delta = sudut_deklinasi(JD)
    WT = waktu_transit(JD, longitude, timezone)

    # Altitude untuk maghrib (sunset)
    h_maghrib = -0.8333 - 0.0347 * (altitude ** 0.5)

    # Sudut jam
    h_ashar = math.degrees(acot(KA + math.tan(math.radians(abs(delta - latitude)))))
    HA_ashar = HA(h_ashar, latitude, delta)
    HA_maghrib = HA(h_maghrib, latitude, delta)
    HA_isya = HA(h_isya, latitude, delta)
    HA_subuh = HA(h_subuh, latitude, delta)

    # Waktu sholat (jam desimal)
    zuhur = WT
    ashar = WT + math.degrees(HA_ashar) / 15
    maghrib = WT + math.degrees(HA_maghrib) / 15
    isya = WT + math.degrees(HA_isya) / 15
    subuh = WT - math.degrees(HA_subuh) / 15
    terbit = WT - math.degrees(HA_maghrib) / 15

    return {
        "Subuh": to_hhmm(subuh),
        "Terbit": to_hhmm(terbit),
        "Zuhur": to_hhmm(zuhur),
        "Ashar": to_hhmm(ashar),
        "Maghrib": to_hhmm(maghrib),
        "Isya": to_hhmm(isya)
    }
