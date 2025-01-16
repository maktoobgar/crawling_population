import optparse
from general import print_log, get_options, Options
from typing import List
import random
import uuid


class Person:
    id: str = ""
    # 0 male, 1 female
    gender: bool = False
    # An instance of friends class
    friends = None

    def __init__(self, gender: bool):
        self.id = uuid.uuid4().int
        self.gender = gender
        self.friends = Friends()

    def __repr__(self):
        return f'ID: {self.id} - {"Female" if self.gender else "Male"} - Friends Stats: {self.friends}'

    def __len__(self):
        return len(self.all)


class Results:
    males_percentages: List[float] = []
    females_percentages: List[float] = []
    unbiased_analysis: bool = False
    total_percentages_calculated: bool = False
    total_males_percentages: int = 0
    total_females_percentages: int = 0

    def __init__(self, unbiased_analysis: bool = False):
        self.females_percentages = []
        self.males_percentages = []
        self.unbiased_analysis = False
        self.total_percentages_calculated = False
        self.total_males_percentages = 0
        self.total_females_percentages = 0

    def add_result(self, males: List[Person], females: List[Person]):
        all_count = len(males) + len(females)
        if self.unbiased_analysis:
            pass
        else:
            males_percentage = len(males) / all_count
            females_percentage = len(females) / all_count
            self.males_percentages.append(males_percentage)
            self.females_percentages.append(females_percentage)

    def calculate_results(self):
        if len(self.males_percentages) == 0 or len(self.females_percentages) == 0:
            return

        males_percentages = 0
        for i in range(len(self.males_percentages)):
            males_percentages += self.males_percentages[i]
        females_percentages = 0
        for i in range(len(self.females_percentages)):
            females_percentages += self.females_percentages[i]
        self.total_males_percentages = males_percentages / len(self.males_percentages)
        self.total_females_percentages = females_percentages / len(
            self.females_percentages
        )
        self.total_percentages_calculated = True

    def __repr__(self):
        if not self.total_percentages_calculated:
            self.calculate_results()
        return f"Males Percentage: {self.total_males_percentages * 100}% - Females Percentage: {self.total_females_percentages * 100}%"


class Friends:
    males: List[Person] = []
    females: List[Person] = []
    all: List[Person] = []
    probabilities: List[float] = []

    def __init__(self):
        self.males = []
        self.females = []
        self.all = []
        self.probabilities = []

    def add_friend(self, person: Person):
        if person.gender:
            self.females.append(person)
        else:
            self.males.append(person)
        self.all.append(person)

    def shuffle(self, seed: float = 42):
        random.seed(seed)
        random.shuffle(self.all)
        random.shuffle(self.males)
        random.shuffle(self.females)

    def __repr__(self):
        return f"All: {len(self.all)} (Males: {len(self.males)} [{len(self.males)/len(self.all) * 100 if len(self.males) > 0 else 0}%], Females: {len(self.females)} [{len(self.females)/len(self.all) * 100 if len(self.males) > 0 else 0}%])"

    def __len__(self):
        return len(self.all)


class Problem:
    all: List[Person] = []
    males: List[Person] = []
    females: List[Person] = []

    def add_person(self, person: Person):
        if person.gender:
            self.females.append(person)
        else:
            self.males.append(person)
        self.all.append(person)

    def shuffle(self, seed: float = 42):
        random.seed(seed)
        random.shuffle(self.all)
        random.shuffle(self.males)
        random.shuffle(self.females)

    def pick_random_male(self, not_included: Person) -> Person:
        while True:
            friend = random.choice(self.males)
            if friend.id != not_included.id:
                return friend

    def pick_random_female(self, not_included: Person) -> Person:
        while True:
            friend = random.choice(self.females)
            if friend.id != not_included.id:
                return friend

    def get_random_starting_point(self) -> Person:
        return random.choice(self.all)

    def __repr__(self):
        return f"All: {len(self.all)} (Males: {len(self.males)} [{len(self.males)/len(self.all) * 100 if len(self.males) > 0 else 0}%], Females: {len(self.females)} [{len(self.females)/len(self.all) * 100 if len(self.males) > 0 else 0}%])"

    def __len__(self):
        return len(self.all)


def generate_problem(options: Options) -> Problem:
    problem = Problem()
    for _ in range(options.male_population_count):
        problem.add_person(Person(False))
    for _ in range(options.female_population_count):
        problem.add_person(Person(True))
    problem.shuffle()
    for person in problem.all:
        male_friends_count = (
            options.male_friends_count
            if person.gender
            else options.male_friends_count - 1
        )
        female_friends_count = (
            options.female_friends_count - 1
            if person.gender
            else options.female_friends_count
        )

        for _ in range(male_friends_count):
            person.friends.add_friend(problem.pick_random_male(person))
        for _ in range(female_friends_count):
            person.friends.add_friend(problem.pick_random_female(person))
        person.friends.add_friend(person)
        person.friends.shuffle()
    return problem


def _crawl(person: Person, options: Options, problem: Problem) -> List[Person]:
    # Calculate the probabilities of each friend to get selected
    person.friends.probabilities = []
    for i in range(len(person.friends.all)):
        if options.unbiased_crawling:
            pass
        else:
            person.friends.probabilities.append(1.0 / len(person.friends.all))
    choices = random.choices(
        person.friends.all,
        weights=person.friends.probabilities,
        k=len(person.friends.all),
    )
    return list(set(choices))


def crawl(options: Options, problem: Problem) -> Results:
    results = Results(options.unbiased_analysis)
    person = problem.get_random_starting_point()
    crawled_people: List[Person] = []
    to_crawl: List[Person] = [person]

    random.seed(42)
    for i in range(len(to_crawl)):
        to_crawl.append(_crawl(to_crawl[i], options, problem))


def main():
    parser = optparse.OptionParser(
        usage="main.py [--population=BIG_NUMBER|--male=PERCENTAGE|--friends-per-person=NUMBER|--male-friends=PERCENTAGE|--sample-size=NUMBER|--iterations=BIG_NUMBER|--unbiased-crawling|--unbiased-analysis]",
        description="simulates the male and female percentages and analyses the population with taking multiple samples and getting a converged answer out of it.",
    )
    parser.add_option(
        "--population",
        dest="population",
        type=int,
        default=100000,
        help="sets the population count, default 100000",
    )
    parser.add_option(
        "--male",
        dest="male",
        type=float,
        default=50,
        help="sets the male's population count, default 50",
    )
    parser.add_option(
        "--friends-per-person",
        dest="friendsPerPerson",
        type=int,
        default=10,
        help="sets the number of friends each person normally has",
    )
    parser.add_option(
        "--male-friends",
        dest="maleFriends",
        type=float,
        default=50,
        help="sets the male's favoritism friendship in population, default 50",
    )
    parser.add_option(
        "--sample-size",
        dest="sampleSize",
        type=int,
        default=1000,
        help="sets the sample size, default 1000",
    )
    parser.add_option(
        "--iterations",
        dest="iterations",
        type=int,
        default=1000,
        help="sets the count of how many times to take samples to reach a conclusion, default 1000",
    )
    parser.add_option(
        "--unbiased-crawling",
        action="store_true",
        dest="unbiasedCrawling",
        help="does crawling in an unbiased way",
        default=False,
    )
    parser.add_option(
        "--unbiased-analysis",
        action="store_true",
        dest="unbiasedAnalysis",
        help="does analysis in an unbiased way",
        default=False,
    )

    (options, args) = parser.parse_args()

    options = get_options(options)
    print_log(options)

    problem = generate_problem(options)
    results = crawl(options, problem)


if __name__ == "__main__":
    main()
