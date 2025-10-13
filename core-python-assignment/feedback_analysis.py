def positive_percentage(ratings):
    if not ratings:
        return 0
    positives = [r for r in ratings if r >= 4]
    return round(len(positives) / len(ratings) * 100, 2)

ratings = [5, 4, 3, 5, 2, 4, 1, 5]
print("Positive Feedback:", positive_percentage(ratings), "%")
