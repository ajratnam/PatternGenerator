import re
import string
import sys
from functools import wraps, partial
from itertools import count


def to_int(value):
    if value == "True":
        return 1
    if value == "False":
        return 0
    return int(value)


def line_dissector(pattern_seperator, dissector_function=None):
    if dissector_function is None:
        return partial(line_dissector, pattern_seperator)

    @wraps(dissector_function)
    def wrapped_line_dissector(instance, *abstract_line):
        abstract_line = abstract_line[0]
        dissected_abstract_line = pattern_seperator.split(abstract_line)
        if len(dissected_abstract_line) < 2:
            return abstract_line
        for line_position, line_value in enumerate(dissected_abstract_line[1::2]):
            dissected_abstract_line[2 * line_position + 1] = dissector_function(instance, line_value)
        return ''.join(dissected_abstract_line)

    return wrapped_line_dissector


seperator_pattern = re.compile(r'\[(.*?)],([^,]*)')
replace_stack_pattern = re.compile('(!+)')
letter_converter_pattern = re.compile(r'\((.*?)\)')
evaluator_pattern = re.compile(r'{(.*?)}')

name_regex = re.compile(r'(.*?):(.*)')


class ComplexPatternGenerator:
    _count = count(1)
    _loop_stack = []

    def __init__(self, justify_size=False, auto_index=False):
        self.generated_patterns = {}
        self._sizes = {}

        self.justify_size = justify_size
        self.auto_index = auto_index

    def generate(self, external_pattern, pattern_name=None, _internal_call=False):
        if not _internal_call:
            if pattern_name == "_CURRENT":
                raise ValueError("The pattern name _CURRENT is reserved for internal use")
            parsed_pattern = seperator_pattern.findall(external_pattern)
            self.generated_patterns["_CURRENT"] = ""
        else:
            sliced_external_pattern = external_pattern.split(',')
            parsed_pattern = list(zip(sliced_external_pattern[::2], sliced_external_pattern[1::2]))

        if not parsed_pattern:
            loop_value = self.replace_stack(external_pattern)
            evaluated_value = self.evaluate_values(loop_value)
            self.generated_patterns["_CURRENT"] += self.replace_letters(evaluated_value)
            return

        for abstract_line, loop_condition in parsed_pattern:
            loop_condition = self.replace_stack(loop_condition)
            loop_substituted = self.evaluate_values(loop_condition)
            stack_index = len(self._loop_stack)
            self._loop_stack.append(0)
            if '..' in loop_substituted:
                loop_bounds = loop_substituted.split('..')
                loop_bound_list = []
                for index, bound in enumerate(loop_bounds[:-1]):
                    loop_start, loop_end = to_int(bound.rstrip("$")), to_int(loop_bounds[index + 1].rstrip("$"))
                    loop_step = 1 if loop_end > loop_start else -1
                    loop_start -= bound.endswith("$")
                    loop_bound_list.append((loop_start, loop_end, loop_step))
            else:
                loop_bound_list = [(1, to_int(loop_substituted), 1)]
            for loop_start, loop_end, loop_step in loop_bound_list:
                for current_index in range(loop_start, loop_end + loop_step, loop_step):
                    self._loop_stack[stack_index] = current_index
                    self.generate(abstract_line, pattern_name=pattern_name, _internal_call=True)
            del self._loop_stack[stack_index]
        if _internal_call:
            self.generated_patterns["_CURRENT"] += "\n"
        else:
            if pattern_name is None:
                pattern_name = f"Pattern {next(self._count)}"
            elif self.auto_index:
                pattern_name = f"{next(self._count)}. {pattern_name}"
            generated_pattern = self.generated_patterns["_CURRENT"].splitlines()
            generated_pattern = list(map(str.rstrip, generated_pattern))
            self._sizes[pattern_name] = max(map(len, generated_pattern))
            generated_pattern = "\n".join(generated_pattern)
            self.generated_patterns[pattern_name] = generated_pattern
            del self.generated_patterns["_CURRENT"]
            return generated_pattern

    def print(self, pattern_name):
        pattern = self.generated_patterns.get(pattern_name)
        if pattern is None:
            raise ValueError(f"No pattern named {pattern_name}")
        local_max_length = max_length = self._sizes[pattern_name]
        max_length = max(max_length, len(pattern_name))
        if self.justify_size:
            max_length = max([*self._sizes.values(), *map(len, self._sizes)])
        print("╭" + "─" * max_length + "╮")
        print("│" + pattern_name.center(max_length) + "│")
        print("├" + "─" * max_length + "┤")
        for line in pattern.splitlines():
            if self.justify_size:
                print("│" + line.ljust(local_max_length).center(max_length) + "│")
            else:
                print("│"+line.ljust(max_length)+"│")
        print("╰" + "─" * max_length + "╯")

    def print_all(self):
        for pattern in self.generated_patterns:
            self.print(pattern)

    @line_dissector(replace_stack_pattern)
    def replace_stack(self, stack_history):
        return str(self._loop_stack[-len(stack_history)])

    @line_dissector(letter_converter_pattern)
    def replace_letters(self, letter_number):
        return string.ascii_uppercase[to_int(letter_number) - 1]

    @line_dissector(evaluator_pattern)
    def evaluate_values(self, raw_line):
        return str(eval(raw_line))


if __name__ == '__main__':
    if sys.argv[1:]:
        patterns = {}
        with open(sys.argv[1]) as file:
            for pattern_index, combined_pattern in enumerate(file.read().splitlines()):
                match = name_regex.match(combined_pattern)
                if match:
                    pattern_name, pattern_code = map(str.strip, match.groups())
                    patterns[pattern_name] = pattern_code
                else:
                    patterns[pattern_index] = combined_pattern
    else:
        raise TypeError("Usage python pattern_generator.py [patterns.pg]")

    generator = ComplexPatternGenerator(justify_size=True, auto_index=True)
    for pattern_name, pattern_code in patterns.items():
        if not isinstance(pattern_name, str):
            pattern_name = None
        generator.generate(pattern_code, pattern_name)

    generator.print_all()
