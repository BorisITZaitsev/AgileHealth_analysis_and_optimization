import json

def extract_event_statistics(csv_data_path, csv_sprints_path):
    # Функция для формирования данных по количеству событий за день
    def calculate_event_count(data, days):
        daily_event_count = {}
        for day in days:
            daily_event_count[day] = 0
        for event in data:
            event_date = data[event][4][:10]
            daily_event_count[event_date] += 1
        return daily_event_count

    # Функция для формирования данных по отклонению от среднего количества событий за день
    def calculate_uniformity(data, days):
        daily_event_count = calculate_event_count(data, days)
        average_events_per_day = len(data) / len(daily_event_count)
        for day in daily_event_count:
            daily_event_count[day] = abs(daily_event_count[day] - average_events_per_day)
        return daily_event_count

    # Функция для подсчета отмененных событий за день
    def calculate_canceled_events(data, days):
        daily_canceled_count = {}
        for day in days:
            daily_canceled_count[day] = 0
        for event in data:
            event_details = data[event]
            if (event_details[1] == "Дефект" and event_details[2] == "Отклонено исполнителем") or \
               (event_details[2] == "Закрыто" and event_details[-1] != "Готово\n") or \
               (event_details[-1] in ("Отклонено\n", "Отменено инициатором\n", "Дубликат\n")):
                event_date = event_details[4][:10]
                daily_canceled_count[event_date] += 1
        return daily_canceled_count

    with open(csv_data_path, encoding="utf-8") as csvfile:
        raw_data = csvfile.readlines()[1:]
        categories = raw_data[0].split(";")
        event_database = {}

    with open(csv_sprints_path, encoding="utf-8") as csvfile2:
        sprint_ids = csvfile2.readline()[1:-2].split(",")

    event_dates = []

    for row in raw_data[2:]:
        row_data = row.split(";")
        if row_data[0] not in sprint_ids:
            continue
        event_date = row_data[8][:10]
        if event_date not in event_dates:
            event_dates.append(event_date)
        event_database[row_data[0]] = (row_data[0], row_data[2], row_data[3], row_data[6],
                                        row_data[8], row_data[10], row_data[-3], row_data[-1])

    with open("canceled_database.json", "w") as cancel_file:
        json.dump(calculate_canceled_events(event_database, event_dates), cancel_file)

    with open("uniform_of_distribution.json", "w") as uniform_file:
        json.dump(calculate_uniformity(event_database, event_dates), uniform_file)

    with open("overload.json", "w") as overload_file:
        json.dump(calculate_event_count(event_database, event_dates), overload_file)

# Вызов функции (пример):
# extract_event_statistics('data_for_spb_hakaton_entities1-Table 1.csv', 'sprints-Table 1.csv')

'''import json


#функция ниже получает на вход словарь {номер события: описание с датой}, а также даты,
#в которые происходили какие-либо события. Она возвращает данные для формирования линейного графика
#который иллюстрирует количество событий, произошедших за один день.
def overload(data, days):
    Days = {}
    for i in days:
        Days[i] = 0
    for i in data:
        Days[data[i][4][:10]] += 1
    return Days


#функция ниже получает на вход аналогичные предыдущей функции даты. Она также формирует данные для графика,
#но теперь, основываясь на отклонении количества событий за каждый день от общего среднего количества событий в день
def uniform(data, days):
    Days = {}
    for i in days:
        Days[i] = 0
    for i in data:
        Days[data[i][4][:10]] += 1
    sr_ar = len(data) / len(Days)
    for i in Days:
        Days[i] = abs(Days[i] - sr_ar)
    return Days


#функция ниже получает на вход аналогичные предыдущей функции даты. Она также формирует данные для графика,
#но теперь, исходя из количества событий отмены за каждый день. (отмена определяется в условии if)
def canceled(data, days):
    Days = {}
    for i in days:
        Days[i] = 0
    for i in data:
        event = data[i]
        if (event[1] == "Дефект" and event[2] == "Отклонено исполнителем") or (event[2] == "Закрыто" and event[-1] != "Готово\n") or (event[-1] in ("Отклонено\n", "Отменено инициатором\n", "Дубликат\n")):
            Days[data[i][4][:10]] += 1
    return Days



with open('data_for_spb_hakaton_entities1-Table 1.csv', encoding="utf-8") as csvfile:
    data = csvfile.readlines()[1:]
    categories = data[0].split(";")
    database = {}

with open("sprints-Table 1.csv", encoding="utf-8") as csvfile2:
    id_s = csvfile2.readline()[1:-2].split(",")

days = []


for i in data[2:]:
    i = i.split(";")
    if i[0] not in id_s:
        continue
    if i[8][:10] not in days:
        days.append(i[8][:10])
    database[i[0]] = (i[0], i[2], i[3], i[6], i[8], i[10], i[-3], i[-1])


with open("canceled_database.json", "w") as cancels:
        json.dump(canceled(database, days), cancels)

with open("uniform_of_distribution.json", "w") as unif:
    json.dump(uniform(database, days), unif)

    with open("overload.json", "w") as overloads:
        json.dump(overload(database, days), overloads)'''