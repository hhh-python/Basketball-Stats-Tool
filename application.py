import constants

PLAYERS = constants.PLAYERS.copy()
panthers, warriors, bandits = [], [], []

#Updates the PLAYERS database by converting height(string type)
#to an integar and the experience(string type) to a boolean type
def clean_data():
    for player in PLAYERS:
        player['height'] = int(player['height'][:2])
        player['guardians'] = player['guardians'].split(' and ')
        print(player['guardians'])
        player['guardians']
        if player['experience'].lower() == 'yes':
            player['experience'] = True
        else:
            player['experience'] = False
 
            
#Loops through the PLAYERS database and adds experienced and inexperienced
#players proportionatley to the 3 teams  
def balance_teams():
    experienced_players, inexperienced_players = [], []
    teams = [panthers, warriors, bandits]
    for team in teams:
            experienced_players.clear()
            inexperienced_players.clear()
            for player in PLAYERS.copy():
                if player['experience'] == True and len(experienced_players) < 3:
                    team.append(player)
                    experienced_players.append(player)
                    del PLAYERS[PLAYERS.index(player)]
                elif player['experience'] == False and len(inexperienced_players) < 3:
                    team.append(player)
                    inexperienced_players.append(player)
                    del PLAYERS[PLAYERS.index(player)]

  
def display_stats_for(team, team_data):
        print(f'TEAM: {team.capitalize()}')
        print('-'*17)
        print(f'TOTAL PLAYERS: {len(team_data)} \n')
        experienced_players = [i['experience'] for i in team_data].count(True)
        inexperienced_players = [i['experience'] for i in team_data].count(False)
        print(f'TOTAL EXPERIENCED PLAYERS: {experienced_players} \n')
        print(f'TOTAL INEXPERIENCED PLAYERS: {inexperienced_players} \n')
        average_height = [i['height'] for i in team_data]
        average_height = round(sum(average_height) / len(average_height), 1)
        print(f'AVERAGE HEIGHT: {average_height} \n')
        names = [player['name'] for player in team_data]
        names = ', '.join(names)
        guardians = []
        for player in team_data:
            if len(player['guardians']) > 1:
                for i in player['guardians']:
                    guardians.append(i)
            else:
                guardians.append(''.join(player['guardians']))
        print(f'PLAYER NAMES: {names} \n')
        print('PLAYERS GUARDIANS:', ', '.join(guardians), '\n')


if __name__ == "__main__":
    clean_data()
    balance_teams()
    print('\n', 'YOU ARE NOW USING THE BASKETBALL TEAM STATS TOOL')
    while True: 
        print('\n', '-'* 21, 'Menu', '-'* 21)
        print('''
        Please select one of the following menu options:
        A). Display team stats
        B). Quit
        ''')
        try:
            menu_option = input('Enter option: ').lower()
            if menu_option not in ['a', 'b']:
                raise ValueError('Please select either of the two options only (A or B)')
            if menu_option.lower() == 'a':
                print('Here are the teams stats you can view Panthers, Warriors, and Bandits', '\n')
                selected_team = input('Please type in the entire name of the team to view their stats: ').lower()
                if selected_team not in ['panthers', 'warriors', 'bandits']:
                    raise ValueError('The only avaliable names to type in are Panthers, Warriors, Bandits)')
            elif menu_option.lower() == 'b':
                break
        except ValueError as error:
            print(f'That is not a valid value you! ({error})')
        else:
            if selected_team == 'panthers':
                display_stats_for(selected_team, panthers)
            elif selected_team == 'warriors':
                display_stats_for(selected_team, warriors)
            elif selected_team == 'bandits':
                display_stats_for(selected_team, bandits)
            back_to_menu = input('Press ENTER to continue...')
