from termcolor import colored


class Options:
    population: int
    male_population_percentage: float
    female_population_percentage: float
    male_population_count: int
    female_population_count: int
    max_friends_per_male: int
    max_friends_per_female: int
    male_on_male_friends_percentage: float
    male_on_female_friends_percentage: float
    female_on_male_friends_percentage: float
    female_on_female_friends_percentage: float
    sample_size: int
    iterations_count: int
    unbiased_analysis: bool
    unbiased_crawling: bool


def print_log(options: Options):
    print(
        colored("\nProblem Configurations", "green", attrs=["bold", "underline"])
        + ":\n"
    )
    print(
        colored("Population:\t\t", "black", attrs=["bold"])
        + colored(options.population, "blue")
        + colored(
            f" ({options.male_population_count} Male [{options.male_population_percentage * 100}%] + {options.female_population_count} Female [{options.female_population_percentage * 100}%])",
            attrs=["bold"],
        )
    )
    print(
        colored("Friends/Male:\t\t", "black", attrs=["bold"])
        + colored(f"{options.max_friends_per_male} Max", "blue")
        + colored(
            f" ({options.male_on_male_friends_percentage * 100}% Male + {options.male_on_female_friends_percentage * 100}% Female)",
            attrs=["bold"],
        )
    )
    print(
        colored("Friends/Female:\t\t", "black", attrs=["bold"])
        + colored(f"{options.max_friends_per_female} Max", "blue")
        + colored(
            f" ({options.female_on_male_friends_percentage * 100}% Male + {options.female_on_female_friends_percentage * 100}% Female)",
            attrs=["bold"],
        )
    )
    print(
        colored("Sample Size:\t\t", "black", attrs=["bold"])
        + colored(f"{options.sample_size}", "blue")
    )
    print(
        colored("Unbiased Crawling:\t", "black", attrs=["bold"])
        + colored(
            f"{options.unbiased_crawling}",
            "green" if options.unbiased_crawling else "red",
        )
    )
    print(
        colored("Unbiased Analysis:\t", "black", attrs=["bold"])
        + colored(
            f"{options.unbiased_analysis}",
            "green" if options.unbiased_analysis else "red",
        )
    )
    print(
        colored("Iterations:\t\t", "black", attrs=["bold"])
        + colored(f"{options.iterations_count}", "blue")
    )

    print()


def get_options(options) -> Options:
    obj = Options()
    obj.population = options.population
    obj.male_population_percentage = round(options.male * 1000) / 100000
    obj.female_population_percentage = round((100 - options.male) * 1000) / 100000
    obj.male_population_count = int(options.population * obj.male_population_percentage)
    obj.female_population_count = int(
        options.population * obj.female_population_percentage
    )
    obj.max_friends_per_male = options.maxFriendsPerMale
    obj.max_friends_per_female = options.maxFriendsPerFemale
    obj.male_on_male_friends_percentage = round(options.maleMaleFriends * 1000) / 100000
    obj.male_on_female_friends_percentage = (
        round((100 - options.maleMaleFriends) * 1000) / 100000
    )
    obj.female_on_female_friends_percentage = (
        round(options.femaleFemaleFriends * 1000) / 100000
    )
    obj.female_on_male_friends_percentage = (
        round((100 - options.femaleFemaleFriends) * 1000) / 100000
    )
    obj.sample_size = options.sampleSize
    obj.iterations_count = options.iterations
    obj.unbiased_analysis = options.unbiasedAnalysis
    obj.unbiased_crawling = options.unbiasedCrawling
    return obj
