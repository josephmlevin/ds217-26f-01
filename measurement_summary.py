measurements = [18, 21, 24, 19]
review_threshold_text = "20"

# Replace this scaffold output with your calculation, loop, decision, and summary.
review_threshold = int(review_threshold_text)

total, review_count = 0, 0
for measurement in measurements:
    total += measurement
    if measurement >= review_threshold:
        review_count += 1
        print("Measurement:", measurement, "review")
    else:
        print("Measurement:", measurement, "within range")

the_mean = total / len(measurements)
print("Count:", len(measurements))
print("Total:", total)
print("Mean:", the_mean)
print("Review count:", review_count)

