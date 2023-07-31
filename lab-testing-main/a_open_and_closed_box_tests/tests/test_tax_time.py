import tests.test_helper as th
import re
# test examples
command_python = "python3 python/tax_time.py"
command_java = "java javasource.TaxTime"
command = command_python 

def test_example():
    input_values = [ 45000, 3 ]
    output = th.call_shell_command(command, input_values)
    numbers = extract_numbers(output)
    assert numbers == [45000.0, 3.0, 8300.0, 300.0]

def extract_numbers(output):
    relevant_output = output[4:-2]
    numbers = [float(re.sub(r'.* ([0-9.]+).*',r'\1', s)) for s in relevant_output]
    return numbers

def test_example_with_string():
    input_values = [ 45000, 3 ]
    output = th.call_shell_command(command, input_values)
    relevant_output = output[4:-2]
    output_str = '\n'.join(output[4:-2])
    expected_str = """Your income was 45000.0 €.
You have 3 family members.
Your total tax is 8300.0 €.
Family member tax saving is 300 €."""
    assert output_str == expected_str
