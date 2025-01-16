from termcolor import colored


class Options:
    population: int
    male_population_percentage: float
    female_population_percentage: float
    male_population_count: int
    female_population_count: int
    friends_per_person: int
    male_friends_percentage: float
    female_friends_percentage: float
    male_friends_count: int
    female_friends_count: int
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
        colored("Friends/Person:\t\t", "black", attrs=["bold"])
        + colored(f"{options.friends_per_person}", "blue")
        + colored(
            f" ({options.male_friends_count} Male [{options.male_friends_percentage * 100}%] + {options.female_friends_count} Female [{options.female_friends_percentage * 100}%])",
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
    obj.male_population_percentage = options.male / 100
    obj.female_population_percentage = 1 - options.male / 100
    obj.male_population_count = int(options.population * obj.male_population_percentage)
    obj.female_population_count = int(
        options.population * obj.female_population_percentage
    )
    obj.friends_per_person = options.friendsPerPerson
    obj.male_friends_percentage = options.maleFriends / 100
    obj.female_friends_percentage = 1 - options.maleFriends / 100
    obj.male_friends_count = int(obj.friends_per_person * obj.male_friends_percentage)
    obj.female_friends_count = int(
        obj.friends_per_person * obj.female_friends_percentage
    )
    obj.sample_size = options.sampleSize
    obj.iterations_count = options.iterations
    obj.unbiased_analysis = options.unbiasedAnalysis
    obj.unbiased_crawling = options.unbiasedCrawling
    return obj
