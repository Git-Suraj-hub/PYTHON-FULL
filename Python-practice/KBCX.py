questions = {
    "What is the capital of India": "Delhi",
    "What is the National Bird of India": "Peacock",
    "What is the National Animal of India": "Tiger",
    "How many states are there in India": "28",
}
Options = [
    ["Delhi", "Kolkata", "Mumbai", "Chennai"],
    ["Pigeon", "Crow", "humming bird", "Peacock"],
    ["Elephant", "Lion", "Tiger", "Liger"],
    ["9", "28", "31", "23"],
]
# print(len(questions))
l = len(questions)
i = 0
for key, value in questions.items():
    print(key)
    print(Options[i])
    ans = int(input("enter Your Option : "))
    i = i + 1
    if value == Options[i-1][ans-1]:
        print("Correct Ans ")
        print("You Won The 10000 rs")
        continue
    else:
        print("You are out")
        break