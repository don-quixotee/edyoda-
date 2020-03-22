from a01 import *
import pytest

@pytest.mark.parametrize("test_input, expected", [(5, '5\n10\n15\n20\n25\n30\n35\n40\n45\n50\n')])
def test_eval1(test_input, expected):
    assert question_first_solution(test_input)== expected

@pytest.mark.parametrize("test_input, expected", [(153, True)])
def test_eval2(test_input, expected):
    assert question_second_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(15, 'FizzBuzz')])
def test_eval3(test_input, expected):
    assert question_third_solution(test_input) == expected


@pytest.mark.parametrize("test_input1, test_input2, expected", [(54, 24, 6)])
def test_eval4(test_input1, test_input2, expected):
    assert question_fourth_solution(test_input1, test_input2) == expected

@pytest.mark.parametrize("test_input, expected", [([5,9,7,3,1,5,97,6,3,7],[1, 3, 3, 5, 5, 6, 7, 7, 9, 97])])
def test_eval5(test_input, expected):
    assert question_fifth_solution(test_input) == expected

@pytest.mark.parametrize("test_input1, test_input2, expected", [(3, 4, [[0, 2, 4, 6], [2, 4, 6, 8], [4, 6, 8, 10]])])
def test_eval6(test_input1, test_input2, expected):
    assert question_sixth_solution(test_input1, test_input2) == expected

@pytest.mark.parametrize("test_input, expected", [(315, [3,5,7])])
def test_eval7(test_input, expected):
    assert question_seventh_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(5, [0,1,1,2,3])])
def test_eval8(test_input, expected):
    assert question_eighth_solution(test_input) == expected

@pytest.mark.parametrize("test_input, expected", [(5462, 2645)])
def test_eval9(test_input, expected):
    assert question_ninth_solution(test_input) == expected


@pytest.mark.parametrize("test_input, expected", [(25643, 2)])
def test_eval10(test_input, expected):
    assert question_tenth_solution(test_input) == expected