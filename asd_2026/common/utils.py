from datetime import datetime


def ts() -> float:
    return datetime.now().timestamp()


def duration(start: float) -> str:
    return  f'{ts() - start:.3f}'