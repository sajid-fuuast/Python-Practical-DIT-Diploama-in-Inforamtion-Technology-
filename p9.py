#9.	Write a script to takes score from a user between (1 and 100)
# and display its grade according to score. (Score: 1-50 Grade: Average)
# (Score: 51-70 Grade: Good) (Score: 71-100 Grade: Excellent).

score = int(input("Enter the score (between 1 and 100): "))

grade="Invalid score. Please enter a score between 1 and 100."

if 1 <= score <= 50:
        grade = "Average"
if 51 <= score <= 70:
        grade = "Good"
if 71 <= score <= 100:
        grade = "Excellent"

print("Grade =", grade)
