import pandas as pd
import matplotlib.pyplot as plt

# Load the xlsx file
excel_data = pd.read_excel('ud_2023-03-10.xlsx')
# Read the values of the file in the dataframe
data = pd.DataFrame(excel_data, columns=[
    'participant.id_in_session',
    'participant.code',
    'participant.payoff',
    'player.id_in_group',
    'player.payoff',
    'group.id_in_subsession',
    'group.sent_amount',
    'group.accept_answer',
    'subsession.round_number',
    ''
])
# Print the content
# print("The content of the file is:\n", data['participant.code'])

# Найти средний размер предложения партнеру по всем участникам за всю игру. = 3.66
def averageOffer():
    offers = data['group.sent_amount']
    avg = sum(offers) / len(data)
    print(avg)

# Найти среднюю величину предложения, на которое соглашались участники. = 4.21
def averageOfferAccepted():
    sentAmountAccepted = data.loc[data['group.accept_answer'] == 'ДА', 'group.sent_amount'].sum()
    acceptedNum = len(data[data['group.accept_answer'] == 'ДА'])
    avgAccepted = sentAmountAccepted / acceptedNum
    print(avgAccepted)

# Найти средние, разбив все попытки на группы по 5 ???

# Вычисление среднего предложения от определенного участника
def personalAverageOffer(playerId):
    sentAmount = data.loc[(data['player.id_in_group'] == 1) & (data['participant.id_in_session'] == playerId), 'group.sent_amount'].sum()
    sentNum = len(data[(data['participant.id_in_session'] == playerId) & (data['player.id_in_group'] == 1)])
    return sentAmount / sentNum

# Средний размер предложения от определенного участника
def averageOfferFromPlayers():
    playersNum = data['participant.id_in_session'].nunique()
    playersAverageOffers = {}
    for i in range(playersNum):
        playersAverageOffers[i + 1] = personalAverageOffer(i + 1)

    print(playersAverageOffers)

# Вычисление среднего принятого предложения от определенного участника
def personalAverageOfferAccepted(playerId):
    sentAmount = data.loc[
        (data['player.id_in_group'] == 1) &
        (data['participant.id_in_session'] == playerId) &
        (data['group.accept_answer'] == 'ДА'),
        'group.sent_amount'
    ].sum()
    sentNum = len(data[
                      (data['participant.id_in_session'] == playerId) &
                      (data['player.id_in_group'] == 1) &
                      (data['group.accept_answer'] == 'ДА')
                      ])
    return sentAmount / sentNum

# Средний размер принятого предложения от определенного участника
def averageOfferFromPlayersAccepted():
    playersNum = data['participant.id_in_session'].nunique()
    playersAverageOffers = {}
    for i in range(playersNum):
        playersAverageOffers[i + 1] = personalAverageOfferAccepted(i + 1)

    print(playersAverageOffers)


# def personalAverageOffer(playerId):
#     sentAmount = data.loc[(data['group.accept_answer'] == 'ДА') & (data['participant.id_in_session'] == playerId), 'group.sent_amount'].sum()
#     sentNum = len(data[(data['participant.id_in_session'] == playerId) & (data['player.id_in_group'] == 1)])
#     print(sentAmount / sentNum)


# averageOffer()
# averageOfferAccepted()
# averageOfferFromPlayers()
# averageOfferFromPlayersAccepted()
