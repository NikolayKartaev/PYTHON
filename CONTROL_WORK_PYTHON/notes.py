import argparse
import datetime
import json

# {Идентификатор, Заголовок, Тело Заметки, Дата и время создания//Изменения}

def add_note(notes, title, message):                                                                                        # список, заголовок, тело заметки
    note_id = len(notes) + 1
    for note in notes:
        if note['note_id'] == note_id:
            note_id = note_id + 1                                                                                                                                                                  
    created_at = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')                                                      # дата и время заметки
    new_note = {'note_id': note_id, 'title': title, 'message': message, 'created_at': created_at, 'updated_at': created_at} # создание заметки в виде JSON (ключ:значение)
    notes.append(new_note)                                                                                                  # список заметок
    save_notes_to_file(notes)                                                                                               # запись в файл

def edit_note(notes, note_id, title, message):
    for note in notes:
        if note['note_id'] == note_id:
            note['title'] = title
            note['message'] = message
            note['updated_at'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            break
    save_notes_to_file(notes)

def delete_note(notes, note_id):
    notes[:] = [note for note in notes if note['note_id'] != note_id]                                                       # создание списка без заметки с указанным ID
    save_notes_to_file(notes)

def filter_notes_by_date(notes, date):
    filtered_notes = [note for note in notes if note['created_at'].startswith(date)]
    return filtered_notes

def save_notes_to_file(notes):
    with open('notes.json', 'w') as file:
        json.dump(notes, file, indent=4)

def load_notes_from_file():
    try:
        with open('notes.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def homework():
    user_parser = argparse.ArgumentParser()
    user_parser.add_argument('action', choices=['add', 'edit', 'delete', 'print_list', 'filter'])
    user_parser.add_argument('--title', help='Note title')
    user_parser.add_argument('--id', help='Note id')
    user_parser.add_argument('--msg', help='Note message')
    user_parser.add_argument('--date', help='Filter notes by date')
    
    args = user_parser.parse_args()
    
    notes = load_notes_from_file()

    if args.action == 'add':
        add_note(notes, args.title, args.msg)
    elif args.action == 'edit':
        edit_note(notes, int(args.id), args.title,args.msg)
    elif args.action == 'delete':
        delete_note(notes, int(args.id))
    elif args.action == 'print_list':
        for note in notes:
            print(f"ID: {note['note_id']}, Title: {note['title']}, Created: {note['created_at']}")
    elif args.action == 'filter':
        filtered_notes = filter_notes_by_date(notes, args.date)
        for note in filtered_notes:
            print(f"ID: {note['note_id']}, Title: {note['title']}, Created: {note['created_at']}")

if __name__ == '__main__':
    homework()


# ТИПОВЫЕ КОМАНДЫ: 
# СОЗДАНИЕ ЗАМЕТКИ:                                     python notes.py add --title "NEW NOTE" --msg "This is my new note" 
# РЕДАКТИРОВАТЬ ЗАМЕТКУ:                                python notes.py edit --id "3" --title "THIRD NOTE" --msg "This is my updated note"
# УДАЛИТЬ ЗАМЕТКУ:                                      python notes.py delete --id "2"
# ВЫВЕСТИ СПИСОК ЗАГОЛОВКОМ ЗАМЕТОК И ДАТ СОЗДАНИЯ:     python notes.py print_list
# ФИЛЬТРАЦИЯ ЗАМЕТОК ПО ДАТЕ:                           python notes.py filter --date "2023-08-18"
