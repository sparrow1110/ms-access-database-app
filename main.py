import tkinter
import customtkinter as ctk
from tkinter import ttk
import tkinter.messagebox as messagebox
import pyodbc

# Импортирую классы: DataBase - класс для взаимодействия с БД, Abstract_Ex - абстрактный класс содержащий метод для отображения таблиц,
# Interfeis_Ex - интерфейсный класс содержащий методы для добавления, изменения, удаления записей, а так же метод для отображения записей по заданному запросу.
from Connect_DB import DataBase

from OOP_abstract_interfies import Abstract_Ex, Interfeis_Ex

# Реальный класс наследник, который отвечает за приложение, он наследуется от: ctk.CTk - класс, методы которого позволяют выстраивать интерфейс приложения,
# Abstract_Ex - абстрактный класс, Interfeis_Ex - интерфейсный класс.
class App(ctk.CTk, Abstract_Ex, Interfeis_Ex):

    # В конструкторе класса создаются и определяются поля объекта класса.
    def __init__(self):
        # Вызывается конструктор класса-родителя, а именно: ctk.CTk.
        super().__init__()

        # Создание поля класса, которое будет являться объектом класса DataBase, для взаимодействия через него с БД.
        self.conn = DataBase()

        self.geometry("960x650")
        self.title("Информационная система соревнований")
        self.resizable(False, False)

        self.appearanse_mode = ctk.set_appearance_mode("light")
        self.default_color_theme = ctk.set_default_color_theme("green")

        # Пустой лейбл для отступа между верхней границей приложения и кнопками, которые будут ниже.
        self.label = ctk.CTkLabel(master=self, text="")

        # Размещение лейбла на окне приложения.
        self.label.grid(row=0, column=0)

        # Фрейм, на котором в дальнейшем будут размещаться другие элементы.
        self.top_menu_frame = ctk.CTkFrame(master=self, fg_color="transparent")
        self.top_menu_frame.grid(row=1, column=0, padx=(30, 30), sticky="nsew")

        # Пустой лейбл для получения отступа от верхней границы фрейма.
        self.labelTopMenu = ctk.CTkLabel(master=self.top_menu_frame, text="")
        self.labelTopMenu.grid(row=0, column=0)

        # Кнопки для переключения между таблицами.
        self.btn_sports = ctk.CTkButton(master=self.top_menu_frame, text="Виды спорта", width=150,
                                       command=self.show_sports)
        self.btn_sports.grid(row=1, column=0, padx=(0, 20))

        self.btn_teams = ctk.CTkButton(master=self.top_menu_frame, text="Команды", width=150,
                                         command=self.show_teams)
        self.btn_teams.grid(row=1, column=1, padx=(0, 20))

        self.btn_results = ctk.CTkButton(master=self.top_menu_frame, text="Результаты", width=150,
                                          command=self.show_results)
        self.btn_results.grid(row=1, column=2, padx=(0, 20))

        self.btn_competitions = ctk.CTkButton(master=self.top_menu_frame, text="Соревнования", width=150,
                                         command=self.show_competitions)
        self.btn_competitions.grid(row=1, column=3, padx=(0, 20))

        self.btn_sportsman = ctk.CTkButton(master=self.top_menu_frame, text="Спортсмены", width=150,
                                           command=self.show_sprotsmans)
        self.btn_sportsman.grid(row=1, column=4, padx=(0, 20))

        # Пустой лейбл для отступа между первым и вторым рядом кнопок.
        self.label_spacer = ctk.CTkLabel(master=self.top_menu_frame, text="")
        self.label_spacer.grid(row=2, column=0, columnspan=5)

        self.btn_stadiums = ctk.CTkButton(master=self.top_menu_frame, text="Стадионы", width=150,
                                         command=self.show_stadiums)
        self.btn_stadiums.grid(row=3, column=0, padx=(0, 20))

        self.btn_participations = ctk.CTkButton(master=self.top_menu_frame, text="Участие", width=150,
                                         command=self.show_participations)
        self.btn_participations.grid(row=3, column=1, padx=(0, 20))

        self.label.grid(row=2, column=0)

        # Фрейм, который будет содержать в себе таблицу.
        self.table_frame = ctk.CTkFrame(master=self, height=400, fg_color="transparent")
        self.table_frame.grid(row=3, column=0, padx=(10, 10))

        # Пустой лейбл для создания границы.
        self.label_border = ctk.CTkLabel(master=self, text="", height=50)
        self.label_border.grid(row=4, column=0)

        # Фрейм, который будет содержать в себе нижнее меню с кнопками добавления, изменения, удаления и запроса.
        self.frame_bottom_menu = ctk.CTkFrame(master=self, fg_color="transparent")
        self.frame_bottom_menu.grid(row=5, column=0, padx=(30, 30), sticky="nsew")

        self.btn_add = ctk.CTkButton(master=self.frame_bottom_menu, text="Добавить", width=150,
                                     command=self.add)
        self.btn_add.grid(row=1, column=0, padx=(0, 20))

        self.btn_edit = ctk.CTkButton(master=self.frame_bottom_menu, text="Изменить", width=150,
                                      command=self.edit)
        self.btn_edit.grid(row=1, column=1, padx=(0, 20))

        self.btn_delete = ctk.CTkButton(master=self.frame_bottom_menu, text="Удалить", width=150,
                                        command=self.delete)
        self.btn_delete.grid(row=1, column=2, padx=(0, 20))

        self.btn_saved_queries = ctk.CTkButton(master=self.frame_bottom_menu, text="Запросы", width=150,
                                               command=self.show_saved_queries)
        self.btn_saved_queries.grid(row=1, column=3, padx=(0, 20))

        self.frame_bottom_end = ctk.CTkFrame(master=self, fg_color="transparent")
        self.frame_bottom_end.grid(row=6, column=0, padx=(0, 30), sticky="nsew")

        self.bottom_label = ctk.CTkLabel(master=self.frame_bottom_end, text="", height=50)
        self.bottom_label.grid(row=1, column=0, padx=(0, 20))

        # Словарь, в котором ключом является первичный ключ таблицы, а значением - имя таблицы.
        self.tuple = {'Идентификатор вида спорта': "Вид спорта", 'Идентификатор команды': "Команда", ('Номер спортсмена', 'Номер попытки'): "Результат",
                      'Идентификатор соревнования': "Соревнование", 'Номер спортсмена' : "Спортсмен", 'Идентификатор стадиона': "Стадион",
                      ('Идентификатор соревнования','Номер спортсмена') : "Результат"}

        # Словарь, где ключ - имя таблицы, значение - массив содержащий имена всех столбцов.
        self.tuple_title = {
            "Вид_спорта": ['Идентификатор вида спорта', 'Название вида спорта'],
            "Команда": ['Идентификатор команды', 'Название команды', 'Город', 'Количество игроков', 'Тренер'],
            "Результат": ['Номер спортсмена', 'Номер попытки', 'Результат попытки', 'Дата выступления'],
            "Соревнование": ['Идентификатор соревнования', 'Дата начала', 'Дата окончания', 'Идентификатор вида спорта',
                             'Идентификатор стадиона'],
            "Спортсмен" : ['Номер спортсмена', 'Фамилия', 'Имя', 'Отчество', 'Идентификатор команды'],
            "Стадион" : ['Идентификатор стадиона', 'Название', 'Адрес', 'Вместимость'],
            "Участие" : ['Идентификатор соревнования', 'Номер спортсмена']}
        self.list_entry = []

        self.current_table = "Вид_спорта"
        self.show_sports()

    # Методы для отображения определенной таблицы.
    def show_sports(self):
        headers = ['Идентификатор вида спорта', 'Название вида спорта']
        self.show_table("Вид_спорта", headers)

    def show_teams(self):
        headers = ['Идентификатор команды', 'Название команды', 'Город', 'Количество игроков', 'Тренер']
        self.show_table("Команда", headers)

    def show_results(self):
        headers = ['Номер спортсмена', 'Номер попытки', 'Результат попытки', 'Дата выступления']
        self.show_table("Результат", headers)

    def show_competitions(self):
        headers = ['Идентификатор соревнования', 'Дата начала', 'Дата окончания', 'Идентификатор вида спорта', 'Идентификатор стадиона']
        self.show_table("Соревнование", headers)

    def show_sprotsmans(self):
        headers = ['Номер спортсмена', 'Фамилия', 'Имя', 'Отчество', 'Идентификатор команды']
        self.show_table('Спортсмен', headers)

    def show_stadiums(self):
        headers = ['Идентификатор стадиона', 'Название', 'Адрес', 'Вместимость']
        self.show_table('Стадион', headers)

    def show_participations(self):
        headers = ['Идентификатор соревнования', 'Номер спортсмена']
        self.show_table('Участие', headers)

    # Этот метод вызывает реализацию из абстрактного класса Abstract_Ex.
    def show_table(self, nameTable, headers):
        self.current_table = nameTable
        return super().show_table(nameTable, headers)

    # Этот метод создает реализацию для метода add из интерфейского класса Interfeis_Ex (добавление записи).
    def add(self):
        # Новое окно поверх основного.
        add_window = ctk.CTkToplevel(self)
        add_window.title("Добавление записи")
        add_window.geometry("400x500")
        add_window.resizable(False, False)

        # Центрирую окно относительно главного окна.
        add_window.transient(self)
        x = self.winfo_x() + (self.winfo_width() // 2) - (400 // 2)
        y = self.winfo_y() + (self.winfo_height() // 2) - (500 // 2)
        add_window.geometry(f"+{x}+{y}")

        # Фрейм для элементов формы.
        form_frame = ctk.CTkFrame(master=add_window, fg_color="transparent")
        form_frame.pack(padx=20, pady=20)

        self.list_entry.clear()

        # Добавление полей ввода.
        for indx in self.tuple_title[self.current_table]:
            label_add = ctk.CTkLabel(master=form_frame, text=indx, width=150)
            label_add.pack(pady=(10, 0))
            entry_add = ctk.CTkEntry(master=form_frame, width=200)
            entry_add.pack(pady=(0, 10))
            self.list_entry.append(entry_add)

        button_frame = ctk.CTkFrame(master=form_frame, fg_color="transparent")
        button_frame.pack(pady=20)

        btn_close = ctk.CTkButton(master=button_frame, text="Закрыть", width=150,
                                  command=add_window.destroy)
        btn_close.pack(side="left", padx=10)

        btn_add = ctk.CTkButton(master=button_frame, text="Добавить", width=150,
                                command=lambda: self.get_entry(add_window))
        btn_add.pack(side="left", padx=10)

    # Этот метод считывает введённые данные в форме добавления и отправляет запрос на добавление данных в таблицу.
    def get_entry(self, window):
        try:
            stringTitle = ""
            data = []
            for i in self.list_entry:
                data.append(i.get())

                stringTitle += f"{self.tuple_title[self.current_table][self.list_entry.index(i)].replace(' ', '_')}, "
            stringTitle += " "
            stringTitle = stringTitle.replace(",  ", "")

            self.conn.insert(self.current_table, stringTitle, tuple(data))

            self.show_repit(self.current_table)
            window.destroy()
            messagebox.showinfo("Информация", "Успешно добавлено!")
        except pyodbc.DataError:
            messagebox.showerror("Ошибка", "Неправильный тип данных!")
        except pyodbc.IntegrityError as e:
            if e.args[1].find('-1613') != -1:
                messagebox.showerror("Ошибка","Введен идентификатор несуществующего объекта")
            elif e.args[1].find('-1605') != -1:
                messagebox.showerror("Ошибка", "Запись с указанным идентификатором уже существует")

    # Данный метод заново отрисовывает таблицы со всеми изменениями.
    def show_repit(self, title):
        if title == "Вид_спорта":
            self.show_sports()
        elif title == "Результат":
            self.show_results()
        elif title == "Команда":
            self.show_teams()
        elif title == "Стадион":
            self.show_stadiums()
        elif title == "Спортсмен":
            self.show_sprotsmans()
        elif title == "Участие":
            self.show_participations()
        elif title == "Соревнование":
            self.show_competitions()

    # Этот метод создает реализацию для метода edit  из интерфейского класса Interfeis_Ex (изменение выбранной записи).
    def edit(self):
        try:
            # Проверка, выбрана ли строка.
            selected_item = self.table.focus()
            if not selected_item:
                messagebox.showwarning("Предупреждение", "Выберите строку для изменения")
                return

            edit_window = ctk.CTkToplevel(self)
            edit_window.title("Изменение записи")
            edit_window.geometry("400x500")
            edit_window.resizable(False, False)

            edit_window.transient(self)
            x = self.winfo_x() + (self.winfo_width() // 2) - (400 // 2)
            y = self.winfo_y() + (self.winfo_height() // 2) - (500 // 2)
            edit_window.geometry(f"+{x}+{y}")

            form_frame = ctk.CTkFrame(master=edit_window, fg_color="transparent")
            form_frame.pack(padx=20, pady=20)

            self.list_entry.clear()

            # Добавляем поля с текущими значениями.
            for indx in self.tuple_title[self.current_table]:
                label_edit = ctk.CTkLabel(master=form_frame, text=indx, width=150)
                label_edit.pack(pady=(10, 0))
                entry_edit = ctk.CTkEntry(master=form_frame, width=200)
                entry_edit.insert(0, self.table.item(selected_item)['values'][
                    self.tuple_title[self.current_table].index(indx)])
                entry_edit.pack(pady=(0, 10))
                self.list_entry.append(entry_edit)

            button_frame = ctk.CTkFrame(master=form_frame, fg_color="transparent")
            button_frame.pack(pady=20)

            btn_close = ctk.CTkButton(master=button_frame, text="Закрыть", width=150,
                                      command=edit_window.destroy)
            btn_close.pack(side="left", padx=10)

            btn_edit = ctk.CTkButton(master=button_frame, text="Изменить", width=150,
                                     command=lambda: self.get_edit(edit_window))
            btn_edit.pack(side="left", padx=10)

        except pyodbc.Error:
            messagebox.showwarning("Предупреждение", "Строка не может быть изменена")

    # Данный метод считывает данные из формочки и отправляет запросы на изменение выбранных данных в таблице.
    def get_edit(self, window):
        try:
            string_ti_val = ""
            values = []
            if self.current_table == "Результат" or self.current_table == "Участие":
                for i in self.tuple_title[self.current_table]:
                    string_ti_val += f'{i.replace(" ", "_")}=?, '
                    values.append(self.list_entry[self.tuple_title[self.current_table].index(i)].get())
                string_ti_val += " "
                string_ti_val = string_ti_val.replace(",  ", "")
                c_update = f'{self.tuple_title[self.current_table][0].replace(" ", "_")}=? and {self.tuple_title[self.current_table][1].replace(" ", "_")}=?'
                values.append(self.table.item(self.table.focus())["values"][0])
                values.append(self.table.item(self.table.focus())["values"][1])
            else:
                for i in self.tuple_title[self.current_table][1:]:
                    string_ti_val += f'{i.replace(" ", "_")}=?, '
                    values.append(self.list_entry[self.tuple_title[self.current_table].index(i)].get())
                string_ti_val += " "
                string_ti_val = string_ti_val.replace(",  ", "")
                c_update = f'{self.tuple_title[self.current_table][0].replace(" ", "_")}=?'
                values.append(self.table.item(self.table.focus())["values"][0])

            self.conn.update(self.current_table, string_ti_val, c_update, values)

            self.show_repit(self.current_table)
            window.destroy()
            messagebox.showinfo("Информация", "Успешно изменено!")
        except pyodbc.DataError:
            messagebox.showerror("Ошибка", "Неправильный тип данных!")
        except pyodbc.IntegrityError as e:
            if e.args[1].find('-1613') != -1:
                messagebox.showerror("Ошибка","Введен идентификатор несуществующего объекта")
            elif e.args[1].find('-1605') != -1:
                messagebox.showerror("Ошибка", "Запись с указанным идентификатором уже существует")

    # Этот метод создает реализацию для метода delete из интерфейского класса Interfeis_Ex (удаление выбранной строки).
    def delete(self):
        try:

            c_delete = f'{self.tuple_title[self.current_table][0].replace(" ", "_")}=?'
            value = self.table.item(self.table.focus())["values"][0]
            self.conn.delete(self.current_table, c_delete, value)

            self.list_entry.clear()
            self.show_repit(self.current_table)
            messagebox.showinfo("Информация", "Успешно удалено!")
        except pyodbc.Error:
            messagebox.showwarning("Предупреждение", "Строка не может быть удалена")
        except IndexError:
            messagebox.showwarning("Предупреждение", "Выберите строку для удаления")

    # Этот метод создает реализацию для метода из интерфейского класса Interfeis_Ex (выполнение пользовательских запросов).
    def show_saved_queries(self):
        query_window = ctk.CTkToplevel(self)
        query_window.title("Сохраненные запросы")
        query_window.geometry("400x500")
        query_window.resizable(False, False)

        query_window.transient(self)
        x = self.winfo_x() + (self.winfo_width() // 2) - (400 // 2)
        y = self.winfo_y() + (self.winfo_height() // 2) - (500 // 2)
        query_window.geometry(f"+{x}+{y}")

        # Создание основного фрейма.
        main_frame = ctk.CTkFrame(master=query_window, fg_color="transparent")
        main_frame.pack(padx=20, pady=20, fill="both", expand=True)

        # Получение списка сохраненных запросов.
        queries = self.conn.get_queries()
        query_names = [query[0] for query in queries]

        # Добавление комбобокса.
        self.combox = ctk.CTkComboBox(master=main_frame, values=query_names, width=320)
        self.combox['state'] = "readonly"
        self.combox.pack(pady=5)

        # Добавление текстового поля.
        self.textBox = ctk.CTkTextbox(master=main_frame, width=320, wrap=None)
        self.textBox.pack(pady=5, fill="both", expand=True)

        button_frame = ctk.CTkFrame(master=main_frame, fg_color="transparent")
        button_frame.pack(pady=5)

        btn_close = ctk.CTkButton(master=button_frame, text="Закрыть", width=150,
                                  command=query_window.destroy)
        btn_close.pack(side="left", padx=5)

        btn_execute = ctk.CTkButton(master=button_frame, text="Выполнить", width=150,
                                    command=lambda: self.execute_saved_query(query_window))
        btn_execute.pack(side="left", padx=5)

    # Выполнение выбранного запроса.
    def execute_saved_query(self, window):
        try:
            query_name = self.combox.get()
            if not query_name:
                messagebox.showinfo("Ошибка!", "Выберите запрос для выполнения!")
                return

            if query_name == "Команды из определенного города" or query_name == "Соревнования по определенному виду спорта" or query_name == "Соревнования, проводимые на определенном стадионе":
                data = self.textBox.get("1.0", "end-1c")
                if data == "":
                    messagebox.showerror("Ошибка!", "Заполните поле!")
                    return 0
                else:
                    result = self.conn.execute_query(query_name, data)
            else:
                result = self.conn.execute_query(query_name)

            self.table_frame.grid_forget()
            self.table_frame = ctk.CTkFrame(master=self, height=400, fg_color="transparent")
            self.table_frame.grid(row=3, column=0, padx=(10, 10))

            self.table = ttk.Treeview(master=self.table_frame, height=20, show='headings')
            self.table.pack(expand=tkinter.YES, fill=tkinter.BOTH)

            # Определение заголовков столбцов.
            headers = [desc[0] for desc in result[0].cursor_description]
            self.table['columns'] = headers

            for header in headers:
                self.table.heading(header, text=header, anchor='center')
                self.table.column(header, width=int((1000 - 20) / len(headers)), anchor=tkinter.CENTER)

            for row in result:
                cleaned_values = [str(value).strip("(),'") for value in row]
                self.table.insert('', tkinter.END, values=cleaned_values)

            for i in self.table.get_children():
                self.table.tag_configure(i, background="black")

            window.destroy()
            self.table.pack(expand=tkinter.YES, fill=tkinter.BOTH)
            messagebox.showinfo("Успех", "Запрос выполнен!")
        except IndexError:
            window.destroy()
            messagebox.showinfo("Информация", "По вашему запросу ничего не найдено")
            self.show_repit(self.current_table)


# Запуск только когда запускается именно текущий файл.
if __name__ == '__main__':
    # Создание экземпляра реального класса App.
    app = App()
    # Данный метод находится в классе ctk.CTK и отвечает за запуск приложения.
    app.mainloop()
    app.conn.connect.close()


