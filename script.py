
print("Software Testing Practical 6")

print("GitHub Version Control")

# Sample test cases

def test_addition():
    assert 10 + 20 == 30
    print("Test 1 Passed: Addition")

def test_subtraction():
    assert 20 - 10 == 10
    print("Test 2 Passed: Subtraction")

def test_multiplication():
    assert 5 * 4 == 20
    print("Test 3 Passed: Multiplication")

# Execute test cases

test_addition()
test_subtraction()
test_multiplication()

print("All test cases executed successfully!")

def test_division():
    assert 20 / 5 == 4
    print("Test 4 Passed: Division")

test_division()