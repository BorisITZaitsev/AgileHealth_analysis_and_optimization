import tkinter as tk
import json
from datetime import datetime
from tkinter import messagebox

class NewWindow(tk.Toplevel):
    def __init__(self, root, data, title):
        super().__init__(root)
        self.title(title)

        # Создаем фрейм для колонтитула и бегунка
        frame = tk.Frame(self)
        frame.pack(fill=tk.BOTH, expand=True)

        # Колонтитул
        title_label = tk.Label(frame, text=self.get_title(title), font=("Arial", 16))
        title_label.pack()

        # Создаем канвас с горизонтальной прокруткой
        self.canvas = tk.Canvas(frame, width=1440, height=700)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Прокрутка
        scrollbar = tk.Scrollbar(frame, orient="horizontal", command=self.canvas.xview)
        scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
        self.canvas.configure(xscrollcommand=scrollbar.set)

        # Текстовое поле
        if self.get_title(title) == "Статистика отменённых задач":
            message = ("Этот график демонстрирует кол-во отменённых задач за каждый день спринта.\n"
                       "Красным выделены все дни, когда происходила отмена.")
        elif self.get_title(title) == "Статистика нагрузки":
            message = ("Этот график демонстрирует кол-во задач, обработанных сотрудниками за каждый день.\n"
                       "Красным выделены дни, когда такие кол-во задач привысило среднее значение.")
        elif self.get_title(title) == "Статистика распределения":
            message = "Этот график демонстрирует статистику отклонений от среднего объёма от обработанных задач."
        else:
            message = ""

        self.text_field = tk.Text(self, height=5, wrap=tk.WORD, font=("Arial", 10))
        self.text_field.insert(tk.END, message)
        self.text_field.pack(fill=tk.X, padx=10, pady=10)

        self.draw_chart(data)

    def get_title(self, filename):
        """Возвращает заголовок в зависимости от имени файла."""
        if 'canceled_database' in filename:
            return "Статистика отменённых задач"
        elif 'overload' in filename:
            return "Статистика нагрузки"
        elif 'uniform_of_distribution' in filename:
            return "Статистика распределения"
        return "Статистика"

    def draw_chart(self, data):
        self.canvas.delete("all")
        sorted_dates = sorted(data.keys())
        values = [data[date] for date in sorted_dates]

        max_value = max(values)
        middle_value = sum(values) / len(values)
        bar_width = 20
        spacing = 10
        x_start = 50

        for i, date in enumerate(sorted_dates):
            bar_height = (values[i] / max_value) * 300
            x_position = x_start + i * (bar_width + spacing)
            y_position = 350 - bar_height

            color = "red" if values[i] >= middle_value else "skyblue"
            self.canvas.create_rectangle(x_position, y_position, x_position + bar_width, 350, fill=color)
            self.canvas.create_text((x_position + bar_width / 2) - 7, 400, text=date.strftime('%Y-%m-%d'), angle=90, anchor='n')
            self.canvas.create_text(x_position + bar_width / 2, y_position - 10, text=str(values[i]), anchor='s')

        self.canvas.config(scrollregion=self.canvas.bbox("all"))  # Устанавливаем область прокрутки

def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

def convert_dates(data):
    converted_data = {}
    previous_date = datetime.strptime("2000-01-01", "%Y-%m-%d")
    for date_str, value in data.items():
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')  # Преобразование строки в объект datetime
            converted_data[date_obj] = value
            previous_date = date_obj
        except ValueError:
            converted_data[previous_date] = value

    return converted_data

def create_graph_windows(json_files):
    root = tk.Tk()
    root.withdraw()

    for json_file in json_files:
        data = load_data_from_json(json_file)
        converted_data = convert_dates(data)
        NewWindow(root, converted_data, json_file)

    root.mainloop()

# Пример вызова функции из другого файла
'''if __name__ == "__main__":
    json_files = ['overload.json', "uniform_of_distribution.json", "canceled_database.json"]
    create_graph_windows(json_files)'''

'''import tkinter as tk
import json
from datetime import datetime

class NewWindow(tk.Toplevel):
    def __init__(self, root, data, title):
        super().__init__(root)
        self.title(title)
        self.canvas = tk.Canvas(self, width=1440, height=800)
        self.canvas.pack()
        self.draw_chart(data)

    def draw_chart(self, data):
        self.canvas.delete("all")
        sorted_dates = sorted(data.keys())
        values = [data[date] for date in sorted_dates]

        max_value = max(values)
        middle_value = sum(values) / len(values)
        bar_width = 20
        spacing = 10
        x_start = 50

        for i, date in enumerate(sorted_dates):
            bar_height = (values[i] / max_value) * 300
            x_position = x_start + i * (bar_width + spacing)
            y_position = 350 - bar_height


            if values[i] >= middle_value:
                color = "red"
            else:
                color = "skyblue"
            self.canvas.create_rectangle(x_position, y_position, x_position + bar_width, 350, fill=color)
            self.canvas.create_text((x_position + bar_width / 2) - 7, 400, text=date.strftime('%Y-%m-%d'), angle=90,
                                    anchor='n')
            self.canvas.create_text(x_position + bar_width / 2, y_position - 10, text=str(values[i]), anchor='s')


def load_data_from_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def convert_dates(data):
    converted_data = {}
    previous_date = datetime.strptime("2000-01-01", "%Y-%m-%d")
    for date_str, value in data.items():
        try:
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')  # Преобразование строки в объект datetime
            converted_data[date_obj] = value
            previous_date = date_obj
        except ValueError:
            converted_data[previous_date] = value

    return converted_data


def create_graph_windows(json_files):
    root = tk.Tk()
    root.withdraw()

    for json_file in json_files:
        data = load_data_from_json(json_file)
        converted_data = convert_dates(data)
        NewWindow(root, converted_data, json_file)

    root.mainloop()'''

# Пример вызова функции из другого файла
'''if __name__ == "__main__":
    json_files = ['overload.json', "uniform_of_distribution.json", "canceled_database.json"]
    create_graph_windows(json_files)'''



