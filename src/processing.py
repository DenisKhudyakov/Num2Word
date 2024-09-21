from src.dictionary_with_numerals import *


class Num2Word:
    def __init__(self, number: int, gender: str, _case: str) -> None:
        self.number = number
        self.gender = gender
        self._case = _case

    @staticmethod
    def get_case_word(number: int, words: list) -> str:
        """
        Возвращает корректную форму слова в зависимости от числа.
        :param number: число которое нужно обработать
        :param words: массив данных либо миллионы, либо тысячи и тп
        :return: строковое значение массива
        """
        if number % 100 in (11, 12, 13, 14):
            return words[2]  # Родительный падеж множественного числа
        last_digit = number % 10
        if last_digit == 1:
            return words[0]
        elif 2 <= last_digit <= 4:
            return words[1]
        else:
            return words[2]

    @staticmethod
    def number_to_text(number: int, gender: str, _case: str):
        """
        Функция преобразования трехзначного числа в строку
        :param number:
        :param gender:
        :param _case:
        :return:
        """
        result: list = []
        if number >= 100:
            result.append(HUNDREDS[_case][number // 100 - 1])
            number %= 100
        if 10 <= number <= 19:
            result.append(TENS[_case][number - 10])
        else:
            if number >= 20:
                result.append(DOZENS[_case][number // 10 - 2])
                number %= 10
            if number > 0:
                result.append(UNITS[_case][gender][number])
        return " ".join(result)

    def split_number(self) -> tuple:
        """
        Разбиваем число на миллиарды, миллионы, тысячи и единицы
        :return: кортэж из миллиардов, миллионов и тп., если число маленькое будет нуль
        """
        billions_num = self.number // 10**9
        millions_num = (self.number % 10**9) // 10**6
        thousands_num = (self.number % 10**6) // 10**3
        remainder = self.number % 10**3
        return billions_num, millions_num, thousands_num, remainder

    def build_word(self) -> str:
        """
        Функция преобразования большого числа и сборка в строку
        :return: готовое число прописью
        """
        words: list = []
        billions_num, millions_num, thousands_num, remainder = self.split_number()

        if billions_num:
            words.append(
                f"{self.number_to_text(billions_num, 'М', self._case)} {self.get_case_word(billions_num, BILLIONS[self._case])}"
            )

        if millions_num:
            words.append(
                f"{self.number_to_text(millions_num, 'М', self._case)} {self.get_case_word(millions_num, MILLIONS[self._case])}"
            )

        if thousands_num:
            words.append(
                f"{self.number_to_text(thousands_num, 'Ж', self._case)} {self.get_case_word(thousands_num, THOUSANDS[self._case])}"
            )

        if remainder:
            words.append(self.number_to_text(remainder, self.gender, self._case))

        return " ".join(words)
