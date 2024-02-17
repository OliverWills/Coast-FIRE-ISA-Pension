import tkinter as tk
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np

def fire():
    try:
        networth = int(ent_networth.get())
        income = int(ent_income.get())
        expenses = int(ent_expenses.get())
        swr = int(ent_swr.get())
        interest = int(ent_interest.get())
        income_change = int(ent_income_change.get())
        expenses_change = int(ent_expenses_change.get())
        taxrate = int(ent_taxrate.get())

        years = 0
        x = []

        # Totals
        y_networth = []
        y_saved = []
        y_interest_collected = []

        # Annual
        y_annual_saving = []
        y_annual_interest = []
        saved = 0
        interest_collected = 0

        while networth < expenses / (100 - taxrate) * 100 * (100 / swr):
            income = income / 100 * (100 + income_change)
            expenses = expenses / 100 * (100 + expenses_change)
            networth = (networth + income - expenses) / 100 * (100 + interest)
            years = years + 1
            saved = saved + income - expenses
            interest_collected = interest_collected + (networth + income - expenses) * interest / 100
            annual_saving = income - expenses
            annual_interest = (networth + income - expenses) * interest / 100

            ## Data for Graphs
            x.append(years)
            y_networth.append(networth)
            y_saved.append(saved)
            y_interest_collected.append(interest_collected)
            y_annual_saving.append(annual_saving)
            y_annual_interest.append(annual_interest)

            if years >= 50:
                break
        if years >=50:
            lbl_result["text"] = 'Fire is not achievable under these condition'

        else:
            lbl_result["text"] = "You will achieve FIRE in {} years with a networth of {:,.0f} €".format(years, int(networth))
            ## Figure
            plt.style.use('ggplot')
            fig, axs = plt.subplots(nrows=2, sharex=True)
            ## Plots
            axs[0].plot(x, y_networth, color='blue')
            axs[0].plot(x, y_saved, color='green')
            axs[0].plot(x, y_interest_collected, color='purple')
            axs[1].plot(x, y_annual_saving, color='green')
            axs[1].plot(x, y_annual_interest, color='purple')

            ## Styling
            axs[0].set_title('Networth')
            axs[1].set_title('Annual Savings vs. Interest')
            axs[0].legend(['Networth', 'Saved', 'Interest Collected'])
            axs[1].legend(['Saving', 'Interest'])
            axs[0].yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x / 1000) + 'K'))
            axs[1].yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, pos: '{:,.0f}'.format(x / 1000) + 'K'))
            plt.xticks(np.arange(min(x), max(x)+1, 1))

            # Hide x labels and tick labels for top plots and y ticks for right plots.
            for ax in axs.flat:
                ax.set(xlabel='YEARS', ylabel='€')
            for ax in axs.flat:
                ax.label_outer()
            ## Adding to Window
            canvas = FigureCanvasTkAgg(fig, master=window)
            canvas.draw()
            canvas.get_tk_widget().grid(row=3, column=0, padx=10)
            frm_toolbar = tk.Frame(master=window)
            frm_toolbar.grid(row=4, column=0, padx=10)
            toolbar = NavigationToolbar2Tk(canvas, frm_toolbar)
            toolbar.update()

    except ValueError:
        lbl_result["text"] = 'Please make sure to enter values in all fields!'



# Initiate Main Window
window = tk.Tk()
window.title('FIRE Calculator')

# Entry Frame
frm_entry = tk.Frame(master=window)

## Networth
lbl_networth = tk.Label(master=frm_entry, text="Networth:")
ent_networth = tk.Entry(master=frm_entry, width=10)
lbl_networth_cur = tk.Label(master=frm_entry, text="€")

lbl_networth.grid(row=2, column=0, sticky="w")
ent_networth.grid(row=2, column=1, sticky="e")
lbl_networth_cur.grid(row=2, column=2, sticky="w")

## Income
lbl_income = tk.Label(master=frm_entry, text="Income:")
ent_income = tk.Entry(master=frm_entry, width=10)
lbl_income_cur = tk.Label(master=frm_entry, text="€")

lbl_income.grid(row=0, column=0, sticky="w")
ent_income.grid(row=0, column=1, sticky="e")
lbl_income_cur.grid(row=0, column=2, sticky="w")

## Expenses
lbl_expenses = tk.Label(master=frm_entry, text="Expenses:")
ent_expenses = tk.Entry(master=frm_entry, width=10)
lbl_expenses_cur = tk.Label(master=frm_entry, text="€")

lbl_expenses.grid(row=1, column=0, sticky="w")
ent_expenses.grid(row=1, column=1, sticky="e")
lbl_expenses_cur.grid(row=1, column=2, sticky="w")

## Income Change
lbl_income_change = tk.Label(master=frm_entry, text="Income Change:")
ent_income_change = tk.Entry(master=frm_entry, width=10)
lbl_income_change_cur = tk.Label(master=frm_entry, text="%")
ent_income_change.insert(0, '0')

