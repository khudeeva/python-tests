from text_pytest import (reverse_string, count_vowels,capitalize_first, is_alpha_only, is_upper, remove_spaces, remove_digits, extract_letters, is_palindrome, is_palindrome_sentence, capitalize_word, count_letter_frequency, filter_advanced, filtered_by_length, filtered_by_length_and_start, invert_words, analyze_string, analyze_case, describe_string, classify_word, classify_rich_word, analyze_text, letter_frequency, word_frequency, repeat_text, has_upper, all_capitalized, describe_words, book_data, user_info, words_list, people_data, products_list, users_list, movies_list, film_list, users_active, books_list, get_price, get_author, get_rating, get_pages, get_age, books_list_by_pages, get_pages_of_book, get_discounted_price, get_age_person, validate_password, calculate_shipping, calculate_tax,count_vowels_practice, reverse_text_practice, normalize_text_practice,count_words_practice, is_title_case, count_unique_words_practice, contains_only_letters_practice, count_uppercase, user_data_fixture, qa_skills, project_info, check_user_role, validate_age)
import pytest
# переворачиваем строку
def test_reverse_string():
    assert reverse_string("мир") == "рим"
# считаем гласные в строке
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


def test_classify_rich_word():
    assert classify_rich_word("аисточка") == "Богатое слово"
def test_classify_rich_word_no_rich():
    assert classify_rich_word("тааанец") == "Не богатое"
def test_classify_rich_word_not_rich():
    assert classify_rich_word("аист") == "Не богатое"

def test_analyze_text():
    assert analyze_text("Привет, как дела?") == {'Слова': 3, 'Буквы': 13, 'Пробелы': 2}
def test_analyze_not_spaces():
    assert analyze_text("каракатица") == {'Слова': 1, 'Буквы': 10, 'Пробелы': 0}
def test_analyze_text_one_letters():
    assert analyze_text("аааааааа ааааааааааааа") == {'Слова': 2, 'Буквы': 21, 'Пробелы': 1}
def test_analyze_text_only_spaces():
    assert analyze_text("     ") == {'Слова': 0, 'Буквы': 0, 'Пробелы': 5}

def test_letter_frequency():
    assert letter_frequency("Привет, мир!")   == {'п': 1, 'р': 2, 'и': 2, 'в': 1, 'е': 1, 'т': 1, 'м': 1}
def test_letter_frequency_one_word():
    assert letter_frequency("капитализация") == {'к': 1, 'а': 3, 'п':1,'и': 3, 'т': 1, 'л': 1 ,'з': 1, 'ц': 1, 'я': 1}

def test_word_frequency_one_word():
    assert word_frequency("самарканд") == {'самарканд': 1}
def test_word_frequency_two_words():
    assert word_frequency("капуста зеленая") == {'капуста': 1, 'зеленая': 1} 
def test_word_frequency_none():
    assert word_frequency("") == {}  
def test_word_frequency_repeat():
    assert word_frequency("дом дом сад сад сад") == {'дом': 2, 'сад': 3}
def test_word_frequency_mixed_case():
    assert word_frequency("Привет привет ПРИВЕТ") == {'привет': 3}
def test_word_frequency_symbols():
    assert word_frequency("Привет, мир!") == {'привет,': 1, 'мир!': 1}

def test_repeat_text():
    assert repeat_text("Привет") == "ПриветПривет"
def test_has_upper_start():
    assert has_upper("Привет") == True
def test_has_upper_end():
    assert has_upper("привеТ") == True
def test_has_upper_false():
    assert has_upper("привет") == False

def test_has_upper_start():
    assert has_upper("Каравай") == True
def test_has_upper_end():
    assert has_upper("караваН") == True
def test_has_upper_medium():
    assert has_upper("каРл") == True
def test_has_upper_false():
    assert has_upper("сарай") == False

def test_all_capitalized_true():
    assert all_capitalized(["Привет", "Python"]) == True
