import PySimpleGUI as sg
from pprint import pformat, pprint

sg.theme("DarkBrown1")
sg.set_options(font=("Ubuntu", 16),
               scaling=2,
               margins=(150, 150),
               element_padding=(10, 10))


def oldmenu(basic_options: dict, special_options: dict = None, title=""):
    options = basic_options | (special_options if special_options else {})
    enum = {str(i): op for i, op in enumerate(options, 1)}
    while 1:
        print("[" + title + "]")
        for (i, op) in enum.items():
            print(i, "->", op)
        ch = input("Enter your choice: ")
        if ch in enum and enum[ch] in options:
            # print("Chosen: ", enum[ch], "->", options[enum[ch]])
            if isinstance(options[enum[ch]], str):
                if options[enum[ch]] == "Back":
                    break
                print(options[enum[ch]])
            elif isinstance(options[enum[ch]], dict):
                menu(title + " > " + enum[ch], options[enum[ch]])
            else:
                options[enum[ch]]()
        else:
            print("Invalid option, please try again")
    return "Back"


def passfunc():
    pass


def menu(title: str, options1: dict, options2: dict = None):
    options = options1 | (options2 if options2 else {})
    layout = [
        [sg.T(title)], [[sg.Button(op)] for op in options1] +
        [[sg.Button(op, button_color=('white', 'red'))
          for op in options2] if options2 else []]
    ]

    window = sg.Window(title, layout, modal=True)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, ): break
        if event not in options: continue
        # print("Chosen: ", event, "->", options[event])
        target = options[event]
        if isinstance(target, str):
            if target == "Back":
                break
            sg.Popup(target, keep_on_top=True)
        elif isinstance(target, dict):
            menu(title + " > " + event, target)
        else:
            window.close()
            target()

    window.close()


def inputbox(title, text, default=""):
    layout = [[sg.Text(text)], [sg.Input(default_text=default)],
              [sg.Button("OK")]]

    window = sg.Window(title, layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "OK"): break

    window.close()
    return values[0] if event == "OK" else None


def input_values(title, fields: dict, default: dict = None):
    layout = [[
        sg.Text(text),
        sg.Input(
            key=key,
            password_char=("*" if key == "password" else ""),
            default_text=(default[key] if default and key in default else ""),
        )
    ] for key, text in fields.items()
              ] + [[sg.Button("OK"), sg.Button("Cancel")]]

    window = sg.Window(title, layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "OK", "Cancel"): break

    window.close()
    return values if event == "OK" else None


def confirm(title, text):
    layout = [[sg.Text(text)], [sg.Button("Yes"), sg.Button("No")]]

    window = sg.Window(title, layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "No"): break

    window.close()
    return event == "Yes"


def display(title, text):
    layout = [[sg.T(text)], [sg.Button("OK")]]

    window = sg.Window(title, layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "OK"): break

    window.close()


def display_table(title, data: list, headings: list):
    layout = [[sg.Table(data, headings, auto_size_columns=True)],
              [sg.Button("OK")]]

    window = sg.Window(title, layout)

    while True:
        event, values = window.read()
        if event in (sg.WIN_CLOSED, "OK"): break

    window.close()


def display_cursor_table(title, cur):
    data = [list(i) for i in cur.fetchall()]
    headings = [i[0] for i in cur.description]
    display_table(title, data, headings)