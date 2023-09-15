from statistics import mean


class Game:
    def __init__(self, title):
        self.title = title

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) and not hasattr(self, "title"):
            self._title = title

    def results(self):
        return [result for result in Result.all if result.game is self]

    def players(self):
        return list(
            set([result.player for result in Result.all if result.game is self])
        )

    def average_score(self, player):
        return mean(
            [
                result.score
                for result in Result.all
                if result.game is self and result.player is player
            ]
        )


class Player:
    def __init__(self, username):
        self.username = username

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, username):
        if isinstance(username, str) and len(username) in range(2, 17):
            self._username = username

    def results(self):
        return [result for result in Result.all if result.player is self]

    def games_played(self):
        return list(
            set([result.game for result in Result.all if result.player is self])
        )

    def played_game(self, game):
        return self.num_times_played(game) > 0

    def num_times_played(self, game):
        return len(
            [
                result.game
                for result in Result.all
                if result.player is self and result.game is game
            ]
        )


class Result:
    all = []

    def __init__(self, player, game, score):
        self.player = player
        self.game = game
        self.score = score
        self.__class__.all.append(self)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if (
            isinstance(score, int)
            and not hasattr(self, "score")
            and score in range(1, 5001)
        ):
            self._score = score

    @property
    def game(self):
        return self._game

    @game.setter
    def game(self, game):
        if isinstance(game, Game):
            self._game = game

    @property
    def player(self):
        return self._player

    @player.setter
    def player(self, player):
        if isinstance(player, Player):
            self._player = player
