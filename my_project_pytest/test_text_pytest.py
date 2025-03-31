from text_pytest import (reverse_string, count_vowels,capitalize_first, is_alpha_only, is_upper, remove_spaces, remove_digits, extract_letters, is_palindrome, is_palindrome_sentence, capitalize_word, count_letter_frequency, filter_advanced, filtered_by_length, filtered_by_length_and_start, invert_words, analyze_string, analyze_case, describe_string, classify_word)

def test_reverse_string():
    assert reverse_string("мир") == "рим"

def test_vowels_in_moloko():# проверка 3 гласных в слове
    assert count_vowels("молоко") == 3
def test_vowels_dom():# проверка 1 гласная в слове
    assert count_vowels("дом") == 1
def test_vowels_empty_text(): # проверка пустая строка - 0
    assert count_vowels("") == 0
    
def test_capitalize_first_in_sea():
    assert capitalize_first("море") == "Море" 
def test_capitalize_empty():
    assert capitalize_first("") == ""
def test_capitalize_already_capital():
    assert capitalize_first("Мир") == "Мир"

def test_is_aplpha_more():
    assert is_alpha_only("Море") == True
def test_is_alpha_dom123():
    assert is_alpha_only("Дом123") == False
def test_is_alpha_mir():
    assert is_alpha_only("Мир!") == False
def test_is_alpha_empty():
    assert is_alpha_only("") == False

def test_is_upper_first_letter_true():
    assert is_upper("Лес") == True
def test_is_upper_first_letter_false():
    assert is_upper("край") == False
def test_is_upper_first_letter_empty():
    assert is_upper("") == False

def test_remove_spaces_between():
    assert remove_spaces("молоко и мёд") == "молокоимёд"
def test_remove_spaces_start_and_end():
    assert remove_spaces(" без пробелов ") == "безпробелов"
def test_remove_spaces_empty():
    assert remove_spaces("") == ""

def test_remove_digits_text_and_digit():
    assert remove_digits("дом123") == "дом"
def test_remove_digits_text_space_digit_symbol():
    assert remove_digits("мир 2025!") == "мир !"
def test_remove_digits_only():
    assert remove_digits("42") == ""
def test_remove_digits_empty():
    assert remove_digits("") == ""

def test_extract_letters_text_number_symbol():
    assert extract_letters("дом 123!") == "дом"
def test_extract_letters_text_symbol():
    assert extract_letters("люк:№") == "люк"
def test_extract_letters_only_number():
    assert extract_letters("43") == ""
def test_extract_letters_empty():
    assert extract_letters("") == ""

def test_is_palindrome_true():
    assert is_palindrome("топот") == True
def test_is_palindrome_false():
    assert is_palindrome("корова") == False
def test_ispalindrome_letter():
    assert is_palindrome("а") == True
def test_is_palindrome_empty():
    assert is_palindrome("")== True 

def test_is_palindrome_sentence_true():
    assert is_palindrome_sentence("А роза упала на лапу Азора") == True
def test_is_palindrome_sentence_false():
    assert is_palindrome_sentence("я иду с мячом") == False
def test_is_palindrome_sentence_empty():
    assert is_palindrome_sentence("") == True

def test_capitalize_word_true():
    assert capitalize_word("мама мыла раму") == "Мама Мыла Раму"
def test_capitalize_word_with_symbol_true():
    assert capitalize_word("привет, мир!") == "Привет, Мир!"
def test_capitalize_word_empty():
    assert capitalize_word("") == ""

def test_filtered_by_length_4():
    assert filtered_by_length("мама мыла раму", 4) == ["мама", "мыла", "раму"]
def test_filtered_by_length_3():
    assert filtered_by_length("дом уф да", 3) ==["дом"]
def test_filtered_by_length_empty():
    assert filtered_by_length("", 3) == []

def test_filter_by_length_and_start_4_m():
    assert filtered_by_length_and_start("мама мыла раму мак", 4, "м") == ["мама", "мыла"]
def test_filter_by_length_and_start_4_d():
    assert filtered_by_length_and_start("дом дядя кран друг", 4, "д") == ["дядя", "друг"]
def test_filtered_by_length_and_start_5_c():
    assert filtered_by_length_and_start("свет сок срок", 5, "с") == []
def test_filtered_by_length_and_start_3_m():
    assert filtered_by_length_and_start("", 3, "ы") == []

def test_filtered_advanced_4_start_m_no_o():
    assert filter_advanced("мама мыла раму мак", 4, "м", "ы") == ["мама"]
def test_filtered_advanced_3_start_d_no_y():
    assert filter_advanced("друг дом дуб", 3, "д", "о") == ["друг", "дуб"]
def test_filtered_advanced_empty():
    assert filter_advanced("", 2, "и", "к") == []

def test_invert_words():
    assert invert_words("мама мыла раму") == "амам алым умар"
def test_invert_words_space():
    assert invert_words("привет мир") == "тевирп рим"
def test_invert_words_empty():
    assert invert_words("") == ""

def test_count_frequency_a():
    assert count_letter_frequency("мама мыла раму", "а") == 4
def test_count_frequency_r():
    assert count_letter_frequency("Привет Мир", "р") == 2
def test_count_letter_frequency_none():
    assert count_letter_frequency("", "а") == 0

def test_analyze_string_empty():
    assert analyze_string("") == "Пустая строка"
def test_analyze_string_spaces_only():
    assert analyze_string("    ") == "Только пробелы"
def test_analyze_string_digits_only():
    assert analyze_string("12345") == "Цифры"
def test_analyze_strings_letters_only():
    assert analyze_string("Привет") == "Буквы"
def test_analyze_strings_mixed():
    assert analyze_string("Привет234") == "Смешанная строка"
def test_analyze_string_symbol_and_letters():
    assert analyze_string("Привет:%№") == "Смешанная строка"
def test_analyze_string_only_symbol():
    assert analyze_string("&%$#%@") == "Только спецсимволы"

def test_analyze_case_upper():
    assert analyze_case("ПРИВЕТ МИР") == "Все буквы заглавные"
def test_analyze_case_lower():
    assert analyze_case("привет мир") == "Все буквы строчные"
def test_analyze_case_mixed():
    assert analyze_case("ПрИвЕт мИр") == "Смешанный регистр"
def test_analyze_case_only_symbol():
    assert analyze_case("^%#^$)") == "Нет букв"
def test_analyze_test_symbol_and_letters():
    assert analyze_case("ПРИвет ?:%") == "Смешанный регистр"

def test_describe_string_correct():
    assert describe_string("Привет.") == "Корректное предложение"
def test_describe_string_not_point():
    assert describe_string("Привет") == "Нет точки в конце"
def test_describe_string_not_capitalize():
    assert describe_string("привет.") == "Нет заглавной буквы в начале"
def test_describe_string_no_correct():
    assert describe_string("привет") == "Некорректная строка"

def test_classify_word_only_vowels():
    assert classify_word("иаеа") == "Только гласные"
def test_classify_word_only_consonants():
    assert classify_word("зтпр") == "Только согласные"
def test_classify_word_only_symbol():
    assert classify_word("(*&^$)") == "Нет букв"
def test_classify_word_mixed():
    assert classify_word("топот") == "Смешанное"
def test_classify_word_mixed_case():
    assert classify_word("БаРд") == "Смешанное"
