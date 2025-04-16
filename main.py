def count_vowels(word: str) -> int:
    """Повертає кількість голосних букв у слові (укр. та англ.)."""
    vowels = "aeiouаеєиіїоуюяAEIOUАЕЄИІЇОУЮЯ"
    return sum(1 for char in word if char in vowels)

def main():
    try:
        word = input("Введіть слово: ")
        result = count_vowels(word)
        print("Кількість голосних букв:", result)
    except Exception as e:
        print("Сталася помилка:", e)

if __name__ == "__main__":
    main()
