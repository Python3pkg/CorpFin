

class Security:
    def __init__(
            self, label='',
            bs_val=lambda **kwargs: 0.,
            val=lambda **kwargs: 0.):
        self.name = label
        self.bs_val = bs_val
        self.val = val


DOLLAR = \
    Security(
        label='$',
        bs_val=lambda **kwargs: 1.,
        val=lambda **kwargs: 1.)
