from abc import ABC, abstractmethod


class A(ABC):

    @abstractmethod
    def g(self):
        print('ok')


class B(A):

    def g(self):
        super().g()
        print('done')


if __name__ == '__main__':
    b = B()
    b.g()