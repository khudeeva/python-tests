# функции со словарями(поиск по ролям, активности, форматирование)
# 📋Получение данных из словаря(ключи, значения, пары)
# получаем имена пользователей
def get_user_names(users):
    names = users.values()
    name_list = list(names)
    sorted_names = sorted(name_list)
    return sorted_names

# получаем список всех ключей пользователей
def keys_list(users):
    id = users.keys()
    id_list = list(id)
    sorted_id = sorted(id_list)
    return sorted_id

# получаем пары в виде "имя - id"
def name_id_pairs(users):
    result = []
    for key, value in users.items():
        pair = f"{value} - {key}"
        result.append(pair)
    return result

# получаем строки "ID: имя", сортируем по имени
def names_id(users):
    result = []
    for key, value in sorted(users.items(), key=lambda item: item[1]):
        keys_names = f"{key}:{value}"
        result.append(keys_names)
    return result
# получаем список всех ключей в словаре, отсортируем по алфавиту
def find_all_keys(data):
        return sorted(data.keys()) 
      # return sorted(data.keys(), key=lambda x: int(x)) - сортируем по числу

# ✅Фильтрация пользователей по активности, ролям
# ищем пользователей, у которых активность = True
def get_active_users(users):
    result = []
    for key,value in users.items():
        if value == True:
            result.append(key)
    return sorted(result)

# ищем неактивных пользователей = False
def get_inactive_users(users):
    result = []
    for key, value in users.items():
        if value == False:
            result.append(key)
    return sorted(result)

# ищем пользователей по роли
def find_admins(users):
    result = []
    for key, data in users.items():
        if data["role"] == "admin":
         result.append(key)
    return sorted(result)

# ищем активных пользователей с ролью "user"
def find_role_active(users):
    result = []
    for key, data in users.items():
        if data["role"] == "user" and data["active"] == True:
            result.append(key)
    return sorted(result)

# собираем строки "Имя (роль)"
def format_user_roles(users):
    result = []
    for key, data in users.items():
        user_info = f"{key}({data['role']})"
        result.append(user_info)
    return sorted(result)
# Ищем пользователей с определенной ролью и активностью
def find_users(users, role, only_active):
    result = []
    for key, data in users.items():
        if data["role"] == role and (data["active"]or not only_active):
            result.append(key)
    return sorted(result)

# Практика на разные темы
# ищем пользователей с определенным заказом еды (+ vegan)
def find_orders(orders, dish, only_vegan):
    result = []
    for key, data in orders.items():
        if data["dish"] == dish and (data["is_vegan"] or not only_vegan):
            result.append(key)
    return sorted(result)

# ищем псов и их имена
def find_pets(pets):
    result = []
    for key, data in pets.items():
        if data["type"] == "пёс":
            result.append(key)
    return sorted(result)
# Ищем учеников, которые учатся в обоих классах
def find_class(class_a, class_b):
    set1 = set(class_a)
    set2 = set(class_b)
    return(set1 & set2) 

# Ищем учеников, которые учатся ТОЛЬКО  в одном из 2х классов        
def find_only_class(class_a, class_b):
    set1 = set(class_a)
    set2 = set(class_b)
    return sorted(set1 ^ set2) 
# ищем блюда, заказанне только веганами 1 раз
def find_unique_vegan_dishes(orders):
    vegan_dishes = []
    for key, data in orders.items():  # ищеи блюда заказанные веганами
        if data["vegan"]:
            vegan_dishes.append(data["dish"])

    seen_once = set()
    duplicates = set()

    for dish in vegan_dishes: # тщем блюдо, которое встречалось только 1 раз
        if dish in seen_once:
            duplicates.add(dish)
        else:
            seen_once.add(dish)
    unique_dishes = seen_once - duplicates
    return sorted(unique_dishes)


# 🔁Поиск повторений и уникальности роли
# считаем количество пользователей по ролям
def count_roles(users):
    role_counts = {}
    for key, data in users.items():
       role = data["role"]
       if data["role"] in role_counts:
           role_counts[role] += 1
       else:
        role_counts[role] = 1
    return role_counts
        
# ищем имена, которые встречаются в списке больше 1 раза
def find_repeated_names(names):
    seen_once = set()  # множества имен, которые встречались 1 раз
    duplicates = set() # множества имен, кторые повторялись

    for name in names:
        if name in seen_once:
            duplicates.add(name)
        else:
            seen_once.add(name)
    return sorted(duplicates)

# ищем повторяющиеся роли пользователей
def find_repeated_roles(users):
    seen_only = set()
    duplicates = set()

    for key, data in users.items():
        role = data["role"]
        if data["role"] in seen_only:
            duplicates.add(role)
        else:
            seen_only.add(role)

    return sorted(duplicates)

# ищем роли, которые встречаются только 1 раз
def find_unique_roles(users):
    seen_once = set()
    duplicates = set()

    for key, data in users.items():
        role = data["role"]
        if data["role"] in seen_once:
            duplicates.add(role)
        else:
            seen_once.add(role)
    return sorted(seen_once - duplicates)

# ищем пользователей с уникальной ролью
def find_users_with_unique_roles(users):
    seen_once = set()
    duplicates = set()
    for key, data in users.items():
        role = data["role"]
        if role in seen_once:
            duplicates.add(role)
        else:
            seen_once.add(role)
        
    unique_roles = seen_once - duplicates
    result =[]
    for key, data in users.items():
        if data["role"] in unique_roles:
            result.append(key)
    return sorted(result)

# ищем пользователей с уникальной ролью, которые сегодян не заходили на сайт
def find_unique_role_today(users, active_today):
    seen_once = set()
    duplicates = set()
    # находим уникальные роли
    for key, data in users.items():
        role = data["role"]
        if role in seen_once:
            duplicates.add(role)
        else:
            seen_once.add(role)
    
    unique_roles = seen_once - duplicates
    # выбираем пользователей с этими ролями и НЕ в активных
    result =[]
    for key, data in users.items():
        if data["role"] in unique_roles and key not in active_today:
            result.append(key)
    return sorted(result)

# Ищем, кто не заходил на сайт сегодня
def find_inactive_users(all_users, active_today):
    set1 = set(all_users)
    set2 = set(active_today)
    return sorted(set1-set2)



# Разное
# добавляем ключ в словарь
def update_dict(user_data):
    if not isinstance(user_data, dict):
        return "Ошибка: не словарь"
    user_data["status"] = "active"
    return user_data