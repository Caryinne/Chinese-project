from django.shortcuts import render
from django.core.cache import cache
from . import words_work
from . import characters_work

def index(request):
    return render(request, "index.html")


def words_list(request):
    words = words_work.get_words_for_table()
    return render(request, "word_list.html", context={"words": words})


def add_word(request):
    return render(request, "word_add.html")


def send_word(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_word = request.POST.get("new_word", "")
        new_transcription = request.POST.get("new_transcription", "").replace(";", ",")
        new_translation = request.POST.get("new_translation", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_transcription) == 0:
            context["success"] = False
            context["comment"] = "Транскрипция должна быть не пустой"
        elif len(new_translation) == 0:
            context["success"] = False
            context["comment"] = "Перевод должен быть не пустым"
        elif len(new_word) == 0:
            context["success"] = False
            context["comment"] = "Слово должно быть не пустым"
        else:
            context["success"] = True
            context["comment"] = "Ваше слово принято"
            words_work.write_word(new_word, new_transcription, new_translation)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        return add_word(request)

def characters_list(request):
    characters = characters_work.get_characters_for_table()
    return render(request, "character_list.html", context={"characters": characters})


def add_character(request):
    return render(request, "character_add.html")


def send_character(request):
    if request.method == "POST":
        cache.clear()
        user_name = request.POST.get("name")
        new_character = request.POST.get("new_character", "")
        new_pinyin = request.POST.get("new_pinyin", "").replace(";", ",")
        new_tone = request.POST.get("new_tone", "").replace(";", ",")
        new_meaning = request.POST.get("new_meaning", "").replace(";", ",")
        context = {"user": user_name}
        if len(new_pinyin) == 0:
            context["success"] = False
            context["comment"] = "Пиньинь должен быть не пустым"
        elif len(new_tone) == 0:
            context["success"] = False
            context["comment"] = "Тон должен быть не пустым"
        elif len(new_meaning) == 0:
            context["success"] = False
            context["comment"] = "Значение иероглифа должно быть не пустым"
        elif len(new_meaning) == 0:
            context["success"] = False
            context["comment"] = "Значение иероглифа должно быть не пустым"
        elif character_value < 1 or character_value > 4:
            context["success"] = False
            context["comment"] = "Тон иероглифа должен быть представлен целым числом от 1 до 4"
        else:
            context["success"] = True
            context["comment"] = "Ваш иероглиф принят"
            characters_work.write_character(new_character, new_pinyin, new_tone, new_meaning)
        if context["success"]:
            context["success-title"] = ""
        return render(request, "term_request.html", context)
    else:
        return add_word(request)

def show_stats(request):
    stats = words_work.get_words_stats()
    return render(request, "stats.html", stats)