lbl_income_change.grid(row=0, column=3, sticky="w")
ent_income_change.grid(row=0, column=4, sticky="e")
lbl_income_change_cur.grid(row=0, column=5, sticky="w")

## Expenses Change
lbl_expenses_change = tk.Label(master=frm_entry, text="Expenses Change:")
ent_expenses_change = tk.Entry(master=frm_entry, width=10)
lbl_expenses_change_cur = tk.Label(master=frm_entry, text="%")
ent_expenses_change.insert(0, '0')

lbl_expenses_change.grid(row=1, column=3, sticky="w")
ent_expenses_change.grid(row=1, column=4, sticky="e")
lbl_expenses_change_cur.grid(row=1, column=5, sticky="w")

## Interest
lbl_interest = tk.Label(master=frm_entry, text="Interest:")
ent_interest = tk.Entry(master=frm_entry, width=10)
lbl_interest_cur = tk.Label(master=frm_entry, text="%")
ent_interest.insert(0, '6')
lbl_interest.grid(row=0, column=6, sticky="w")
ent_interest.grid(row=0, column=7, sticky="e")
lbl_interest_cur.grid(row=0, column=8, sticky="w")

## SWR
lbl_swr = tk.Label(master=frm_entry, text="SWR:")
ent_swr = tk.Entry(master=frm_entry, width=10)
lbl_swr_cur = tk.Label(master=frm_entry, text="%")
ent_swr.insert(0, '4')

lbl_swr.grid(row=1, column=6, sticky="w")
ent_swr.grid(row=1, column=7, sticky="e")
lbl_swr_cur.grid(row=1, column=8, sticky="w")

## Taxrate
lbl_taxrate = tk.Label(master=frm_entry, text="Taxrate:")
ent_taxrate = tk.Entry(master=frm_entry, width=10)
lbl_taxrate_cur = tk.Label(master=frm_entry, text="%")
ent_taxrate.insert(0, '0')

lbl_taxrate.grid(row=2, column=6, sticky="w")
ent_taxrate.grid(row=2, column=7, sticky="e")
lbl_taxrate_cur.grid(row=2, column=8, sticky="w")

## Age
lbl_taxrate = tk.Label(master=frm_entry, text="Age:")
ent_taxrate = tk.Entry(master=frm_entry, width=10)
lbl_taxrate_cur = tk.Label(master=frm_entry, text="%")
ent_taxrate.insert(0, '35')

lbl_taxrate.grid(row=3, column=0, sticky="w")
ent_taxrate.grid(row=3, column=1, sticky="e")
lbl_taxrate_cur.grid(row=3, column=2, sticky="w")

## TargetReqtirementAge
lbl_taxrate = tk.Label(master=frm_entry, text="Target Reqtirement Age:")
ent_taxrate = tk.Entry(master=frm_entry, width=10)
lbl_taxrate_cur = tk.Label(master=frm_entry, text="Years")
ent_taxrate.insert(0, '67')

lbl_taxrate.grid(row=4, column=0, sticky="w")
ent_taxrate.grid(row=4, column=1, sticky="e")
lbl_taxrate_cur.grid(row=4, column=2, sticky="w")

## PreRetirementSWR
lbl_taxrate = tk.Label(master=frm_entry, text="PreRetirement SWR:")
ent_taxrate = tk.Entry(master=frm_entry, width=10)
lbl_taxrate_cur = tk.Label(master=frm_entry, text="%")
ent_taxrate.insert(0, '8')

lbl_taxrate.grid(row=5, column=0, sticky="w")
ent_taxrate.grid(row=5, column=1, sticky="e")
lbl_taxrate_cur.grid(row=5, column=2, sticky="w")

## CurrentPension
lbl_taxrate = tk.Label(master=frm_entry, text="Current Pension:")
ent_taxrate = tk.Entry(master=frm_entry, width=10)
lbl_taxrate_cur = tk.Label(master=frm_entry, text="£")
ent_taxrate.insert(0, '0')

lbl_taxrate.grid(row=6, column=0, sticky="w")
ent_taxrate.grid(row=6, column=1, sticky="e")
lbl_taxrate_cur.grid(row=6, column=2, sticky="w")

## CurrentISA
lbl_taxrate = tk.Label(master=frm_entry, text="Current ISA:")
ent_taxrate = tk.Entry(master=frm_entry, width=10)
lbl_taxrate_cur = tk.Label(master=frm_entry, text="£")
ent_taxrate.insert(0, '0')

lbl_taxrate.grid(row=7, column=0, sticky="w")
ent_taxrate.grid(row=7, column=1, sticky="e")
lbl_taxrate_cur.grid(row=7, column=2, sticky="w")

# Calculate Button
btn_calculate = tk.Button(
    master=window,
    text="Calculate",
    command=fire
)
# Bind 'ENTER' to Function
#window.bind('<Return>', fire)

# Result
## Text
lbl_result = tk.Label(master=window)
frm_entry.grid(row=0, column=0, padx=10)
btn_calculate.grid(row=1, column=0, pady=10)
lbl_result.grid(row=2, column=0, padx=10)

#Run
window.mainloop()