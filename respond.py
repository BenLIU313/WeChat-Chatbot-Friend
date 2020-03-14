from joke import joke
from weather import weather
from nlp import interpreter
from finance import market
from finance import sh,sf,sp
import random

INIT=0
MARKET_SUMMARY=1
PROFILE_SYMBOL=2
HOLDERS_SYMBOL=3
FINANCIALS_SYMBOL=4

sad_responses=["Keep smiling! Things will calm down.https://music.163.com/#/song?id=523504",
               "I'm here for you.https://music.163.com/#/song?id=347230",
               "Win a few, lose a few. that's life.https://music.163.com/#/song?id=1383639 ",
               "Don't let it get you down. it will be over with soon.https://music.163.com/#/song?id=30039305",
               "Every cloud has a silver lining.https://emumo.xiami.com/play?ids=/song/playlist/id/mQ4jv3674d7#loaded"
               ]
greet_responses=["Hello，nice to meet you!","hi,Good to see you!","hello :-D","hi :)"]
bye_responses=["See You Later.","Good bye.","bye~","Have a nice day!","Bye bye! "]
happy_responses=[";-)，Got it.What would you want to know?","^0^，La La La La，What would you want to know?",
                 "^_~，Got it.What would you want?"]
thanks_respoonses=["You're welcome."," I'm glad I can help you!","It's my pleasure"]

def interpret(message):
    intent = interpreter.parse(message)["intent"]["name"]
    return intent
 
