import requests
import json
import pandas as pd
from datetime import datetime

# Nick Schmaltz's NHL Player ID
PLAYER_ID = 8477951
SEASON = "20242025"

def fetch_player_stats(player_id, season):
    """Fetch player statistics from NHL Stats API"""
    base_url = "https://api.nhle.com/stats/rest/en/skater/summary"
    params = {
        "cayenneExp": f"playerId={player_id} and seasonId={season}"
    }
    
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def fetch_player_game_log(player_id, season):
    """Fetch player game-by-game statistics"""
    url = f"https://api-web.nhle.com/v1/player/{player_id}/game-log/{season}/2"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching game log: {e}")
        return None

def fetch_player_landing(player_id):
    """Fetch player landing page data with current season stats"""
    url = f"https://api-web.nhle.com/v1/player/{player_id}/landing"
    
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching player landing data: {e}")
        return None

def save_to_json(data, filename):
    """Save data to JSON file"""
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"Data saved to {filename}")

def save_to_csv(data, filename):
    """Save data to CSV file"""
    if isinstance(data, dict) and 'data' in data:
        df = pd.DataFrame(data['data'])
    elif isinstance(data, list):
        df = pd.DataFrame(data)
    else:
        df = pd.DataFrame([data])
    
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    print("Downloading Nick Schmaltz 2024-25 season statistics...")
    print(f"Player ID: {PLAYER_ID}")
    print(f"Season: {SEASON}\n")
    
    # Fetch summary stats
    print("Fetching season summary stats...")
    summary_stats = fetch_player_stats(PLAYER_ID, SEASON)
    if summary_stats:
        save_to_json(summary_stats, "schmaltz_2024-25_summary.json")
        if 'data' in summary_stats and summary_stats['data']:
            save_to_csv(summary_stats, "schmaltz_2024-25_summary.csv")
            print("\nSummary Statistics:")
            stats = summary_stats['data'][0]
            print(f"  Games Played: {stats.get('gamesPlayed', 'N/A')}")
            print(f"  Goals: {stats.get('goals', 'N/A')}")
            print(f"  Assists: {stats.get('assists', 'N/A')}")
            print(f"  Points: {stats.get('points', 'N/A')}")
            print(f"  Plus/Minus: {stats.get('plusMinus', 'N/A')}")
            print(f"  Shots: {stats.get('shots', 'N/A')}")
            print(f"  TOI/Game: {stats.get('timeOnIcePerGame', 'N/A')}")
    
    # Fetch game-by-game log
    print("\n\nFetching game-by-game log...")
    game_log = fetch_player_game_log(PLAYER_ID, SEASON)
    if game_log:
        save_to_json(game_log, "schmaltz_2024-25_game_log.json")
        if 'gameLog' in game_log:
            save_to_csv(game_log['gameLog'], "schmaltz_2024-25_game_log.csv")
            print(f"  Total games in log: {len(game_log['gameLog'])}")
    
    # Fetch landing page data (alternative source)
    print("\nFetching player landing page data...")
    landing_data = fetch_player_landing(PLAYER_ID)
    if landing_data:
        save_to_json(landing_data, "schmaltz_2024-25_landing.json")
        print("  Landing page data saved")
    
    print("\n✅ Download complete!")
    print("\nFiles created:")
    print("  - schmaltz_2024-25_summary.json/csv (season totals)")
    print("  - schmaltz_2024-25_game_log.json/csv (game-by-game stats)")
    print("  - schmaltz_2024-25_landing.json (comprehensive player data)")

if __name__ == "__main__":
    main()