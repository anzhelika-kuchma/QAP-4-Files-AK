# Program description: This program generates a graph that shows the total sales over months based on the user's input.
# Written by:          Anzhelika Kuchma
# Date written:        July 25 - July 25 - 2023

# Required libraries:
import matplotlib.pyplot as plt
from matplotlib import style


# Main program

monthsLst = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
salesLst = []
for m in range(0, len(monthsLst)):
    while True:
        try:
            sales = int(input(f'Enter the total amount of sales for {monthsLst[m]}: '))
        except:
            print("Error - Amount of sales must be a valid number - Please reenter.")
        else:
            if sales < 0:
                print("Error - Amount of sales must be a positive number - Please reenter.")
            else:
                break

    salesLst.append(sales)

style.use('ggplot')
x_axis = monthsLst
y_axis = salesLst

fig, ax = plt.subplots()

ax.bar(x_axis, y_axis, align='center', color='blue')

ax.set_title('Total Sales ($)')
ax.set_ylabel('CAD')
ax.set_xlabel('Months')

ax.set_xticks(x_axis)
ax.set_xticklabels(('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

plt.show()


