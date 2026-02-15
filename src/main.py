from src.storage import category_storage, note_storage


def create_sample_data():
    """Создает тестовые данные."""
    work = category_storage.create('Работа')
    personal = category_storage.create('Личное')

    note_storage.create(
        'План встречи с клиентом',
        'Подготовить презентацию по проекту, обсудить сроки реализации, согласовать бюджет. Встреча в 14:00.',
        work
    )

    note_storage.create(
        'Список покупок',
        '- Хлеб\n- Яблоки\n- Стиральный порошок',
        personal
    )

    note_storage.create(
        'Задачи на неделю',
        f'1. Доделать отчёт по продажам (до среды).\n'
        f'2. Провести обучение для новых сотрудников (четверг).\n'
        f'3. Отправить документы партнёрам (пятница).',
        work
    )


def clear_all_data():
    """Удаляет все данные."""
    note_storage.clear()
    category_storage.clear()


def main():
    """Показывает все заметки по категориям."""
    if not note_storage.all():
        print('Пока пусто...')
    for category in category_storage.all():
        print('*', category.title.upper(), '*')
        for note in note_storage.get_by_category(category):
            print(' *', note.title, f'({note.created_at})')
        print()


if __name__ == '__main__':
    # create_sample_data()
    # clear_all_data()
    main()
