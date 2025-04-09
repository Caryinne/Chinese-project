def get_characters_for_table():
    characters = []
    with open("./data/characters.csv", "r", encoding="utf-8") as f:
        cnt = 1
        for line in f.readlines()[1:]:
            character, pinyin, tone, meaning, source = line.split(";")
            characters.append([cnt, character, pinyin, tone, meaning])
            cnt += 1
    return characters


def write_character(new_character, new_pinyin, new_tone, new_meaning):
    new_character_line = f"{new_character};{new_pinyin};{new_tone};{new_meaning};user"
    with open("./data/characters.csv", "r", encoding="utf-8") as f:
        existing_characters = [l.strip("\n") for l in f.readlines()]
        title = existing_characters[0]
        old_characters = existing_characters[1:]
    characters_sorted = old_characters + [new_character_line]
    characters_sorted.sort()
    new_characters = [title] + characters_sorted
    with open("./data/characters.csv", "w", encoding="utf-8") as f:
        f.write("\n".join(new_characters))


def get_characters_stats():
    db_characters = 0
    user_characters = 0
    meaning_len = []
    with open("./data/characters.csv", "r", encoding="utf-8") as f:
        for line in f.readlines()[1:]:
            character, pinyin, tone, meaning, added_by = line.split(";")
            characters = meaning.split()
            meaning_len.append(len(characters))
            if "user" in added_by:
                user_characters += 1
            elif "db" in added_by:
                db_characters += 1
    stats = {
        "characters_all": db_characters + user_characters,
        "characters_own": db_characters,
        "characters_added": user_characters,
        "characters_avg": sum(meaning_len)/len(meaning_len),
        "characters_max": max(meaning_len),
        "characters_min": min(meaning_len)
    }
    return stats
