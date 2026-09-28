import pytest
import votes

parameters = (
    ([3, 2, 3, 2, 1, 1, 1, 3, 1, 1], 1),
    ([1, 1, 2, 1, 2, 1, 3, 3, 3, 3, 2, 1, 2, 1, 1], 1),
    ([1, 2, 2, 3, 2, 1, 1, 3, 2, 3, 2, 2, 3, 3, 1, 2, 1, 3, 3, 1], 'Нужен второй тур выборов'),
    ([2, 2, 1, 3, 3, 2, 3, 1, 1, 2, 1, 2, 2, 2, 3], 2),
    ([3, 3, 2, 2, 1, 3, 1, 2, 3, 1, 2, 2, 1, 3, 3], 3)
)

@pytest.mark.parametrize("votes_list, expected", parameters)
def test_votes(votes_list, expected):
    assert votes.vote(votes_list) == expected