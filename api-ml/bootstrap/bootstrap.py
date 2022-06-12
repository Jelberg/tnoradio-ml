from mlkit.app.useCases.CleanTextsUc import (UseCaseGetCleanText)

from mlkit.app.controller.getCleanTextsController import (GetCleanTextsController)


class Init:
    
    def getCleanTextsBootstrap():
        return GetCleanTextsController(UseCaseGetCleanText)