def respond(state,message):
    intent = interpreter.parse(message)["intent"]["name"]
    if intent=="joke":
        jk=joke()
    else:jk="haha"
    if intent=="weather":
        zip=interpreter.parse(message)['entities'][0]['value']
        wt=weather(zip)
    else:wt="The weather has been fine"
    if intent=="region":
        region = interpreter.parse(message)['entities'][0]['value'].upper()
        market_summary=market(region)
        print(region)
    else: market_summary="Please enter it again"
    if intent=="stock":
        symbol = interpreter.parse(message)['entities'][0]['value'].upper()
        if state==PROFILE_SYMBOL:
            stock_profile=sp(symbol)
        else:stock_profile="Please enter it again"
        if state==HOLDERS_SYMBOL:
            stock_holders=sh(symbol)
        else:stock_holders="Please enter it again"
        if state==FINANCIALS_SYMBOL:
            stock_financials=sf(symbol)
        else:stock_financials="Please enter it again"
    else: stock_financials,stock_holders,stock_profile="Please enter it again","Please enter stock name","Please enter stock "

    policy = {
        (INIT, "greet"): (INIT, random.choice(greet_responses)),
        (INIT, "name"): (INIT, "My name is Ben robot,you can call me Ben."),
        (INIT, "can"): (INIT,
                        "I can do these things:\n\n1.Be your friend.\n\n2.Tell jokes and make you happy\n"
                        "3.Enter the zip and get the weather report\n4.comfort you when you feel sad\n\n"
                        "5.help you make more money:\ntell you finance information at follow list:\n\n"
                        "1.market summary\n2.stock profile\n3.stock holders\n4.stock financials"),
        (INIT, "thanks"): (INIT, random.choice(thanks_respoonses)),
        (INIT, "no"): (INIT, "Well,what would you want to know?"),
        (INIT, "market"): (MARKET_SUMMARY,
                           "Well,the main region to get summary information from (AU | CA | FR | DE | HK | US | IT | ES | GB | IN)"),
        (INIT, "profile"): (PROFILE_SYMBOL, "Well, here is stock profile search. Enter your stock name."),
        (INIT, "holders"): (HOLDERS_SYMBOL, "Well, here is stock holders search. Enter your stock name."),
        (INIT, "financials"): (FINANCIALS_SYMBOL, "Well, here is stock financials search. Enter your stock name."),
        (INIT, "region"): (INIT,
                           "I can tell you some finance information,like market summary,stock profile,stock holders and"
                           " stock financials.What would you want to know?"),
        (INIT, "stock"): (INIT,
                          "I can tell you some finance information,like market summary,stock profile,stock holders and"
                          " stock financials.What would you want to know?"),
        (INIT, "none"): (INIT, "I'm sorry, I didn't understand that."),
        (INIT, "bye"): (INIT, random.choice(bye_responses)),
        (INIT, "joke"): (INIT, jk),
        (INIT, "weather"): (INIT, wt),
        (INIT, "affirm"): (INIT, random.choice(happy_responses)),
        (INIT, "sad"): (INIT, random.choice(sad_responses)),
        (MARKET_SUMMARY, "greet"): (MARKET_SUMMARY, "Hi, please choose a region."),
        (MARKET_SUMMARY, "name"): (
        MARKET_SUMMARY, "My name is Ben, I think you should remember me,please choose a region."),
        (MARKET_SUMMARY, "can"): (MARKET_SUMMARY, "I am working, please choose a region."),
        (MARKET_SUMMARY, "thanks"): (MARKET_SUMMARY, "It is my pleasure, please choose a region."),
        (MARKET_SUMMARY, "no"): (INIT, "OK,what would you want to know?"),
        (MARKET_SUMMARY, "market"): (MARKET_SUMMARY, "I am working, please choose a region."),
        (MARKET_SUMMARY, "profile"): (
        MARKET_SUMMARY, "If you don't want to get information about market,please say 'no'."),
        (MARKET_SUMMARY, "holders"): (
        MARKET_SUMMARY, "If you don't want to get information about market,please say 'no'."),
        (MARKET_SUMMARY, "financials"): (
        MARKET_SUMMARY, "If you don't want to get information about market,please say 'no'."),
        (MARKET_SUMMARY, "region"): (INIT, market_summary),
        (MARKET_SUMMARY, "stock"): (
        MARKET_SUMMARY, "If you don't want to get information about market,please say 'no'."),
        (MARKET_SUMMARY, "none"): (MARKET_SUMMARY, "I'm sorry, I didn't understand that.(っ °Д °;)っ"),
        (MARKET_SUMMARY, "bye"): (INIT, random.choice(bye_responses)),
        (MARKET_SUMMARY, "joke"): (MARKET_SUMMARY, "I am working, please choose a region."),
        (MARKET_SUMMARY, "weather"): (MARKET_SUMMARY, "I am working, please choose a region."),
        (MARKET_SUMMARY, "affirm"): (INIT, random.choice(happy_responses)),
        (MARKET_SUMMARY, "sad"): (INIT, random.choice(sad_responses)),
        (PROFILE_SYMBOL, "greet"): (PROFILE_SYMBOL, "Hi,please choose a stock."),
        (PROFILE_SYMBOL, "name"): (
        PROFILE_SYMBOL, "My name is Ben, I think you should remember me, please choose a stock."),
        (PROFILE_SYMBOL, "can"): (PROFILE_SYMBOL, "I am working, please choose a stock."),
        (PROFILE_SYMBOL, "thanks"): (PROFILE_SYMBOL, "It is my pleasure, please choose a stock."),
        (PROFILE_SYMBOL, "no"): (INIT, "OK,what would you want to know?"),
        (PROFILE_SYMBOL, "market"): (
        PROFILE_SYMBOL, "If you don't want to get information about stock,please say 'no'."),
        (PROFILE_SYMBOL, "profile"): (PROFILE_SYMBOL, "I am working, please choose a stock."),
        (PROFILE_SYMBOL, "holders"): (HOLDERS_SYMBOL, "OK,here is stock holders.\nPlease choose a stock."),
        (PROFILE_SYMBOL, "financials"): (FINANCIALS_SYMBOL, "OK,here is stock financials.\nPlease choose a stock."),
        (PROFILE_SYMBOL, "region"): (
        PROFILE_SYMBOL, "If you don't want to get information about stock,please say 'no'."),
        (PROFILE_SYMBOL, "stock"): (INIT, stock_profile),
        (PROFILE_SYMBOL, "none"): (PROFILE_SYMBOL, "I'm sorry, I didn't understand that."),
        (PROFILE_SYMBOL, "bye"): (INIT, random.choice(bye_responses)),
        (PROFILE_SYMBOL, "joke"): (PROFILE_SYMBOL, "I am working, please choose a stock."),
        (PROFILE_SYMBOL, "weather"): (PROFILE_SYMBOL, "I am working, please choose a stock."),
        (PROFILE_SYMBOL, "affirm"): (INIT, random.choice(happy_responses)),
        (PROFILE_SYMBOL, "sad"): (INIT, random.choice(sad_responses)),
        (HOLDERS_SYMBOL, "greet"): (HOLDERS_SYMBOL, "Hello, please choose a stock."),
        (HOLDERS_SYMBOL, "name"): (
        HOLDERS_SYMBOL, "My name is Ben, I think you should remember me,please choose a stock."),
        (HOLDERS_SYMBOL, "can"): (HOLDERS_SYMBOL, "I am working, please choose a stock."),
        (HOLDERS_SYMBOL, "thanks"): (HOLDERS_SYMBOL, "It is my pleasure, please choose a stock."),
        (HOLDERS_SYMBOL, "no"): (INIT, "OK,what would you want to know?"),
        (HOLDERS_SYMBOL, "market"): (
        HOLDERS_SYMBOL, "If you don't want to get information about stock,please say 'no'."),
        (HOLDERS_SYMBOL, "profile"): (PROFILE_SYMBOL, "OK,here is stock profile.\nPlease choose a stock."),
        (HOLDERS_SYMBOL, "holders"): (HOLDERS_SYMBOL, "I am working, please choose a stock."),
        (HOLDERS_SYMBOL, "financials"): (FINANCIALS_SYMBOL, "OK,here is stock financials.\nPlease choose a stock."),
        (HOLDERS_SYMBOL, "region"): (
        HOLDERS_SYMBOL, "If you don't want to get information about stock,please say 'no'."),
        (HOLDERS_SYMBOL, "stock"): (HOLDERS_SYMBOL, stock_holders),
        (HOLDERS_SYMBOL, "none"): (HOLDERS_SYMBOL, "I'm sorry, I didn't understand that."),
        (HOLDERS_SYMBOL, "bye"): (INIT, random.choice(bye_responses)),
        (HOLDERS_SYMBOL, "joke"): (HOLDERS_SYMBOL, "I am working, please choose a stock."),
        (HOLDERS_SYMBOL, "weather"): (HOLDERS_SYMBOL, "I am working, please choose a stock."),
        (HOLDERS_SYMBOL, "affirm"): (INIT, random.choice(happy_responses)),
        (HOLDERS_SYMBOL, "sad"): (INIT, random.choice(sad_responses)),
        (FINANCIALS_SYMBOL, "greet"): (FINANCIALS_SYMBOL, "Hey, please choose a stock."),
        (FINANCIALS_SYMBOL, "name"): (
        FINANCIALS_SYMBOL, "My name is Ben, I think you should remember me,please choose a stock."),
        (FINANCIALS_SYMBOL, "can"): (FINANCIALS_SYMBOL, "I am working, please choose a stock."),
        (FINANCIALS_SYMBOL, "thanks"): (FINANCIALS_SYMBOL, "It is my pleasure, please choose a stock."),
        (FINANCIALS_SYMBOL, "no"): (INIT, "OK,what would you want to know?"),
        (FINANCIALS_SYMBOL, "market"): (
        FINANCIALS_SYMBOL, "If you don't want to get information about stock,please say 'no'."),
        (FINANCIALS_SYMBOL, "profile"): (PROFILE_SYMBOL, "OK,here is stock profile.\nPlease choose a stock."),
        (FINANCIALS_SYMBOL, "holders"): (HOLDERS_SYMBOL, "OK,here is stock holders.\nPlease choose a stock."),
        (FINANCIALS_SYMBOL, "financials"): (FINANCIALS_SYMBOL, "I am working, please choose a stock."),
        (FINANCIALS_SYMBOL, "region"): (
        FINANCIALS_SYMBOL, "If you don't want to get information about stock,please say 'no'."),
        (FINANCIALS_SYMBOL, "stock"): (FINANCIALS_SYMBOL, stock_financials),
        (FINANCIALS_SYMBOL, "none"): (FINANCIALS_SYMBOL, "I'm sorry, I didn't understand that."),
        (FINANCIALS_SYMBOL, "bye"): (INIT, random.choice(bye_responses)),
        (FINANCIALS_SYMBOL, "joke"): (FINANCIALS_SYMBOL, "I am working, please choose a stock."),
        (FINANCIALS_SYMBOL, "weather"): (FINANCIALS_SYMBOL, "I am working, please choose a stock."),
        (FINANCIALS_SYMBOL, "affirm"): (INIT, random.choice(happy_responses)),
        (FINANCIALS_SYMBOL, "sad"): (INIT, random.choice(sad_responses)),
    }
    (new_state, response) = policy[(state, interpret(message))]
    return new_state, response

