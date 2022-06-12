from abc import ABC, abstractmethod
from mlkit.app.useCases.CleanTextsUc import UseCaseGetCleanText


class GetCleanTextsController():
    
    def __init__(self, useCase = any):
        self.useCase = useCase

    async def handle():
        print('NIVEL CONTROLADOR HANDLE')
        return await UseCaseGetCleanText.execute()
