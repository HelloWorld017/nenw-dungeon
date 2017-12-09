class Skill(object):
    def __init__(self, name, description, require_score, group, previous):
        self.name = name
        self.description = description
        self.require_score = require_score
        self.group = group
        self.previous = previous

        self.activated = False

        if all(skill.name != name for skill in self.group.skills):
            self.group.add_skill(self)

    def activate(self, player):
        if not self.can_activate(player):
            return False

        player.point -= 1
        player.score -= self.require_score

        self.do_activate(player)
        return True

    def do_activate(self, player):
        pass

    def can_activate(self, player):
        if self.previous is not None:
            if not self.previous.activated:
                return False

        if self.require_score > player.score:
            return False

        if player.point < 1:
            return False

        return self.check_can_activate(player)

    def check_can_activate(self, player):
        pass
