import pandas as pd
import matplotlib.pyplot as plt

# Load the data from the CSV file into a DataFrame
data = pd.read_csv('Medals.csv')
plt.figure(figsize=(10, 6))
plt.plot(data['Team'], data['Total'], color='blue')

plt.xlabel('Team Name', fontsize=14.6, fontdict={'fontname': 'DejaVu Sans'})
plt.ylabel('Total Number of Medals', fontsize=14.6, fontdict={'fontname': 'DejaVu Sans'})
plt.title('Team-wise Total Medal Data', fontsize=18.5, fontdict={'fontname': 'DejaVu Sans'})
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)
#plt.savefig('plot1.png')
plt.show()