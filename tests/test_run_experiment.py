import bayesian_ab_testing


def test_run_experiment_a():
    res = bayesian_ab_testing.run_experiment_a()
    assert isinstance(res, int)
    assert res == 0 or res == 1

def test_run_experiment_b():
    res = bayesian_ab_testing.run_experiment_b()
    assert isinstance(res, int)
    assert res == 0 or res == 1