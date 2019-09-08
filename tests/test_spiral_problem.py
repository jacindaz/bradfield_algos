import pytest
import algos.spiral_problem as spiral
import algos.spiral_problem2 as spiral2


@pytest.mark.parametrize("height, width, expected", [
    (1, 4, [[1,2,3,4]]),
    (3, 4, [[1,2,3,4],[10,11,12,5],[9,8,7,6]]),
    (
        4,4,
        [
            [1,2,3,4],
            [12,13,14,5],
            [11,16,15,6],
            [10,9,8,7]
        ]
    ),
    (
        6,6,
        [
            [1,2,3,4,5,6],
            [20,21,22,23,24,7],
            [19,32,33,34,25,8],
            [18,31,36,35,26,9],
            [17,30,29,28,27,10],
            [16,15,14,13,12,11]
        ]
    )
])
def test_spiral_problem(height, width, expected):
    spiral_instance = spiral.Spiral(height, width)
    spiral_instance.run()

    assert spiral_instance.result == expected

    # simpler solution
    simpler_solution = spiral2.build_spiral(height, width)
    assert simpler_solution == expected
