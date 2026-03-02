def count_vowels_consonants(text):
    vowels = "aeiouAEIOU"
    vowel_count = sum(1 for char in text if char in vowels)
    consonant_count = sum(1 for char in text if char.isalpha() and char not in vowels)
    return vowel_count, consonant_count

# Example usage
if __name__ == '__main__':
    text = input("Enter a string: ")
    vowels, consonants = count_vowels_consonants(text)
    print(f'Vowels: {vowels}, Consonants: {consonants}')