def test_all_capitalized_one():
    assert all_capitalized(["Привет", "помидор"]) == False
def test_all_capitalized_false():
    assert all_capitalized(["привет", "пока"]) == False

def test_describe_words_string():
    assert describe_words(["дом", "море", "поле"]) == "Все строчные"
def test_describe_words_upper():
    assert describe_words(["Дом", "Море", "Поле"]) == "Все заглавные"
def test_describe_words_mixed():
    assert describe_words(["дом", "Море", "поле"]) == "Смешанные"
def test_describe_words_empty():
    assert describe_words([]) == "Список пуст"

# фикстура словарь с данными книги
def test_title_not_empty(book_data):
    assert book_data["title"] != " "
def test_author_has_upper(book_data):
    assert any(char.isupper() for char in book_data["author"])
def test_pages_more_than_100(book_data):
    assert book_data["pages"] > 100

# фикстура с данными пользователя
def test_name_str(user_info):
    assert isinstance(user_info["name"], str) # проверка, что тип данных строка
def test_age_more_than_18(user_info):
    assert user_info["age"] > 18

# фикстура со списком слов
def test_len_5(words_list):
    assert len(words_list) == 5
def test_find_word(words_list):
    assert "пляж" in words_list 
def test_len_all_words_more_than_3(words_list):
    assert all(len(char) > 3 for char in words_list)

def test_all_have_name(people_data):
    for person in people_data:
        assert "name" in person
def test_age_more_than_20(people_data):
    for person in people_data:
        assert person["age"] > 20 



def test_names_products(products_list):
    for product in products_list:
        assert isinstance (product["name"], str) 

def test_have_price_and_more_than_0(products_list):
    for product in products_list:
        assert  "price" in product
        assert product["price"] > 0
def test_has_electronics(products_list):
    assert any(product["category"] == "electronics" for product in products_list)
def test_all_have_category(products_list):
    for product in products_list:
        assert "category" in product
        # ПРОВЕРКА С any(...)
def test_has_expensive_product(products_list): # проверка, что ХОТЯ бы 1 товар дороже 3000
    assert any(product["price"]> 3000 for product in products_list)
    
    # ПРОВЕРКА С all(...)
def test_all_have_name(products_list): # убедимся, что у всех товаров есть ключ и он не пустой
        assert all("name" in product and product["name"].strip() !="" for product in products_list)

    # ПРОВЕРКА С ЦИКЛОМ for
def test_no_negative_price(products_list): # проверка, что ни у одного товара нет отрицательной цены
    for product in products_list:
        assert product["price"] >= 0

# фикстура: список пользоватей
def test_all_have_username(users_list):
    assert all("username" in user and user["username"].strip() !="" for user in users_list)
def test_has_underage_user(users_list):
    assert any(user["age"] < 18 for user in users_list)
def test_valid_emails(users_list):
    for user in users_list:
        if user["email"]: # проверяем, что email не пустой
            assert "@" in user["email"]

# фикстура: список фильмов
def test_all_have_title(movies_list):
    assert all("title" in movie and movie["title"].strip() !="" for movie in movies_list)
def test_one_have_rating_9(movies_list):
    assert any(movie["rating"] > 9 for movie in movies_list)
def test_range_year(movies_list):
    for movie in movies_list:
        assert  1900 <= movie["year"] <= 2025
def test_all_have_genre(movies_list):
     assert all("genre" in movie and movie["genre"].strip() !="" for movie in movies_list)
    
#  фикстура + scope="module"
def test_contains_matrix(film_list):
    title = [film["title"] for film in film_list]
    assert "Matrix" in title
def test_all_movies_after_1980(film_list):
    assert all(film["year"] > 1980 for film in film_list)

# фикстура: список пользователей по активности
def test_user_with_guest(users_active):
    assert any(user["username"] == "guest" for user in users_active)
def test_all_active_users_len_more_than_4(users_active):
    for user in users_active:
        if user["active"] == True: 
            assert len(user["username"]) > 4
 # проверяем, что год ывпуска соответствует ожидаемому           
