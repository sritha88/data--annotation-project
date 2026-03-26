 Annotation Guidelines
## Amazon Product Review Sentiment Labeling

*Project:* Data Annotation Pipeline  
*Annotator:* Sai Sritha  
*Version:* 1.0  
*Date:* March 2026

---

## Overview

This document defines the labeling rules used to classify 
Amazon product reviews into three sentiment categories:
positive, negative, and neutral.

The goal is to ensure every review is labeled consistently,
accurately, and in a way that reflects the customer's actual 
experience — not just the words they used.

These guidelines are designed to simulate real-world data 
annotation workflows used in machine learning pipelines.

---

## Categories

### POSITIVE
The reviewer is satisfied with the product. They express 
happiness, recommendation, or praise.

Examples:
- "This product is amazing, works perfectly!"
- "Highly recommend to everyone, love it!"
- "Best purchase I've made this year."

Keywords that often indicate positive:
amazing, excellent, love, recommend, great, perfect, 
fantastic, happy, satisfied, awesome

---

### NEGATIVE
The reviewer is dissatisfied. They express disappointment, 
frustration, or warn others not to buy.

Examples:
- "Terrible quality, broke after one day."
- "Worst purchase ever, complete waste of money."
- "Very disappointed, not as described."

Keywords that often indicate negative:
terrible, worst, disappointed, waste, broke, bad, 
horrible, poor, useless, frustrated

---

### NEUTRAL
The reviewer has a mixed opinion or is simply describing 
the product without strong emotion.

Examples:
- "Good value for the price, decent product."
- "Average product, nothing special."
- "It works fine, does what it says."

---

## Edge Cases

*Mixed sentiment:*
"The product is great but shipping was terrible."
→ Label based on overall product experience
→ NEUTRAL

*Sarcasm:*
"Oh great, broke on day one. Really amazing quality."
→ Read full context
→ NEGATIVE

*Short reviews:*
"Fine." / "OK" / "Meh"
→ NEUTRAL

*Questions:*
"Does this work with iPhone?"
→ Skip — flag as INVALID

---

## Quality Standards

- Every review must have exactly one label
- Labels must be lowercase: positive / negative / neutral
- No blank labels allowed
- Re-read any review you are unsure about
- If still unsure, label as neutral

---

## Annotator Instructions

- Read each review carefully before assigning a label
- Do not rely only on keywords — understand full context
- Follow guidelines consistently across all reviews
- If unsure, refer back to examples and edge cases

---

## Consistency Check

Before submitting labeled data:
- Check for duplicate reviews
- Check for missing labels
- Spot check 10% of labels for accuracy
- Flag any mislabeled reviews for review
