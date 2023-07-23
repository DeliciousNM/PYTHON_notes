import Repository.loadFromFile as lF
import Repository.writeToFile as wF
import Models.note

def add_note():
    title = input("Введите заголовок заметки: \n")
    body = input("Введите описание заметки: \n")
    note = Models.note.Note(title=title, body=body)
    array_notes = lF.read_file()
    for i in array_notes:
        if Models.note.Note.get_id(note) == Models.note.Note.get_id(i):
            Models.note.Note.set_id(note)
    array_notes.append(note)
    wF.write_file(array_notes, 'a')
    print("Заметка добавлена в журнал!")


def show(txt):
    array_notes = lF.read_file()

    if array_notes:
        if txt == "all":
            print("ЖУРНАЛ ЗАМЕТОК: ")
            for i in array_notes:
                print(Models.note.Note.map_note(i))

        elif txt == "ID":
            for i in array_notes:
                print("ID: ", Models.note.Note.get_id(i))
            id = input("\nВведите ID заметки: ")
            flag = True
            for i in array_notes:
                if id == Models.note.Note.get_id(i):
                    print(Models.note.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такого ID")

        elif txt == "date":
            date = input("Введите дату: ")
            flag = True
            for i in array_notes:
                date_note = str(Models.note.Note.get_date(i))
                if date == date_note[:10]:
                    print(Models.note.Note.map_note(i))
                    flag = False
            if flag:
                print("Нет такой даты")
        else:
            print("Журнал заметок пустой")


def del_notes():
    id = input("Введите ID удаляемой заметки: ")
    array_notes = lF.read_file()
    flag = False

    for i in array_notes:
        if id == Models.note.Note.get_id(i):
            array_notes.remove(i)
            flag = True

    if flag:
        wF.write_file(array_notes, 'a')
        print("Заметка с ID: ", id, " успешно удалена!")
    else:
        print("нет такого ID")


def change_note():
    id = input("Введите ID изменяемой заметки: ")
    array_notes = lF.read_file()
    flag = True
    array_notes_new = []
    for i in array_notes:
        if id == Models.note.Note.get_id(i):
            i.title = input("Измените  заголовок: \n")
            i.body = input("Измените  описание: \n")
            Models.note.Note.set_date(i)
            logic = False
        array_notes_new.append(i)

    if flag:
        wF.write_file(array_notes_new, 'a')
        print("Заметка с ID: ", id, " успешно изменена!")
    else:
        print("нет такого ID")