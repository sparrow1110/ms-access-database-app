from abc import ABC, abstractmethod

import tkinter
from tkinter import ttk
import customtkinter as ctk

# Абстрактный класс, содержащий в себе один абстрактный метод, который отвечает за отображение таблиц с данными.
class Abstract_Ex(ABC):
    @abstractmethod
    def show_table(self, nameTable, headers):
        self.table_frame.grid_forget()
        self.table_frame = ctk.CTkFrame(master=self, height=400, fg_color="transparent")
        self.table_frame.grid(row=3, column=0, padx=(10, 10))

        self.table = ttk.Treeview(master=self.table_frame, height=20, show='headings')
        self.table['columns'] = tuple(headers)

        for header in headers:
            self.table.heading(header, text=header, anchor='center')
            self.table.column(header, width=int((1000 - 20) / len(headers)), anchor=tkinter.CENTER)

        list_values = self.conn.select(columns="*", nameTable=nameTable, condition_select=" ")

        for row in list_values:
            cleaned_values = [str(value).strip("(),'") for value in row]
            self.table.insert('', tkinter.END, values=cleaned_values)

        for i in self.table.get_children():
            self.table.tag_configure(i, background="black")
        self.table.pack(expand=tkinter.YES, fill=tkinter.BOTH)

# Интерфейсный класс, содержит в себе 3 определенных и не реализованных метода, реализованы они будут в его наследниках.
class Interfeis_Ex(ABC):

    # Будет отвечать за добавление новых данных в таблицы.
    @abstractmethod
    def add(self):
        pass

    # Будет отвечать за изменение данных в таблицах.
    @abstractmethod
    def edit(self):
        pass

    # Будет отвечать за удаление данных из таблиц.
    @abstractmethod
    def delete(self):
        pass

    # Будет отвечать за выборку данных из таблиц.
    @abstractmethod
    def show_saved_queries(self):
        pass
