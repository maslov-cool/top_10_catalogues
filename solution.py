import os


def human_read_format(size):
    sizes = ['Б', 'КБ', 'МБ', 'ГБ']
    n = size
    i = 0
    while n // 1024:
        i += 1
        n //= 1024
    return str(round(size / 1024 ** i)) + sizes[i]


def top_10_catalogues(path):
    A = []
    for i in os.listdir(path):
        if os.path.isdir(os.path.join(path, i)):
            A.append([i, os.path.getsize(os.path.join(path, i))])
    for i in sorted(A, key=lambda x: x[1], reverse=True)[:10]:
        print(f"{i[0]:<20}  {human_read_format(i[1]):<20}")


top_10_catalogues(input('введите полный путь нужного каталога'))
