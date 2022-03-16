from tkinter import ttk



def create_table(root) -> ttk.Treeview:
    table = ttk.Treeview(root)
    style = ttk.Style(table)
    style.configure('Treeview', rowheight=45)
    font_size: int = 20
    style.configure("Treeview.Heading", font=(None, font_size))
    style.configure("Treeview", font=(None, font_size))
    # style.theme_use('clam')

    headings = set_media_table(table)
    table['show'] = 'headings'

    for column, heading in zip(table['columns'], headings):
        table.heading(column, text=heading)
        table.column(column, minwidth=0, width=100)

    table.place(relx=0.1, rely=0.15, relwidth=0.80, relheight=0.8)
    return table


def set_media_table(table) -> tuple:
    headings: tuple = ("Title", "Release Date")
    table['columns'] = ['Col1, Col2', 'Col3']
    return headings


def insert_media_table(table, list_of_media_classes):
    for x, media_details in enumerate(list_of_media_classes):
        table.insert(parent='', index='end', iid=x, text=x, values=[media_details.title, media_details.score])
