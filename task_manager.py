import os

def clear_screen():
    if os.name == 'nt':
        os.system('cls')

def task_pin(file):
    for i, task in enumerate(file, start=1):
        print(f'{i} {task.strip()}')

def task_manager():
    with open('tasks.txt', 'a'):
        pass

    
    check_1 = True
    while check_1 == True:
        print('1. Добавить задачу')
        print('2. Просмотреть задачи')
        print('3. Удалить задачу')
        print('4. Выход')
        check_1 = False
        choose = input('Выберите действие: ')
        if choose == '1':
            task = input('Введите задачу: ')
            with open('tasks.txt', 'a') as file:
                file.write(task + '\n')
                print('Задача добавлена.')
                clear_screen()
                check_1 = True
        elif choose == '2':
            with open('tasks.txt', 'r') as file:
                tasks = file.readlines()
                if len(tasks) == 0:
                    print('Список задач пуст.')
                    print('================================')
                    check_1 = True
                else:
                    print('Список задач:')
                    task_pin(tasks)
                    print('================================')
                    check_1 = True
        elif choose == '3':
            with open('tasks.txt','r') as file:
                tasks = file.readlines()
                if len(tasks) == 0:
                    print('Список задач пуст.')
                    print('================================')
                    check_1 = True
                else:
                    print('Выберите задачу для удаления:')
                    task_pin(tasks)
                    try:
                        task_number = int(input('Введите номер задачи: '))
                        
                        if 1 <= task_number <= len(tasks):
                            del tasks[task_number - 1]
                            with open('tasks.txt', 'w') as file:
                                file.writelines(tasks)
                            print('Задача удалена.')
                        else:
                            print('Задачи с таким номером нет.')
                            
                    except ValueError:
                        print('Ошибка: Пожалуйста, введите цифру, а не текст.')
                    print('================================')
                    check_1 = True
        elif choose == '4':
            print('Выход из программы.')
            break
    else:
        print('Ошибка: Пожалуйста, введите цифру от 1 до 4.')
        print('================================')
        task_manager()
                                    
task_manager()
