import matplotlib.pyplot as plt
import pandas as pd

# Функция для чтения данных из внешнего файла
def read_data(file_path):
    df = pd.read_csv(file_path)  # Предполагаем, что данные в файле CSV
    return df

# Функция для построения точечного графика
def scatter_plot(x, y, label):
    plt.scatter(x, y, label=label)

# Основная функция программы
def main():
    file_path = input("Введите путь к файлу с данными: ")
    graph_count = int(input("Введите количество графиков для отображения: "))
    df = read_data(file_path)

    x_values = df['x']
    y_values = df['y']
    scatter_plot(x_values, y_values, label=f"График 1")

    for i in range(2, graph_count+1):
        x_values = df[f"x{i}"]
        y_values = df[f"y{i}"]
        scatter_plot(x_values, y_values, label=f"График {i-1}")

    # Настройки графика
    plt.title('Точечный график')
    plt.xlabel('Ось X')
    plt.ylabel('Ось Y')
    plt.legend()  # Добавляем легенду, если есть метки

    # Отображение графика
    plt.show()

if __name__ == "__main__":
    main()
