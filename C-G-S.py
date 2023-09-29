import numpy as np
import matplotlib.pyplot as plt
import PySimpleGUI as sg


sg.theme('Dark Green 5')

# Define the layout for the title page
layout = [
    [sg.Text('CSV Graphing Software', font=('Helvetica', 30), justification='center')],
    [sg.Button('Launch', size=(15, 1), font=('Helvetica', 14))],
    [sg.Text('Developed for Quantum Aerospace', font=('Helvetica', 14), justification='center')]
]

# Create the title window
title_window = sg.Window('C.G.S', layout, element_justification='c')

# Event loop
while True:
    event, values = title_window.read()
    if event == 'Launch':
        break
    if event == sg.WIN_CLOSED:
        exit()

# Close the title window when done
title_window.close()







# Define the PySimpleGUI layout
layout = [
    [sg.Text('Filename:')],
    [sg.InputText(key='-FILENAME-')],
    [sg.Text('X-Axis Column (0-9):')],
    [sg.InputText(key='-XAXIS-')],
    [sg.Text('Y-Axis Column(0-9):')],
    [sg.InputText(key='-YAXIS-')],
    [sg.Text('Scale Factor (1 for default):')],
    [sg.InputText(key='-SCALE-')],
    [sg.Button('OK'), sg.Button('Cancel')],
]

# Create the PySimpleGUI window
window = sg.Window('C.G.S', layout)

answer = None  # Initialize the answer variable

while True:
    event, values = window.read()

    if event in (sg.WIN_CLOSED, 'Cancel'):
        exit()
    elif event == 'OK':
        answer = values['-FILENAME-']  # Store the filename in the 'answer' variable
        xaxis = int(values['-XAXIS-'])
        yaxis = int(values['-YAXIS-'])
        scale = float(values['-SCALE-'])
        break


window.close()



# Load the CSV file
filename = answer  # Replace 'your_file.csv' with your actual CSV file name
data = np.genfromtxt(filename, delimiter=',')

# Extract the columns
seconds = data[:, xaxis]
ay = data[:, yaxis]  # Assuming ay is in the third column (index 2)

# Take the absolute value of ay
abs_ay = np.abs(ay)

# Multiply by the scaling factor (0.000061)
abs_ay_scaled = abs_ay * scale

# Create the plot
plt.figure(figsize=(10, 6))  # Set the figure size (adjust as needed)
plt.plot(seconds, abs_ay_scaled, label = answer, color='b')  # Plot the scaled absolute value of ay
plt.xlabel('X-Axis')
plt.ylabel('Y-Axis')
plt.title('AGS')
plt.legend()
plt.grid(True)

# Save the plot as an image
plot_filename = 'graph.png'
plt.savefig(plot_filename)
plt.close()

# Define the PySimpleGUI layout
layout = [
    [sg.Text('Graph')],
    [sg.Image(filename=plot_filename)],
    [sg.Button('Exit')]
]

# Create the PySimpleGUI window
window = sg.Window('C.G.S Graph', layout, finalize=True)

# Event loop
while True:
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        exit()

window.close()
