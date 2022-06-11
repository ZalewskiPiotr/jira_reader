from jira_reader import runner


def test_number():
    value = runner.test_func(2)
    assert value == 4
