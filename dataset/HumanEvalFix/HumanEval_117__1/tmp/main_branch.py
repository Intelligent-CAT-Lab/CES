def select_words(s, n):
    result = []
    for word in s.split():
        n_consonants = 0
        for i in range(0, len(word)):
            print('[LINE]5[/LINE] may be hit')
            if word[i].lower() in ["a","e","i","o","u"]:
                print('[LINE]5[/LINE] is hit')
                n_consonants += 1 
        print('[LINE]7[/LINE] may be hit')
        if n_consonants == n:
            print('[LINE]7[/LINE] is hit')
            result.append(word)
    return result


select_words('Mary had a little lamb', 3)