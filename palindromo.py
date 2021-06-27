def palindrome(word):
    word = word.replace(' ', '')
    word = word.lower()
    if word[::-1] == word:
        return True
    else:
        return False


def run():
    words = input('write a word: ')
    is_palindrome = palindrome(words)
    if is_palindrome == True:
        print("It's palindrome")
    else:
        print("Isn't palindrome")


if __name__ == '__main__':
    run()