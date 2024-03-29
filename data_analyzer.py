import sys

# if not done like this, auto formatter changes
# the order of the lines, which matters
if True:
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "capstone_server.settings")
    from django import setup
    setup()
    from core.models import Answer


class MyFunctions:
    def __init__(self):
        self.output = []

    def my_prnt(self, line="", *args, **kwargs):
        self.output.append(str(line).strip("\n "))

    def my_input(self, *args, **kwargs):
        return input()

    def my_int(self, x):
        return int(x)

    def get_output(self):
        return "\n".join(self.output).strip("\n ")


excluded = list(map(lambda x: x.strip('\r\n '),
                open('exclude.txt', 'r').readlines()))

pretest_input = """5 4 2
XXX.
X..X
XXX.
X..X
XXX."""

pretest_output = """XXXXXX..
XXXXXX..
XX....XX
XX....XX
XXXXXX..
XXXXXX..
XX....XX
XX....XX
XXXXXX..
XXXXXX.."""

posttest_input = """5 3
1
6
4
3
1"""

posttest_output = "4"

# pretest requirements
# exactly two input functions
# exactly one print statement function
# at least one for loop
# at least one int function
# error-free
# outputs the correct answer
# at least one + operator

# posttest requirements
# exactly two input functions
# exactly one print function
# at least one for loop
# at least one int function
# error free
# correct answer
# at least one comparison operator


def get_pretest_data():
    pretest_answers = [answer for answer in Answer.objects.all().filter(
        question=1) if str(answer) not in excluded]
    requirements = 7
    pretest_data = {}
    for answer in pretest_answers:
        # 9999 is test unit
        # 5243 uses sys.argv, which breaks this program
        # they did not complete both tests either way...
        if answer.unit.key in ['5243', '9999']:
            continue

        code = format_code(answer.content)
        score = 0

        if code.count("my_input") == 2:
            score += 100/requirements

        if code.count("my_prnt") == 1:
            score += 100/requirements

        if code.count("for ") >= 1:
            score += 100/requirements

        if code.count("my_int") >= 1 or code.count("my_int,") >= 1:
            score += 100/requirements

        if code.count("+") >= 1:
            score += 100/requirements

        try:
            output = execute_code(code, pretest_input)

        except Exception as e:
            pass

        else:
            score += 100/requirements
            if output == pretest_output:
                score += 100/requirements

        pretest_data[answer.unit.key] = {'type': answer.unit.type,
                                         "score": score, "time_spent": answer.time_spent}

    return pretest_data


def get_posttest_data():
    posttest_answers = [answer for answer in Answer.objects.all().filter(
        question=6) if str(answer) not in excluded]
    requirements = 7
    posttest_data = {}
    for answer in posttest_answers:
        if answer.unit.key in ['9999']:
            continue

        code = format_code(answer.content)

        score = 0
        if code.count("my_input") == 2:
            score += 100/requirements

        if code.count("my_prnt") == 1:
            score += 100/requirements

        if code.count("my_int") >= 2 or code.count("my_int,") >= 2:
            score += 100/requirements

        if code.count("for ") >= 1:
            score += 100/requirements

        if any([comparator in code for comparator in ["<", ">", "<=", ">="]]):
            score += 100/requirements

        try:
            output = execute_code(code, posttest_input)

        except Exception as e:
            pass

        else:
            score += 100/requirements
            if output == posttest_output:
                score += 100/requirements

        posttest_data[answer.unit.key] = {'type': answer.unit.type,
                                          "score": score, "time_spent": answer.time_spent}

    return posttest_data


def get_excluded_data():
    excluded_data = [answer for answer in Answer.objects.all()
                     if str(answer) in set(excluded)]
    return "\n".join(set([f"{answer}*{answer.time_spent}*{len(answer.content)}" for answer in set(excluded_data)]))


def format_code(code):
    lines = code.split("\n")
    new_lines = []
    for line in lines:
        new_line = line
        if any([word in line for word in ["import", 'clear']]):
            continue
        new_lines.append(new_line)
    code = "\n".join(new_lines)

    code = code.replace("print", "my_functions.my_prnt")
    code = code.replace("input", "my_functions.my_input")
    code = code.replace("int", "my_functions.my_int")
    code = code.replace("int,", "my_functions.my_int,")

    return code


def execute_code(code, inp):
    my_functions = MyFunctions()

    with open("test_file.txt", "w") as file:
        file.write(inp)

    with open("test_file.txt", "r") as file:
        sys.stdin = file
        exec(code, {'my_functions': my_functions})
    return my_functions.get_output()


# pre_data = get_pretest_data()
# post_data = get_posttest_data()
# print(pre_data)
# print(post_data)
print(get_excluded_data())
