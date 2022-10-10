def get_salary_from_api(name):
    return 500
    # raise Exception()


def get_total_salary(name, bonus):
    if bonus < 0:
        raise ValueError("low_bonus")

    salary = get_salary_from_api(name)
    return salary + bonus


if __name__ == "__main__":
    sal = get_total_salary("example", 200)
    print(f"{sal=}")
