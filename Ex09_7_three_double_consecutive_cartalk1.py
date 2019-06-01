#Author : Ishwar Jindal
#Created On : 31-May-2019 09:10 PM
#Purpose : Find word with three consecutive double letters

def is_double_digit_with_n_sequence(word, sequence_needed):
    if len(word) < sequence_needed * 2:
        return False

    sequence_found = 0
    last_rhs_index_matched = -1

    lhs_index = 0
    while lhs_index + 1 < len(word) - 1:
        rhs_index = lhs_index + 1
        #if current and next word is same. if this is the first match i.e. sequence_found is zero then we found first match
        #if current and next word is same. if this is not the first match i.e. sequence_found is non zero then to ensure consecutiveness the current rhs index and last rhs index should have difference of two
        if word[lhs_index] == word[rhs_index] and (sequence_found == 0 or rhs_index - last_rhs_index_matched == 2):
            sequence_found = sequence_found + 1
            last_rhs_index_matched = rhs_index
            lhs_index = rhs_index + 1

            #this condition will handle scenario where a letter is repeated thrice in sequence. If this happens then we should treat last two character as match.
            if word[lhs_index - 1] == word[lhs_index]:
                last_rhs_index_matched = lhs_index
                lhs_index = lhs_index + 1
        else:
            lhs_index = lhs_index + 1
            
    if sequence_found >= sequence_needed:
        return True
    return False

def is_double_digit_with_three_sequence(word):
    return is_double_digit_with_n_sequence(word, 3)

print("main started")

fin = open("words.txt")
for line in fin:
    word = line.strip()
    if is_double_digit_with_three_sequence(word):
        print(str.format("{0} has three consequetive letters in it", word))
print("main ended")
