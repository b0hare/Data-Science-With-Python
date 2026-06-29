
def count_line():
    file = open("file.txt", 'r')
    count = 0
    for line in file:
        count+=1
    return count

    


def repeated_word():
    file = open("file.txt", 'r')
    text = file.read().lower()
    
    file.close()

    words = text.split()
    
    freq = {}

    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    most_word = ""
    max_count = 0

    for word in freq:
        if word != "the":
            if freq[word] > max_count:
                max_count = freq[word]
                most_word = word

    return most_word.upper()
    

time = count_line()

if(time > 12):
    print("The Meeting time is: %d PM" %time)
else:
    print("The Meeting time is: %d AM" %time)

print("The Meeting place is", repeated_word())