@pytest.mark.parametrize("title, expected_year", [
    ("1984", 1949),
    ("Brave New World", 1932),
    ("Dune", 1965)
])
def test_years_books(books_list, title, expected_year):
    book = next(book for book in books_list if book["title"] == title)
    assert book["year"]== expected_year

# проверяем, что у каждой книги - правильный автор
@pytest.mark.parametrize("title, expected_author",[
    ("1984", "George Orwell"),
    ("Brave New World", "Aldous Huxley"),
    ("Dune", "Frank Herbert")   
])
def test_author_of_books(books_list, title, expected_author):
    book = next(book for book in books_list if book["title"] == title)
    assert book["author"] == expected_author
# проверка длины названия книги
@pytest.mark.parametrize("title, min_length",[
    ("1984", 4),
    ("Brave New World", 13),
    ("Dune", 4)
])
def test_min_length_of_book(books_list, title, min_length):
    book = next(book for book in books_list if book["title"] == title)
    assert len(book["title"]) >= min_length

# проверка длины имени автора
@pytest.mark.parametrize("title, min_author_length",[
    ("1984", 12),
    ("Brave New World", 12),
    ("Dune", 12)
])
def test_min_author_length(books_list, title, min_author_length):
    book = next(book for book in books_list if book["title"] == title)
    assert len(book["author"]) >= min_author_length

# ПРОВЕРКА ИСКЛЮЧЕНИЙ 
# проверка исключения(KeyError)
def test_get_price_valid():
    product = {"name": "Milk", "price": 120}
    assert get_price(product) == 120
def test_get_price_missing_key():
    product = {"name": "Bread"}
    with pytest.raises(KeyError):
        get_price(product)

# проверка исключений автора книги
def test_get_author_valid():
    book = {"title": "Dune", "author": "Frank Herbert"}
    assert get_author(book) == "Frank Herbert"

def test_get_author_invalid():
    book = {"title": "Inkom"} 
    with pytest.raises(KeyError):
        get_author(book)

# проверяем рейтинг фильма с pytest.raises
def test_get_rating_valid(): # корректный рейтинг
    movie = {"title": "Inception", "rating": 8.8}
    assert get_rating(movie) == 8.8

def test_get_rating_invalid(): # нет ключа - ожидаем KeyError
    movie = {"title": "Inception"}
    with pytest.raises(KeyError):
        get_rating(movie)

def test_get_rating_str(): #рейтинг - строка - TypeError
    movie = {"title": "Inception", "rating": "high"}
    with pytest.raises(TypeError):
        get_rating(movie)

def test_get_rating_range():# рейтинг вне диапазона
    movie = {"title": "Inception", "rating": 11}
    with pytest.raises(ValueError):
        get_rating(movie)

# проверка страниц книги
def test_get_pages_valid():
    book = {"title": "Yoga", "pages": 130}
    assert get_pages(book) == 130
def test_get_pages_no_key():
    book = {"titlt": "Yoga"}
    with pytest.raises(KeyError):
        get_pages(book)
def test_get_pages_no_str():
    book = {"title": "Yoga", "pages": "low"}
    with pytest.raises(TypeError):
        get_pages(book)
def test_get_pages_no_value():
    book = {"title": "Yoga", "pages": 3000}
    with pytest.raises(ValueError):
         get_pages(book)

# тестируем список пользователей (фикстура + параметризация)
@pytest.mark.parametrize("username, expected_email", [
    ("admin", "admin@example.com"),
    ("manager", "manager@example.com")
]) # проверка, что email есть у admin, manager
def test_users_list_email(users_list, username,  expected_email):
    user = next(user for user in users_list if user["username"]== username)
    assert user["email"] == expected_email 

# проверка возраста исключениями
def test_get_age_no_number():
    user = {"username": "manager", "age": "unknown", "email": "manager@example.com"}
    with pytest.raises(TypeError):
        get_age(user)

