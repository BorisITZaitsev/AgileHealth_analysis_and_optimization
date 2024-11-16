import pandas as pd


# Шаг 1: Загрузка данных
def load_data(file_path):
    with open(file_path, encoding="utf-8") as csvfile:
        raw_data = csvfile.readlines()[1:]
        event_database = {}

    event_dates = []

    for row in raw_data[2:]:
        row_data = row.split(";")
        event_database[row_data[0]] = (row_data[0], row_data[2], row_data[3], row_data[6],
                                        row_data[8], row_data[10], row_data[-3], row_data[-1])
    print(event_database)
    return event_database


# Шаг 2: Анализ данных
def analyze_data(data):
    # Преобразуем даты в формат datetime
    data['start_date'] = pd.to_datetime(data['start_date'])
    data['end_date'] = pd.to_datetime(data['end_date'])

    # Подсчет общего объема задач
    total_tasks = len(data)

    # Подсчет статусов
    status_counts = data['status'].value_counts()

    # Проверка на равномерность переходов статусов
    transition_counts = {
        'to_in_progress': ((data['status'] == 'К выполнению') & (data['next_status'] == 'В работе')).sum(),
        'to_done': ((data['status'] == 'В работе') & (data['next_status'] == 'Сделано')).sum()
    }

    # Проверка на массовый переход в статус "Сделано" в последний день спринта
    last_day = data['end_date'].max()
    mass_done_transition = data[(data['status'] == 'Сделано') & (data['end_date'] == last_day)].shape[0]

    # Проверка на процент "К выполнению"
    todo_percentage = (status_counts.get('К выполнению', 0) / total_tasks) * 100

    # Проверка на процент "Снято"
    removed_percentage = (status_counts.get('Снято', 0) / total_tasks) * 100

    # Проверка на изменение бэклога
    backlog_start = data['backlog_start'].sum()  # Предполагается, что есть колонка с начальным бэклогом
    backlog_end = data['backlog_end'].sum()  # Предполагается, что есть колонка с конечным бэклогом
    backlog_change_percentage = abs((backlog_end - backlog_start) / backlog_start) * 100

    # Сбор результатов анализа
    results = {
        'total_tasks': total_tasks,
        'status_counts': status_counts.to_dict(),
        'transition_counts': transition_counts,
        'mass_done_transition': mass_done_transition,
        'todo_percentage': todo_percentage,
        'removed_percentage': removed_percentage,
        'backlog_change_percentage': backlog_change_percentage
    }

    return results


# Шаг 3: Вывод результатов анализа
def print_analysis_results(results):
    print("Общий объем задач:", results['total_tasks'])
    print("Количество задач по статусам:", results['status_counts'])
    print("Переходы статусов:", results['transition_counts'])
    print("Массовый переход в статус 'Сделано' в последний день спринта:", results['mass_done_transition'])
    print("Процент 'К выполнению': {:.2f}%".format(results['todo_percentage']))
    print("Процент 'Снято': {:.2f}%".format(results['removed_percentage']))
    print("Изменение бэклога: {:.2f}%".format(results['backlog_change_percentage']))


# Основная функция
def main():
    file_path = 'data_for_spb_hakaton_entities1-Table 1.csv'  # Путь к файлу с данными
    data = load_data(file_path)
    results = analyze_data(data)
    print_analysis_results(results)


if __name__ == "__main__":
    main()
