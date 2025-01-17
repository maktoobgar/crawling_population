# Crawling then Analyzing on population of men & women

## Setup

First create a python virtual environment:

```bash
python3 -m venv env
source ./env/bin/activate
```

Install the requirements for the project:

```bash
pip install -r requirement.txt
```

## Usage

Then run the project, first make sure you activated the environment:

```bash
source ./env/bin/activate
```

Run the project with default parameters:

```bash
python main.py
```

To get help about command options, run:

```bash
python main.py -h
```

## What are Unbiased Analysis and Unbiased Crawling?

We crawl through the data and then determine the results with applying an analysis.
Two analysis and two crawling methods are used here:

1. Default Crawling: Simple Random Walk
2. Unbiased Crawling: Uses Metropolis-Hastings Random Walk (MHRW)
3. Default Analysis: Accuracy method to determine results
4. Unbiased Analysis: Uses Re-Weighted Random Walk (RWRW)

## Different Cases

### 1. More Men but Dominant Women

```output
Population:                     100000 (80000 Male [80.0%] + 20000 Female [20.0%])
Friends/Male:                   100 Max (20.0% Male + 80.0% Female)
Friends/Female:                 100 Max (20.0% Male + 80.0% Female)
Friendship Standard Deviation:  20.0%
```

#### 1.1. **First Attempt** with random walk + accuracy analysis

```output
Sample Size:                    1000
Unbiased Crawling:              False
Unbiased Analysis:              False
Iterations:                     50
```

Command to generate the problem and solve:

```bash
python main.py --male=80 --male-male-percentage=20 --female-female-percentage=80
```

Results:

```output
Males Percentage: 50.58% - Females Percentage: 49.42%
```

#### 1.2. **Second Attempt** with Metropolis-Hastings random walk + accuracy analysis

```output
Sample Size:                    1000
Unbiased Crawling:              **True**
Unbiased Analysis:              False
Iterations:                     50
```

Command to generate the problem and solve:

```bash
python main.py --male=80 --male-male-percentage=20 --female-female-percentage=80 --unbiased-crawling
```

Results:

```output
Males Percentage: 61.23% - Females Percentage: 38.77%
```

#### 1.3. **Third Attempt** with random walk + Re-Weighted analysis

```output
Sample Size:                    1000
Unbiased Crawling:              False
Unbiased Analysis:              **True**
Iterations:                     50
```

Command to generate the problem and solve:

```bash
python main.py --male=80 --male-male-percentage=20 --female-female-percentage=80 --unbiased-analysis
```

**BEST Results:**

```output
Males Percentage: 80.42% - Females Percentage: 19.58%
```

### 2. More Women and Dominant Women

```output
Population:                     100000 (20000 Male [20.0%] + 80000 Female [80.0%])
Friends/Male:                   100 Max (40.0% Male + 60.0% Female)
Friends/Female:                 100 Max (40.0% Male + 60.0% Female)
Friendship Standard Deviation:  20.0%
```

#### 2.1. **First Attempt** with random walk + accuracy analysis

```output
Sample Size:                    1000
Unbiased Crawling:              False
Unbiased Analysis:              False
Iterations:                     50
```

Command to generate the problem and solve:

```bash
python main.py --male=20 --male-male-percentage=40 --female-female-percentage=60
```

Results:

```output
Males Percentage: 29.91% - Females Percentage: 70.09%
```

#### 2.2. **Second Attempt** with Metropolis-Hastings random walk + accuracy analysis

```output
Sample Size:                    1000
Unbiased Crawling:              **True**
Unbiased Analysis:              False
Iterations:                     50
```

Command to generate the problem and solve:

```bash
python main.py --male=20 --male-male-percentage=40 --female-female-percentage=60
```

Results:

```output
Males Percentage: 24.23% - Females Percentage: 75.77%
```

#### 2.3. **Third Attempt** with random walk + Re-Weighted analysis

```output
Sample Size:                    1000
Unbiased Crawling:              False
Unbiased Analysis:              **True**
Iterations:                     50
```

Command to generate the problem and solve:

```bash
python main.py --male=20 --male-male-percentage=40 --female-female-percentage=60 --unbiased-analysis
```

**BEST Results:**

```output
Males Percentage: 20.080000000000002% - Females Percentage: 79.92%
```
