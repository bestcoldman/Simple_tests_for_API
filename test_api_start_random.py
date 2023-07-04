import requests

class Test_new_joke():
    """Создание новой шутки"""
    # def test_create_new_random_joke(self):
    #     """Создание случайной шутки"""
    #     url = "https://api.chucknorris.io/jokes/random"
    #     result = requests.get(url)
    #     print("Status code is: " + str(result.status_code))
    #     if result.status_code == 200:
    #         print("Succesful")
    #     else:
    #         print("Failed in status code")
    #     assert 200 == result.status_code
    #     result.encoding = 'utf-8'
    #     print(result.text)
    #     check = result.json()
    #     # check_info = check.get("categories")
    #     # print(check_info)
    #     # assert check_info == []
    #     # print("Категория верная")
    #     check_info_value = check.get("value")
    #     print(check_info_value)
    #     name = "Chuck"
    #     if name in check_info_value:
    #         print("Joke is valid")
    #     else:
    #         print("Joke is unvalid")

    def test_create_new_random_categories_joke(self):
        """Создание случайной шутки на определенную тему"""

        category = "sport"
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        result = requests.get(url)
        print("Status code is: " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Succesful")
        else:
            print("Failed in status code")
        result.encoding = 'utf-8'
        print(result.text)
        check = result.json()
        check_info = check.get("categories")
        print(check_info)
        assert check_info == ["sport"]
        print("Категория верная")
        # check_info_value = check.get("value")
        # print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print("Joke is valid")
        # else:
        #     print("Joke is unvalid")

sport_joke = Test_new_joke()
sport_joke.test_create_new_random_categories_joke()