def test_get_age_negative():
    user = {"username": "manager", "age": -1, "email": "manager@example.com"}
    with pytest.raises(ValueError):
        get_age(user)

# проверка объединения со списком книг
@pytest.mark.parametrize("title, expected_pages",[
 ("Dune", 412),
 ("1984", 328)
])
def test_books_list_pages(books_list_by_pages, title, expected_pages):
    book = next(book for book in books_list_by_pages if book["title"]== title)
    assert book["pages"] == expected_pages

# работа с исключенями по страницам книг
def test_get_pages_no_pages():
    books = {"title": "Brave New World", "pages": "many", "available": True}
    with pytest.raises(TypeError):
        get_pages_of_book(books)
def test_get_pages_negative():
    books = {"title": "Brave New World", "pages": -10, "available": True}
    with pytest.raises(ValueError):
        get_pages_of_book(books)

# параметризация + проверка исключений
@pytest.mark.parametrize("product, expected_result", [
    ({"name": "Phone", "price": 1000, "discount": 0.1}, 900),
    ({"name": "Book", "price": 500, "discount": 2}, ValueError),                 # скидка слишком большая
    ({"name": "Pen", "price": 0, "discount": 0.1}, ValueError),                 # цена = 0
    ({"name": "Watch", "price": "expensive", "discount": 0.2}, TypeError),     # цена строка
    ({"name": "Bag", "price": 700, "discount": "a lot"}, TypeError),           # скидка строка
])
def test_discounted_price(product, expected_result):
    if isinstance(expected_result, type) and issubclass(expected_result, Exception):
        with pytest.raises(expected_result):
            get_discounted_price(product)
    else:
        assert get_discounted_price(product) == expected_result

# ищем возраст (параметризация + проверка исключений)
@pytest.mark.parametrize("user, expected_result", [
    ({"name": "Anna", "age": 25}, 25),
    ({"name": "Bob", "age": 0}, ValueError),
    ({"name": "Alice", "age": "unkown"}, TypeError),
    ({"name": "Maria", "age": -20}, ValueError),
    ({"name": "Olga", "age": 21.6}, 21.6),
    ({"name": "Oleg", "age": None},  TypeError)
])
def test_get_age_person(user, expected_result):
    if isinstance(expected_result, type) and issubclass(expected_result, Exception):
        with pytest.raises(expected_result):
            get_age_person(user)
    else:
        assert get_age_person(user) == expected_result

@pytest.mark.parametrize("password_list, expected_result",[
    ({"password": "abc123"}, "Password accepted"),
    ({"password": "short"}, ValueError),
    ({"password": 123456}, TypeError),
    ({"password": "abcdef"}, ValueError),
    ({"password": "pass123word"}, "Password accepted")
])
def test_validate_password(password_list, expected_result):
    if isinstance(expected_result, type) and issubclass(expected_result, Exception):
        with pytest.raises(expected_result):
            validate_password(password_list)
    else:
        assert validate_password(password_list) == expected_result 

# проверка стоимости доставки
@pytest.mark.parametrize("order, expected_result", [
    ({"weight": 2, "destination": "local"}, 10),
    ({"weight": 1.5, "destination": "international"}, 15.0),
    ({"weight": 0, "destination": "local"}, ValueError),
    ({"weight": "heavy", "destination": "local"}, TypeError),
    ({"weight": 3, "destination": "moon"}, ValueError),
])
def test_calculate_shipping(order, expected_result):
    if  isinstance(expected_result, type) and issubclass(expected_result, Exception):
        with pytest.raises(expected_result):
            calculate_shipping(order)
    else:
        assert calculate_shipping(order) == expected_result

