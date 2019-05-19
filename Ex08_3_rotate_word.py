# Author        Ishwar Jindal
# Created On    19-May-2019 05:15 PM
# Purpose       rotate the letters in given input by specified length

def rotate_word(word, rotate_by):
    rotated_word = ""
    for letter in word:
        if letter.isalpha() == True:
            rotated_letter = ord(letter) + rotate_by
            if chr(rotated_letter).isalpha() == True:
                rotated_word = rotated_word + chr(rotated_letter)
            elif letter.islower() == True:
                if rotate_by >= 0:
                    rotated_letter = ord(letter) + rotate_by - ord('z') - 1 + ord('a')
                    rotated_word = rotated_word + chr(rotated_letter)
                else:
                    rotated_letter = ord('a') - ord(letter) + rotate_by + 1 + ord('z')
                    rotated_word = rotated_word + chr(rotated_letter)
            else:
                if rotate_by >= 0:
                    rotated_letter = ord(letter) + rotate_by - ord('Z') - 1 + ord('A')
                    rotated_word = rotated_word + chr(rotated_letter)
                else:
                    rotated_letter = ord('A') - ord(letter) + rotate_by + 1 + ord('Z')
                    rotated_word = rotated_word + chr(rotated_letter)                    
        else:
            rotated_word = rotated_word + letter
    return rotated_word

#word = "Ishwar Chandra Vidya Sagar Jindal"
#word = "AXBYCZ axbycz 1a 2b 3c 4X 5Y 6Z"
word = "NASA"
rotate_by = 2
rotated_word = rotate_word(word, rotate_by)

print(str.format("{0} becomes {1} when rotated by {2}", word, rotated_word, rotate_by))
