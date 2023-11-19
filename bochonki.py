import random
import logging

# Настройка логгирования
logging.basicConfig(filename='lottery.log', level=logging.INFO, format='%(asctime)s %(message)s')


def init_barrels(n):
    """
    Функция для инициализации мешка с бочонками.
    Возвращает список бочонков от 1 до n.
    """
    return list(range(1, n + 1))


def shuffle_barrels(barrels):
    """
    Функция для перемешивания бочонков в мешке.
    """
    random.shuffle(barrels)


def draw_barrel(barrels):
    """
    Функция для вытаскивания бочонка из мешка.
    Возвращает вытащенный бочонок и обновленный список бочонков.
    """
    if barrels:
        barrel = barrels.pop()
        logging.info(f'Drawing barrel: {barrel}')
        return barrel, barrels
    else:
        logging.info('No more barrels to draw.')
        return None, barrels


def main():
    try:
        # Диалог с пользователем для ввода числа N
        n = int(input("Введите натуральное число N (количество бочонков): "))
        if n <= 0:
            raise ValueError

        # Инициализация мешка с бочонками
        barrels = init_barrels(n)
        shuffle_barrels(barrels)
        logging.info(f'Barrels initialized and shuffled: {barrels}')

        # Игровой процесс - вытаскивание бочонков по нажатию клавиши
        input("Нажмите Enter, чтобы вытянуть бочонок...")
        while barrels:
            barrel, barrels = draw_barrel(barrels)
            if barrel is not None:
                print(f"Вытащен бочонок: {barrel}")
            else:
                print("Бочонки закончились.")
                break
            input("Нажмите Enter, чтобы вытянуть следующий бочонок...")

        print("Игра окончена.")

    except ValueError:
        print("Ошибка: Нужно ввести положительное целое число.")


if __name__ == "__main__":
    main()