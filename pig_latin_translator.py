# pig -> igPay
# glove -> oveGlay
# duck -> uckDay
# apple -> appleyay
# eat -> eatyay
# if it starts with a vowel => add "yay"
# otherwise, move the first consonant cluster to end, and add 'ay'

#Get sentence from user
original = input("Enter a sentence: ").strip().lower()
#Split sentence into words
words = original.split()
#Loop through the words and convert to pig latin
new_words = []
for word in words:
    if word[0] in 'aeiou':
        word += 'yay'
        new_words.append(word)
    else:
        vowel_pos = 0
        for letter in word:
            if letter not in 'aeiou':
                vowel_pos+=1
            else:
                break
        cons = word[:vowel_pos]
        the_rest_of_the_word = word[vowel_pos:]
        new_word = the_rest_of_the_word + cons + 'ay'
        new_words.append(new_word)
print(new_words)
# Stick words back together into a sentence

output = " ".join(new_words)
print(output)