import broadway as bw
import json
import matplotlib.pyplot as plt
import numpy as np

bw_data = bw.get_shows()

# how many people attended the most popular shows
# the most popular shows

production = {}

for show in bw_data:
    show_name = show["Show"]["Name"]
    attendance = show["Statistics"]["Attendance"]

    if show_name not in production:
       production[show_name] = 0

    production[show_name] += attendance

filtered_prod = {k:v for k, v in production.items() if v > 3000000}
highest_int = max(filtered_prod.values())

plt.figure()
plt.bar(range(len(filtered_prod)), filtered_prod.values(), align="center", width=0.5)
plt.ylabel("number of people attended")
plt.title("broadway productions with the highest attendances ")
plt.xticks(range(len(filtered_prod)), list(filtered_prod.keys()) )
plt.tick_params(axis="x", rotation = -90)
plt.yticks(np.arange(0, highest_int + 1, 2000000))
#plt.show() # will only show one graph and stop 



# productions that made the most money before calculating costs 
grosses = {}
for show in bw_data:
    show_name = show["Show"]["Name"]
    gross = show["Statistics"]["Gross"]

    if show_name not in grosses:
        grosses[show_name] = 0

    grosses[show_name] += gross
    
filtered_gross = {g:b for g, b in grosses.items() if b > 300000000}
highest_int = max(filtered_gross.values())

plt.figure()
plt.bar(range(len(filtered_gross)), filtered_gross.values(), align="center", width= 0.3)
plt.ylabel("gross amount (dollars)")
plt.title("broadway productions with the highest gross incomes ")
plt.xticks(range(len(filtered_gross)), list(filtered_gross.keys()) )
plt.tick_params(axis="x", rotation = -90)
plt.yticks(np.arange(0, highest_int + 1, 200000000))
plt.show()