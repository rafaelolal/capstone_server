import random
import datetime
import sys
# if I do not do it like this, my auto formatter changes
# the order of the lines, which matters
if True:
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "capstone_server.settings")
    from django import setup
    setup()
    from django.utils import timezone
    from core.models import Answer

class MyFunctions:
    def __init__(self):
        self.output = []

    def my_print(self, line):
        self.output.append(str(line).strip("\n "))

    def my_input(self, *args, **kwargs):
        return input()

    def get_output(self):
        return "\n".join(self.output).strip("\n ")

pretest_inp = """5 4 2
XXX.
X..X
XXX.
X..X
XXX."""

pretest_answer = """XXXXXX..
XXXXXX..
XX....XX
XX....XX
XXXXXX..
XXXXXX..
XX....XX
XX....XX
XXXXXX..
XXXXXX.."""

# requirements
# exactly two input functions
# at least two for loops
# at most one print statement that prints a variable
# at least one + operator
# at least one int function
# error-free
# outputs the correct answer
def get_pretest_data():
    requirements = 7
    pretest_data = {}
    for answer in Answer.objects.all().filter(question=1):
        if answer.unit.key in ['5243', '1041', "9999"]:
            continue

        score = 0

        if answer.content.count("input(") == 2:
            score += 100/requirements

        if answer.content.count("for ") >= 2:
            score += 100/requirements

        if answer.content.count("print(") == 1:
            i = answer.content.find("print(")
            if answer.content[i+6].isalpha():
                score += 100/requirements

        if answer.content.count("+") >= 1:
            score += 100/requirements

        if answer.content.count("int(") >= 1 or answer.content.count("int,") >= 1:
            score += 100/requirements

        try:
            output = execute_code(answer.content, pretest_inp)
            score += 100/requirements

            if output == pretest_answer:
                score += 100/requirements

        except Exception as e:
            pass

        pretest_data[answer.unit.key] = {'type': answer.unit.type,
            "score": score, "time_spent": answer.time_spent}

    return pretest_data

posttest_inp = """5 3
1
6
4
3
1"""
posttest_output = "4"

# requirements
# exactly two input functions
# exactly one print function
# at least one int function
# at least one for loop
# at least one comparison operator
# error free
# correct answer
def get_posttest_data():
    requirements = 7
    posttest_data = {}
    for answer in Answer.objects.all().filter(question=6):
        if answer.unit.key in ["9999"]:
            continue

        score = 0
        if answer.content.count("input(") == 2:
            score += 100/requirements

        if answer.content.count("int(") >= 2 or answer.content.count("int,") >= 2:
            score += 100/requirements

        if answer.content.count("for ") >= 1:
            score += 100/requirements

        if any([comparator in answer.content for comparator in ["<", ">", "<=", ">="]]):
            score += 100/requirements

        if answer.content.count("print(") == 1:
            score += 100/requirements

        try:
            output = execute_code(answer.content, posttest_inp)
            score += 100/requirements

            if output == posttest_output:
                score += 100/requirements

        except Exception as e:
            pass

        posttest_data[answer.unit.key] = {'type': answer.unit.type,
            "score": score, "time_spent": answer.time_spent}

    return posttest_data

def execute_code(code, inp):
    my_functions = MyFunctions()
    code = format_code(code)
    
    with open("test_file.txt", "w") as file:
        file.write(inp)
    
    with open("test_file.txt", "r") as file:
        sys.stdin = file
        exec(code)
    
    return my_functions.get_output()

def format_code(code):
    code = code.replace("print(", "my_functions.my_print(")
    code = code.replace("input(", "my_functions.my_input(")
    lines = code.split("\n")
    new_lines = []
    for line in lines:
        new_line = line
        if any([word in line for word in ["import", 'clear']]):
            continue
        new_lines.append(new_line)
    code = "\n".join(new_lines)
    return code

pre_data = get_pretest_data()
post_data = get_posttest_data()
print(pre_data)
print(post_data)