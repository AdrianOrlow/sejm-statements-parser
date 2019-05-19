import time
import requests
import textwrap
from bs4 import BeautifulSoup


class SejmStatement:
    baseUrl = 'http://www.sejm.gov.pl/Sejm8.nsf/wypowiedz.xsp'

    def __init__(self, sittingIndex, sittingDay, statementIndex):
        self.queryUrl = self.getQueryUrl(
            sittingIndex, sittingDay, statementIndex)

    def getQueryUrl(self, sittingIndex, sittingDay, statementIndex):
        return f"{self.baseUrl}?posiedzenie={sittingIndex}&dzien={sittingDay}&wyp={statementIndex}"

    def getText(self):
        time.sleep(.600)
        response = requests.get(self.queryUrl)
        statementPage = BeautifulSoup(response.text, 'html.parser')

        return self.getStatementText(statementPage)

    def getStatementText(self, statementPage):
        # Selects statement transcript without headers
        lines = statementPage.select('.stenogram p:not([class])')

        statement = ""
        for line in lines:
            textLine = line.text

            # Removes paragraph indentation
            textLine = textLine.lstrip()

            # Checks is tag not an additional info
            tagIsPartOfStatement = textLine[0] != '('

            if tagIsPartOfStatement:
                statement += textLine + '\n'

        return statement