# проверка налог на покупку
@pytest.mark.parametrize("item, expected_result", [
    ({"price": 100, "tax_rate": 0.2}, 120),
    ({"price": 200, "tax_rate": 0.15}, 230),
    ({"price": -100, "tax_rate": 0.2}, ValueError),
    ({"price": 100, "tax_rate": "high"}, TypeError)
])
def test_calculate_tax(item, expected_result):
    if isinstance(expected_result, type) and issubclass(expected_result, Exception):
        with pytest.raises(expected_result):
            calculate_tax(item)
    else:
        assert calculate_tax(item) == expected_result

    # ПОВТОРЕНИЕ
def test_count_vowels_practice():
    assert count_vowels_practice("Привет") == 2
    assert count_vowels_practice("Солнце Ясное") == 5
    assert count_vowels_practice("") == 0
    assert count_vowels_practice("БРРРР") == 0
    assert count_vowels_practice("УЗИ") == 2
def test_reverse_text_practice():
    assert reverse_text_practice("Привет") == "тевирП"
    assert reverse_text_practice("топот") == "топот"
    assert reverse_text_practice("N") == "N"
    assert reverse_text_practice("") == ""
def test_normalize_text_practice():
    assert normalize_text_practice(" ПРивет  ") == "привет"
    assert normalize_text_practice("     p ") =="p"
    assert normalize_text_practice("   ")==""
def test_count_words_practice():
    assert count_words_practice("Привет, как дела?") == 3
    assert count_words_practice("  Один  Два три  ") == 3
    assert count_words_practice("") == 0
def test_is_title_case():
    assert is_title_case("Привет, мир!") == True
    assert is_title_case("   привет") == False
    assert is_title_case("123") == False
    assert is_title_case("") == False

def test_count_unique_words_practice():
    assert count_unique_words_practice("Привет привет Привет") == 1  
    assert count_unique_words_practice("QA is great and QA is fun") == 5  
    assert count_unique_words_practice("  Один  два три три  ") == 3  
    assert count_unique_words_practice("") == 0

def test_contains_only_letters_practice():
    assert contains_only_letters_practice("Ksenia") == True
    assert contains_only_letters_practice("Ксения") == True
    assert contains_only_letters_practice("Ksenia13243") == False
    assert contains_only_letters_practice("   QA ") == False
    assert contains_only_letters_practice("") == False

def test_count_uppercase():
    assert count_uppercase("Привет Мир!") == 2
    assert count_uppercase("HELLO") == 5
    assert count_uppercase("hello") == 0
    assert count_uppercase("") == 0

def test_user_data_fixture(user_data_fixture):
    assert user_data_fixture["name"] == "Марина"
    assert user_data_fixture["role"] == "QA"
    assert user_data_fixture["age"] >= 18

def test_qa_skills(qa_skills):
    assert "Selenium" in qa_skills
    assert len(qa_skills) == 4
    assert qa_skills 

def test_project_info(project_info):
    assert project_info["project"] == "Autotest"
    assert isinstance(project_info["version"], float)
    assert project_info["version"] > 0

# @pytest.fixture(autouse=True)
# def show_test_start():
#     print("\n Тест начинается...")
# def test_something():
#     assert 1 + 1 ==2

@pytest.fixture
def open_and_close():
    print("Open соединение")
    yield "соединение"
    print("Close соединение")
def test_connection(open_and_close):
    assert True

@pytest.fixture
def valid_roles():
    return ["QA", "Dev", "PM"]
@pytest.mark.parametrize("role, expect_error", [
    ("QA", False),
    ("Dev", False),
    ("Designer", True)
])
def test_check_user_role(role, expect_error, valid_roles):
    if expect_error:
        with pytest.raises(ValueError):
            check_user_role(role, valid_roles)
    else:
        assert check_user_role(role, valid_roles) == "OK"

@pytest.fixture
def min_age():
    return 18
@pytest.mark.parametrize("age, error_age", [
    (20, False),
    (18, False),
    (17, True)
])
def test_validate_age(age, error_age, min_age):
    if error_age:
        with pytest.raises(ValueError):
            validate_age(age, min_age)
    else:
        assert validate_age(age, min_age) == "Допущен"

