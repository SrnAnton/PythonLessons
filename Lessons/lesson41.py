import time
from multiprocessing import Pool


def read_info(filename):
    with open(filename, 'r') as file:
        all_data = []
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)
    return all_data


def main():
    filenames = [f'Files/file {i}.txt' for i in range(1, 5)]

    # Линейный вызов
    start_time = time.perf_counter()
    for filename in filenames:
        read_info(filename)
    linear_time = time.perf_counter() - start_time
    print(f"0:00:{linear_time:.3f} (линейный)")

    # Многопроцессный вызов
    start_time = time.perf_counter()
    with Pool() as pool:
        pool.map(read_info, filenames)
    multiprocess_time = time.perf_counter() - start_time
    print(f"0:00:{multiprocess_time:.3f} (многопроцессный)")


if __name__ == '__main__':
    main()
