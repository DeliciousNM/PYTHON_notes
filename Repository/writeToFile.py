import Models.note

def write_file(array, mode):
    file = open("memory.csv", mode='w', encoding='utf-8')
    file.seek(0)
    file.close()
    file = open("memory.csv", mode=mode, encoding='utf-8')
    for notes in array:
        file.write(Models.note.Note.to_string(notes))
        file.write('\n')
    file.close
