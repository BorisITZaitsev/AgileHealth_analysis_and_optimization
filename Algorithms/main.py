import tkinter as tk
from tkinter import messagebox
import os
import csv_reader
import diagramGenerator


class App:
    def __init__(self, root):
        self.root = root
        self.root.title('CSV and Diagram Processing')

        # Ввод пути к файлу данных
        self.data_file_label = tk.Label(root, text='Путь к файлу данных:')
        self.data_file_label.pack()
        self.data_file_entry = tk.Entry(root, width=50)
        self.data_file_entry.pack()

        # Ввод пути к файлу спринтов
        self.sprints_file_label = tk.Label(root, text='Путь к файлу спринтов:')
        self.sprints_file_label.pack()
        self.sprints_file_entry = tk.Entry(root, width=50)
        self.sprints_file_entry.pack()

        # Кнопка для обработки файлов
        self.process_button = tk.Button(root, text='Обработать файлы', command=self.process_files)
        self.process_button.pack()

        # Кнопка для выхода из программы
        self.exit_button = tk.Button(root, text='Выход и очистка', command=self.exit_program)
        self.exit_button.pack()

    def process_files(self):
        data_file_path = self.data_file_entry.get()
        sprints_file_path = self.sprints_file_entry.get()

        if os.path.exists(data_file_path) and os.path.exists(sprints_file_path):
            csv_reader.extract_event_statistics(data_file_path, sprints_file_path)
            self.create_diagram_windows()
        else:
            messagebox.showerror("Ошибка", "Проверьте, что пути к файлам существуют.")

    def create_diagram_windows(self):
        json_files = ['overload.json', 'uniform_of_distribution.json', 'canceled_database.json']
        if all(os.path.exists(file) for file in json_files):
            diagramGenerator.create_graph_windows(json_files)
        else:
            messagebox.showerror("Ошибка", "Некоторые JSON файлы отсутствуют.")

    def exit_program(self):
        json_files = ['canceled_database.json', 'overload.json', 'uniform_of_distribution.json']
        for file in json_files:
            try:
                os.remove(os.path.join(os.getcwd(), file))
            except FileNotFoundError:
                pass  # Если файл не найден, игнорируем это
        messagebox.showinfo("Успех", "Файлы очищены. Программа завершена.")
        self.root.quit()


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


'''import csv_reader
import diagramGenerator
import os


data_file_path = input()
sprints_file_path = input()
if os.path.exists(data_file_path) and os.path.exists(sprints_file_path):
    csv_reader.extract_event_statistics(data_file_path, sprints_file_path)
if os.path.exists("canceled_database.json") and os.path.exists("overload.json") and os.path.exists("uniform_of_distribution.json"):
    if __name__ == "__main__":
        json_files = ['overload.json', "uniform_of_distribution.json", "canceled_database.json"]
        diagramGenerator.create_graph_windows(json_files)
exit_controller = input("Введите 'EXIT' для выхода из программы и очистки памяти от системных файлов. -->  ")
while exit_controller != "EXIT":
    exit_controller = input()
os.remove(os.getcwd().replace('\\', "/") + "/" + "canceled_database.json")
os.remove(os.getcwd().replace('\\', "/") + "/" + "overload.json")
os.remove(os.getcwd().replace('\\', "/") + "/" + "uniform_of_distribution.json")'''






