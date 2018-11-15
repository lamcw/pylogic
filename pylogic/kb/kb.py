from abc import ABC, abstractmethod


class KnowledgeBase(ABC):
    @abstractmethod
    def ask(fact):
        pass

    @abstractmethod
    def tell(fact):
        pass
