import requests

def sp(stock):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-profile"

    querystring = {"symbol": stock}

    headers = {####
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    js = response.json()
    s=js["price"]
    result=("Symbol:{0}\nsector:{1}\n\nregularMarketOpen:\n{2}\n\naverageDailyVolume3Month:\n{3}\n\n"
            "averageDailyVolume10Day:\n{4}\n\nregularMarketDayHigh:\n{5}\n\nregularMarketChange:\n{6}"
            "\n\nregularMarketPreviousClose:\n"
            "{7}\n\npageViews:\nshortTermTrend:{8}\nmidTermTrend:{9}\nlongTermTrend:{10}")\
        .format(js["symbol"],js["assetProfile"]["sector"],s["regularMarketOpen"]["fmt"],
                s["averageDailyVolume3Month"]["fmt"],s["averageDailyVolume10Day"]["fmt"],s["regularMarketDayHigh"]["fmt"],
                s["regularMarketChange"]["fmt"],s["regularMarketPreviousClose"]["fmt"],js["pageViews"]["shortTermTrend"],
                js["pageViews"]["midTermTrend"],js["pageViews"]["longTermTrend"])
    return result

def sf(stock):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-financials"

    querystring = {"symbol": stock}

    headers = {####
    }

    re = requests.request("GET", url, headers=headers, params=querystring)
    js=re.json()
    j=js["cashflowStatementHistory"]["cashflowStatements"][0]
    s=js["balanceSheetHistoryQuarterly"]["balanceSheetStatements"][0]
    result=("CashflowStatements:\n\nchangeToLiabilities:{0}\ntotalCashflowsFromInvestingActivities:{1}\n"
            "netBorrowings:{2}\ntotalCashFromFinancingActivities:{3}\nchangeToOperatingActivities:{4}\n"
            "issuanceOfStock:{5}\nnetIncome:{6}\nchangeInCash:{7}\nrepurchaseOfStock:{8}\n\n"
            "balanceSheetHistory:\n\nintangibleAssets:{9}\ncapitalSurplus:{10}\ntotalLiab:{11}\n"
            "totalStockholderEquity:{12}\notherCurrentLiab:{13}\ntotalAssets:{14}\ncommonStock:{15}\ntreasuryStock:{16}")\
        .format(j["changeToLiabilities"]["fmt"],j["totalCashflowsFromInvestingActivities"]["fmt"],j["netBorrowings"]["fmt"],
         j["totalCashFromFinancingActivities"]["fmt"],j["changeToOperatingActivities"]["fmt"],j["issuanceOfStock"]["fmt"],
         j["netIncome"]["fmt"],j["changeInCash"]["fmt"],j["repurchaseOfStock"]["fmt"],s["intangibleAssets"]["fmt"],
         s["capitalSurplus"]["fmt"],s["totalLiab"]["fmt"],s["totalStockholderEquity"]["fmt"],s["otherCurrentLiab"]["fmt"],
         s["totalAssets"]["fmt"],s["commonStock"]["fmt"],s["treasuryStock"]["fmt"])
    return result



def sh(stock):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-holders"

    querystring = {"symbol": stock}

    headers = {####
    }

    re = requests.request("GET", url, headers=headers, params=querystring)
    js=re.json()
    s=js["insiderHolders"]["holders"]
    result=("InsiderHolders:\n\n1.name:{0}\nrelation:{1}\nlatestTransDate:{2}\npositionDirect:{3}\n\n"
            "2.name:{4}\nrelation:{5}\nlatestTransDate:{6}\npositionDirectDate:{7}\n\n"
            "3.name:{8}\nrelation:{9}\nlatestTransDate:{10}\npositionDirect:{11}\n\n"
            "4.name:{12}\nrelation:{13}\nlatestTransDate:{14}\npositionDirect:{15}\n\n"
            "5.name:{16}\nrelation:{17}\nlatestTransDate:{18}\npositionDirect:{19}\n\n")\
        .format(s[0]["name"],s[0]["relation"],s[0]["latestTransDate"]["fmt"],s[0]["positionDirect"]["fmt"],
                s[1]["name"],s[1]["relation"],s[1]["latestTransDate"]["fmt"],s[1]["positionDirectDate"]["fmt"],
                s[2]["name"],s[2]["relation"],s[2]["latestTransDate"]["fmt"],s[2]["positionDirect"]["fmt"],
                s[3]["name"],s[3]["relation"],s[3]["latestTransDate"]["fmt"],s[3]["positionDirect"]["fmt"],
                s[4]["name"],s[4]["relation"],s[4]["latestTransDate"]["fmt"],s[4]["positionDirect"]["fmt"])
    return result



def market(region):
    url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/market/get-summary"

    querystring = {"region": region, "lang": "en"}

    headers = {####
    }

    r = requests.request("GET", url, headers=headers, params=querystring)
    js=r.json()
    result=("ExchangeTimezoneName:{0}\nfullExchangeName:{1}\n\nregularMarketChange:\n{2}\n\nregularMarketTime:\n"
            "{3}\n\nregularMarketChangePercent:\n{4}\n\nregularMarketPrice:\n{5}\n\n"
            "regularMarketPreviousClose:\n{6}\n\nmarket:{7}\nregion:{8}")\
        .format(js["marketSummaryResponse"]["result"][0]["exchangeTimezoneName"],js["marketSummaryResponse"]["result"][0]["fullExchangeName"],
                js["marketSummaryResponse"]["result"][0]["regularMarketChange"]["fmt"],
                js["marketSummaryResponse"]["result"][0]["regularMarketTime"]["fmt"],
                js["marketSummaryResponse"]["result"][0]["regularMarketChangePercent"]["fmt"],
                js["marketSummaryResponse"]["result"][0]["regularMarketPrice"]["fmt"],
                js["marketSummaryResponse"]["result"][0]["regularMarketPreviousClose"]["fmt"],
                js["marketSummaryResponse"]["result"][0]["market"],js["marketSummaryResponse"]["result"][0]["region"])
    return result
