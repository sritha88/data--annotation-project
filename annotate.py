# Data Annotation Project
# Sai - Amazon Data Collection Specialist Application
# Automatically annotates Amazon product reviews

import csv
import os

# Sample Amazon product reviews dataset
reviews = [
    {"id": 1, "review": "This product is amazing, works perfectly!"},
    {"id": 2, "review": "Terrible quality, broke after one day."},
    {"id": 3, "review": "Good value for the price, decent product."},
    {"id": 4, "review": "Not what I expected, very disappointed."},
    {"id": 5, "review": "Excellent! Will buy again, highly recommend!"},
    {"id": 6, "review": "Average product, nothing special."},
    {"id": 7, "review": "Worst purchase ever, complete waste of money."},
    {"id": 8, "review": "Highly recommend to everyone, love it!"}
]

# Keywords for auto-annotation
positive_words = ["amazing", "excellent", "love", "recommend", "great", "perfect"]
negative_words = ["terrible", "worst", "disappointed", "waste", "broke", "bad"]

def annotate_review(review_text):
    text = review_text.lower()
    if any(word in text for word in positive_words):
        return "positive"
    elif any(word in text for word in negative_words):
        return "negative"
    else:
        return "neutral"

def annotate_reviews(reviews):
    print("\n==== DATA ANNOTATION PIPELINE ====")
    for item in reviews:
        label = annotate_review(item["review"])
        item["label"] = label
        print(f"Review {item['id']}: {label.upper()} — {item['review'][:50]}")
    return reviews

def save_results(reviews):
    os.makedirs("output", exist_ok=True)
    output_file = "output/annotated_reviews.csv"
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["id", "review", "label"])
        writer.writeheader()
        writer.writerows(reviews)
    print(f"\nResults saved to {output_file}")

# Run the pipeline
annotated = annotate_reviews(reviews)
save_results(annotated)
print("\nAnnotation complete!")