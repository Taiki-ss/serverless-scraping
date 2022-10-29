
def handle_data(text):
    try:
        with open('data.txt') as f:
            print('Read Success!')
            if f.read() != text:
                f2 = open('data.txt', 'w')
                f2.write(text)
                f2.close()
                print('Update file')
                return True
            else:
                return False

    except FileNotFoundError:
        print('Create a new file because it does not exist')
        f = open('data.txt', 'w')
        f.write(text)
        f.close()
        return True
