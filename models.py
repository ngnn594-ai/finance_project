# я об этой хуйня ваше ток в конце вспомнил

from dataclasses import dataclass


@dataclass
class Transaction:
    id: int
    type: str
    amount: float
    category: str
    date: str
    comment: str


#эт хуйня даже не где не исполь а лан поъ