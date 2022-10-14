from snake_ladder import start
from approvaltests import verify
import random


def test_start(mocker):
    mocker.patch("snake_ladder.get_player_names",
                 return_value=("player_a", "player b"))
    mocker.patch("time.sleep")
    mocker.patch("builtins.input")
    spy = mocker.patch("builtins.print")
    # mocker.patch("sys.exit")
    random.seed(2)

    try:
        start()
    except:
        pass

    verify(spy.call_args_list)
