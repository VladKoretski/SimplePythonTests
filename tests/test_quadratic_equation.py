import quadratic_equation as qe
import pytest

discriminant_params = ((0, 0, 0, 0),
          (4, 4, 1, 0),
          (-1, -5, 6, 49),
          (1, 1, 1, -3),
          (1/3, 1/3, 1/3, -1/3)
          )

equation_params = ((0, 0, 0, 'любое число'),
                   (4, 4, 1, -0.5),
                   (4, 1, 1, 'корней нет'),
                   (-1, -5, 6, (-6, 1))
                    )

@pytest.mark.parametrize('a, b, c, expected', discriminant_params)
def test_discriminant(a, b, c, expected):
    assert qe.discriminant(a, b, c) == pytest.approx(expected, abs=1e-9)


@pytest.mark.parametrize('a, b, c, expected', equation_params)
def test_solution(a, b, c, expected):
    assert qe.solution(a, b, c) == pytest.approx(expected, abs=1e-9)