import json
from sejmStatement import SejmStatement

data = []

sittingExist = True
sittingIndex = 1

while sittingExist:
    firstDaySittingStatement = SejmStatement(sittingIndex, 1, 1)
    sittingExist = len(firstDaySittingStatement.getText()) > 0

    sittingDay = 1
    dayExist = True
    while dayExist:
        statementIndex = 1
        statementExist = True

        while statementExist:
            statement = SejmStatement(sittingIndex, sittingDay, statementIndex)
            statementText = statement.getText()
            if statementText:
                data.append(statementText)
                statementIndex += 1
            else:
                statementExist = False

        sittingDay += 1
        dayFirstStatement = SejmStatement(sittingIndex, sittingDay, 1)
        dayExist = len(dayFirstStatement.getText()) > 0
        with open('data.json', 'w') as outfile:
            json.dump(data, outfile)

    sittingIndex += 1
