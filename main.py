from src.processing import Num2Word


if __name__ == "__main__":
    number = Num2Word(945336128456, "М", "Т")
    print(number.build_word())
