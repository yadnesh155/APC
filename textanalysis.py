text = input("Enter your paragraph: ")

words = text.split()
total_words = len(words)
print("Total number of words:", total_words)

word_freq = {}
for word in words:
    word = word.lower()  
    if word in word_freq:
        word_freq[word] += 1
    else:
        word_freq[word] = 1

print("\nWord frequency:")
for word, freq in word_freq.items():
    print(word, ":", freq)

top_3 = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:3]
print("\nTop 3 most frequent words:")
for word, freq in top_3:
    print(word, ":", freq)

vowels = "aeiouAEIOU"
vowel_count = sum(1 for char in text if char in vowels)
print("\nNumber of vowels in the text:", vowel_count)
