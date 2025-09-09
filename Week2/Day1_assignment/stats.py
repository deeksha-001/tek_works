import statistics

def stats(score):
    mean = statistics.mean(score)
    median = statistics.median(score)
    variance = statistics.variance(score)

    print("Mean:", round(mean,2))
    print("Median:", median)
    print("Variance:", round(variance,2))

score = list(map(int, input("Enter the elements: ").split()))
stats(score)