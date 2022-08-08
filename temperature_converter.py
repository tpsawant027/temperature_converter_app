import tkinter as tk


def refresh():
    val.set("Fahrenheit_to_Celsius")
    entry.delete(0, tk.END)
    label_from["text"] = ""
    label_to["text"] = ""
    label_warning["text"] = ""


def submit():
    opt = val.get()
    if opt == options[0]:
        label_from["text"] = f"\N{DEGREE CELSIUS}"
        label_to["text"] = f"\N{DEGREE FAHRENHEIT}"
    elif opt == options[1]:
        label_from["text"] = f"\N{DEGREE CELSIUS}"
        label_to["text"] = f"\N{KELVIN SIGN}"
    elif opt == options[2]:
        label_from["text"] = f"\N{KELVIN SIGN}"
        label_to["text"] = f"\N{DEGREE CELSIUS}"
    elif opt == options[3]:
        label_from["text"] = f"\N{DEGREE FAHRENHEIT}"
        label_to["text"] = f"\N{KELVIN SIGN}"
    elif opt == options[4]:
        label_from["text"] = f"\N{KELVIN SIGN}"
        label_to["text"] = f"\N{DEGREE FAHRENHEIT}"
    else:
        label_from["text"] = f"\N{DEGREE FAHRENHEIT}"
        label_to["text"] = f"\N{DEGREE CELSIUS}"


def temp_convert():
    if entry.get().isdigit():
        if val.get() == options[0]:
            label_to["text"] = f"{round((float(entry.get()) * 1.8)) + 32} \N{DEGREE FAHRENHEIT}"
        elif val.get() == options[1]:
            label_to["text"] = f"{round(float(entry.get()) + 273)} \N{KELVIN SIGN}"
        elif val.get() == options[2]:
            label_to["text"] = f"{round(float(entry.get()) - 273)} \N{DEGREE CELSIUS}"
        elif val.get() == options[3]:
            label_to["text"] = f"{round((float(entry.get()) + 459.67)/ 1.8)} \N{KELVIN SIGN}"
        elif val.get() == options[4]:
            label_to["text"] = f"{round(1.8 * (float(entry.get()) - 273.15) + 32)} \N{DEGREE FAHRENHEIT}"
        else:
            label_to["text"] = f"{round((float(entry.get()) - 32) * 5/9)} \N{DEGREE CELSIUS}"
        label_warning["text"] = ""
    else:
        label_warning["text"] = "INVALID INPUT"


if __name__ == '__main__':
    window = tk.Tk()
    window.title("Temperature Converter")
    window.resizable(width=False, height=False)

    frame_1 = tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=2)
    frame_1.pack(padx=5, pady=5)
    options = ["Celsius_to_Fahrenheit", "Celsius_to_Kelvin", "Kelvin_to_Celsius",
               "Fahrenheit_to_Kelvin", "Kelvin_to_Fahrenheit"]
    val = tk.StringVar(master=frame_1)
    val.set("Fahrenheit_to_Celsius")
    menu = tk.OptionMenu(frame_1, val, *options)
    menu.grid(row=0, column=0, padx=5, pady=5)
    sub_button = tk.Button(master=frame_1, text="Submit", command=submit)
    sub_button.grid(row=0, column=1, padx=5, pady=5)
    ref_button = tk.Button(master=frame_1, text="Refresh", command=refresh)
    ref_button.grid(row=0, column=2, padx=5, pady=5)

    frame = tk.Frame(master=window)
    frame.pack(padx=5, pady=5)
    entry = tk.Entry(master=frame, width=10)
    entry.grid(row=0, column=0, padx=5, pady=5)
    label_from = tk.Label(master=frame, text="")
    label_from.grid(row=0, column=1, sticky="w")
    button = tk.Button(master=frame, text="\N{RIGHTWARDS BLACK ARROW}", command=temp_convert)
    button.grid(row=0, column=2, padx=5, pady=5)
    label_to = tk.Label(master=frame, text="")
    label_to.grid(row=0, column=3, padx=5, pady=5)

    label_warning = tk.Label(master=window, text="", fg="Red")
    label_warning.pack(padx=5, pady=5)

    window.mainloop()
