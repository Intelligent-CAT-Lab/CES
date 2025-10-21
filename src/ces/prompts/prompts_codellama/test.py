def count_vowels_consonants(input_string):
    vowels = 'aeiouAEIOU'
    vowel_count = 0
    consonant_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count += 1  
        else:
            consonant_count += 1 
    return (vowel_count, consonant_count)

# Example usage:
text = "Hello, World!"
result = count_vowels_consonants(text)
print(result)  # Output: {'vowels': 3, 'consonants': 7}
