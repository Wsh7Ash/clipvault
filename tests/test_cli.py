import json

from click.testing import CliRunner
from clipvault import cli


def test_save_and_list(tmp_path, monkeypatch):
    store = tmp_path / "store.json"
    monkeypatch.setattr(cli, "STORE", store)
    runner = CliRunner()

    assert runner.invoke(cli.main, ["save", "first"]).exit_code == 0
    assert runner.invoke(cli.main, ["save", "second"]).exit_code == 0

    res = runner.invoke(cli.main, ["list"])
    assert res.exit_code == 0, res.output
    assert "0: first" in res.output
    assert "1: second" in res.output
    assert json.loads(store.read_text()) == ["first", "second"]
