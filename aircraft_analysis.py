import numpy as np
import matplotlib.pyplot as plt

#Altitude range (real aircraft range)
altitude = np.linspace(0, 26000, 200)

#Real max speeds (km/h)
sr71_max = 3400
mig25_max = 3000

#Tuned scaling factors (based on operational altitude)
k_sr71 = 6000   #SR-71 accelerates faster at high altitude
k_mig25 = 7500  #MiG-25 slower buildup

#Exponential approach model
speed_sr71 = sr71_max * (1 - np.exp(-altitude / k_sr71))
speed_mig25 = mig25_max * (1 - np.exp(-altitude / k_mig25))
#Speed of sound ≈ 1225 km/h (at sea level)
mach_sr71=speed_sr71/1225
mach_mig25=speed_mig25/1225

#Speed vs altitude graph
plt.plot(altitude, speed_sr71, label="SR-71 Blackbird", linewidth=2)
plt.plot(altitude, speed_mig25, label="MiG-25 Foxbat", linewidth=2)

plt.xlabel("Altitude (m)")
plt.ylabel("Speed (km/h)")
plt.title("High-Speed Aircraft Performance vs Altitude")

plt.legend()
plt.grid(True)
#Mach graph
plt.figure()
plt.plot(altitude, mach_sr71, label="SR-71 Blackbird", linewidth=3,linestyle='--')
plt.plot(altitude, mach_mig25, label="MiG-25 Foxbat", linewidth=3,linestyle='--')

plt.xlabel("Altitude (m)")
plt.ylabel("Mach number")
plt.title("Mach vs Altitude")

plt.legend()
plt.grid(True)
plt.show()