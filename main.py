from utils.tle_parser import parse_tle
from models.gravity import simulate_orbit
from visualization.plot_3d import plot_3d_trajectory
from skyfield.api import load
from skyfield.api import EarthSatellite, load


# Загрузка TLE из файла
def get_iss_initial_state():
    # 1. Загружаем TLE
    with open('data/iss_tle.txt', 'r') as f:
        tle_lines = f.readlines()

    # 2. Создаем объект спутника через Skyfield
    satellite = EarthSatellite(tle_lines[1], tle_lines[2], tle_lines[0])

    # 3. Получаем начальное состояние (эпоха TLE)
    ts = load.timescale()
    t = ts.now()  # текущее время или время эпохи TLE

    # Позиция и скорость в геоцентрических координатах (метры)
    geocentric = satellite.at(t)
    position = geocentric.position.m
    velocity = geocentric.velocity.m_per_s

    return [
        position[0], position[1], position[2],  # x, y, z (м)
        velocity[0], velocity[1], velocity[2]  # vx, vy, vz (м/с)
    ]


# Параметры
GM = 3.986004418e14  # Гравитационный параметр Земли (м³/с²)
t_span = [0, 3600 * 24]  # 1 день в секундах

# Загрузка начальных условий МКС
initial_state = get_iss_initial_state()  # Теперь x,y,z,vx,vy,vz определены!

# Расчёт орбиты
sol = simulate_orbit(initial_state, t_span, GM)

# Визуализация
plot_3d_trajectory(sol)