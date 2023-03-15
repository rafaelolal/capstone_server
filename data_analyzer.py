import random
import datetime

# if I do not do it like this, my auto formatter changes
# the order of the lines, which matters
if True:
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "capstone_server.settings")
    from django import setup
    setup()
    from django.utils import timezone
    from core.models import Answer

# solution
# m, n, k = map(int, input().split())
# ans = ""
# for _ in range(m):
# 	row = input()
# 	new_row = ""
# 	for char in row:
# 		new_row += char * k
# 	ans += (new_row + "\n" * k)

# print(ans[:-1])
#

# requirements
# exactly two input functions
# at least two for loops
# at most one print statement that prints a variable
# at least one + operator
# at least one int function
pretest_data = {}
for answer in Answer.objects.all():
    score = 0
    if answer.content.count("input(") == 2:
        score += 20
    if answer.content.count("for ") >= 2:
        score += 20
    if answer.content.count("print(") == 1:
        i = answer.content.find("print(")
        if answer.content[i+6].isalpha():
            score += 20
    if answer.content.count("+") >= 1:
        score += 20
    if answer.content.count("int(") >= 1 or answer.content.count("int,") >= 1:
        score += 20

    pretest_data[answer.unit.key] = {
        "score": score, "time_spent": answer.time_spent}

print(pretest_data)
