# Ex4.py
import person

if __name__ == "__main__":
    from person import Person
    valtteri = Person("Valtteri", 34)
    kimi = Person("Kimi", 44)

    valtteri.introduce()
    kimi.introduce()

    kimi.celebrate_birthday()

    kimi.introduce()
