def most_frequent(string):
    d = dict()
    for key in string:
        d[key] = d.get(key, 0) + 1
    return d

def letters_in_order_of_frequency(string):
    frequencies = most_frequent(string) 
    frequency_list = [(freq, letter) for (letter, freq) in frequencies.iteritems()]
    frequency_list.sort(reverse=True)
    return [letter for freq, letter in frequency_list]

string = 'aabbbc'
print letters_in_order_of_frequency(string)
