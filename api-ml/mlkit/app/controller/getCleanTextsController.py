from abc import ABC, abstractmethod
from mlkit.app.useCases.CleanTextsUc import UseCaseGetCleanText

class UseCase(ABC):
    @abstractmethod
    def getClean():
        get = UseCaseGetCleanText()
        return get


class GetCleanTextsController():
    
    def __init__(self, useCase = UseCase):
        print('NIVEL CONTROLADOR CONSTRUCTOR')
        self.useCase = useCase

    async def handle():
        print('NIVEL CONTROLADOR HANDLE')
        this = GetCleanTextsController()
        return await this.useCase.getClean().execute()
