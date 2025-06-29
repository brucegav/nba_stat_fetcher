"""
NBA Stat Fetcher

A simple Python program to fetch and display NBA player statistics.

INSTALLATION REQUIREMENTS:
Before running this program, you need to install the required package:

    pip install nba_api

SYSTEM REQUIREMENTS:
- Python 3.6 or later
- Internet connection (for fetching live NBA data)

USAGE:
Run this program and follow the prompts to search for NBA players
and view their statistics including current season, career totals,
playoff stats, and college stats.

Author: [Your Name]
"""

import requests
import json
from nba_api.stats.endpoints import playercareerstats
from nba_api.stats.static import players

def main():
    # Check if required package is available
    try:
        from nba_api.stats.endpoints import playercareerstats
        from nba_api.stats.static import players
    except ImportError:
        print("ERROR: Required package 'nba_api' is not installed.")
        print("Please install it by running: pip install nba_api")
        print("Then restart this program.")
        return
    
    print("Welcome to the NBA Stat Fetcher")
    print("Fetching NBA data... (this may take a moment)")
    print("-" * 50)
    
    while True:  # main program loop
        # get player name
        player_name = input("Enter player name (or 'quit' to exit): ")
        if player_name.lower() == 'quit':
            break

        cleaned_name = clean_player_name(player_name)
        found_players = players.find_players_by_full_name(cleaned_name)
        if not found_players:
            print("Player not found. Please check spelling.")
            continue
            
        player_id = found_players[0]['id']
        player_career_stats = playercareerstats.PlayerCareerStats(player_id=player_id)
        data_frames = player_career_stats.get_data_frames()

        print(f"Player found: {found_players[0]['full_name']}")

        # If player found, enter stats viewing loop
        while True:  # stats viewing loop for current player 
            # shows stats menu
            stats_choice = display_stats_menu()

            if stats_choice in ['1', '2', '3', '4', '5']:
                # display results
                result = extract_stats(data_frames, stats_choice)
                print("\n" + "="*50)
                print(result)
                print("="*50)
                
                # show post-stats menu
                post_choice = display_post_stats_menu()

                if post_choice == '1':  # View different stats for this player
                    continue  # Stay in inner loop
                elif post_choice == '2':  # Search for different player
                    break  # Break inner loop, go to outer loop
                elif post_choice == '3':  # Quit
                    print("Thanks for using NBA Stat Fetcher!")
                    return  # Exit entire program
                else:
                    print("Invalid choice. Returning to stats menu.")
                    continue
                    
            elif stats_choice == '6':
                break
            elif stats_choice == '7':
                print("Thanks for using NBA Stat Fetcher!")
                return
            else:
                print("Invalid choice. Please enter 1-7.")
                continue
                
    print("Thanks for using NBA Stat Fetcher!")

def clean_player_name(user_input):
    return " ".join(user_input.strip().split())

def display_stats_menu():
    print("\nPlease select from the following options:")
    print("1. View current season totals")
    print("2. View past 5 seasons totals")
    print("3. View postseason career totals")
    print("4. View regular season career totals")
    print("5. View college totals")
    print("6. Search another player")
    print("7. Quit program")
    choice = input("Enter your choice (1-7): ")
    return choice

def display_post_stats_menu():
    print("\nWhat would you like to do next?")
    print("1. View different stats for this player")
    print("2. Search for a different player")
    print("3. Quit program")
    return input("Enter your choice (1-3): ")

def extract_stats(data_frames, choice):
    if choice == "1":  # current season stats
        result = data_frames[0].tail(1)
        return clean_stats_display(result)  # last row of season stats
    
    elif choice == "2":  # last 5 seasons 
        result = data_frames[0].tail(5)  # last 5 rows
        return clean_stats_display(result)
    
    elif choice == "3":  # playoff career totals
        playoff_df = data_frames[3]
        if playoff_df.empty:
            return "This player has no postseason stats"
        return clean_stats_display(playoff_df)
    
    elif choice == "4":  # career regular season totals
        return clean_stats_display(data_frames[1])
    
    elif choice == "5":  # college totals
        college_df = data_frames[6]
        if college_df.empty:
            return "This player has no college stats"
        return clean_stats_display(college_df)

def clean_stats_display(df):
    # remove statistically irrelevant columns 
    columns_to_remove = ['LEAGUE_ID', 'ORGANIZATION_ID', 'SCHOOL_NAME', 'TEAM_ID', 'PLAYER_ID']

    # remove unwanted columns, if they exist
    cleaned_df = df.drop(columns=[col for col in columns_to_remove if col in df.columns])

    # rename columns
    column_renames = {
        'SEASON_ID': 'Season',
        'TEAM_ABBREVIATION': 'Team', 
        'PLAYER_AGE': 'Age',
        'FG_PCT': 'FG%',
        'FG3_PCT': '3P%',
        'FT_PCT': 'FT%',
        'FG3M': '3PM',
        'FG3A': '3PA'
    }

    cleaned_df = cleaned_df.rename(columns=column_renames)

    return cleaned_df

if __name__ == "__main__":
    main()
