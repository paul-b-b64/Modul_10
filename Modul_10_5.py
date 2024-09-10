import datetime
import multiprocessing

# 0:00:03.758891 (линейный)
# 0:00:01.742263 (многопроцессный)


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)

filenames = [f'./Files/file {number}.txt' for number in range(1, 5)]

# # Линейный вызов
# start = datetime.datetime.now()
# for name in filenames:
#     read_info(name)
# end = datetime.datetime.now()
# print(end - start)

# Многопроцессный
if __name__ == '__main__':
    start = datetime.datetime.now()
    with multiprocessing.Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end = datetime.datetime.now()
    print(end - start)

