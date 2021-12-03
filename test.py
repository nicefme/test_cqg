def main(config_dict, text_list):
    new_text_dict = {}

    for word in text_list:
        new_word = []
        count = 0
        for symbol in word:
            if symbol in config_dict.keys():
                new_word.append(config_dict[symbol])
                count += 1
            else:
                new_word.append(symbol)
        new_text_dict[''.join(new_word)] = count

    sorted_dict = sorted(
        new_text_dict.items(), key=lambda x: x[1], reverse=True
    )

    for word in sorted_dict:
        print(word[0])


def open_files():
    config_dict = {}
    text_list = []

    while not config_dict:
        try:
            with open(input('Введите название файла конфигурации: ')) as file:  # configuration_file.txt
                for line in file:
                    config_dict[line.rstrip('\n').split('=')[0]] = (
                        line.rstrip('\n').split('=')[1]
                    )
        except FileNotFoundError:
            print('*Данный файл или каталог отсутствует*')

    while not text_list:
        try:
            with open(input('Введите название файла с текстом: ')) as file:  # text_file.txt
                for line in file:
                    text_list.append(line.strip('\n'))
        except FileNotFoundError:
            print('*Данный файл или каталог отсутствует*')

    main(config_dict, text_list)


if __name__ == '__main__':
    open_files()
