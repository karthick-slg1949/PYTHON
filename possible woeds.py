def charcount(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict
def possible_words(lwords, charset):
    for word in lwords:
        flag = 1
        chars = charcount(word)
        for key in chars:
            if key not in charset:
                flag = 0
            else:
                if charset.count(key) != chars[key]:
                    flag = 0
        if flag == 1:
            print(word)
if __name__ == "__main__":
    input = ['go', 'bat','me','eat','goal','boy','run']
    charset = ['e', 'o', 'b', 'a', 'm', 'g', 'l']
    possible_words(input, charset)