# NBA Stat Fetcher

A simple Python command-line application that allows users to search for NBA players and view their basketball statistics in a clean, formatted display.

## Features

- **Player Search**: Search for any NBA player by name
- **Multiple Stat Categories**:
  - Current season totals
  - Past 5 seasons totals
  - Postseason career totals
  - Regular season career totals
  - College totals
- **Clean Data Display**: Removes irrelevant columns and formats data for easy reading
- **Interactive Menu System**: Easy-to-use command-line interface

## Prerequisites

- Python 3.6 or later
- Internet connection (for fetching live NBA data)

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/nba-stat-fetcher.git
   cd nba-stat-fetcher
   ```

2. Install the required package:
   ```bash
   pip install nba_api
   ```

## Usage

Run the program from your terminal:

```bash
python nba_stat_fetcher.py
```

### How to Use

1. **Start the program** - You'll see the welcome message
2. **Enter a player name** - Type the full name of any NBA player (e.g., "LeBron James", "Stephen Curry")
3. **Choose statistics** - Select from the menu options:
   - View current season totals
   - View past 5 seasons totals
   - View postseason career totals
   - View regular season career totals
   - View college totals
4. **Continue or exit** - After viewing stats, choose to view different stats, search another player, or quit

### Example Usage

```
Welcome to the NBA Stat Fetcher
Fetching NBA data... (this may take a moment)
--------------------------------------------------
Enter player name (or 'quit' to exit): LeBron James
Player found: LeBron James

Please select from the following options:
1. View current season totals
2. View past 5 seasons totals
3. View postseason career totals
4. View regular season career totals
5. View college totals
6. Search another player
7. Quit program
Enter your choice (1-7): 1
```

## Dependencies

This project uses the following Python packages:

- **nba_api**: For accessing NBA statistics and player data
- **pandas**: Data manipulation (installed automatically with nba_api)
- **requests**: HTTP requests (installed automatically with nba_api)

## Data Source

All basketball statistics are sourced from the NBA's official statistics API through the `nba_api` package.

## Error Handling

- **Player not found**: The program will notify you if a player name isn't found and prompt you to check the spelling
- **Missing package**: If the required `nba_api` package isn't installed, the program will display installation instructions
- **No stats available**: For players without certain types of stats (e.g., no playoff experience), appropriate messages are displayed

## Contributing

Feel free to fork this project and submit pull requests for any improvements or bug fixes.

## License

This project is open source and available under the [MIT License](LICENSE).

## Author

[Your Name]

---

**Note**: This application requires an internet connection to fetch live NBA data. The first time you run it, there may be a brief delay as it connects to the NBA API.