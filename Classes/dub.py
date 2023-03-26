import pandas as pd

class Dub:
    # Constructor
    def __init__(self):
        self._counter = 0
        self._df = pd.read_excel('WarzoneWins.xlsx', engine='openpyxl')

    # Getter for counter
    def getCounter(self):
        return self._counter
    
    # Function that resets the counter
    def resetCounter(self):
        self._counter = 0

    # Function that gets the value of the "wins" column for a specific date  
    def getWins(self, date):
        # check if the date already exists in the DataFrame
        if date in self._df['Date'].values:
            return self._df.loc[self._df['Date'] == date, 'Wins'].values[0]
        else:
            return 0
        
    # Function that increments the variable counter
    def incrementDub(self):
        self._counter += 1

    # Function that writes to an existing excel file the number of wins based on a specific date
    def storeWins(self, wins, date):
        # check if the date already exists in the DataFrame
        if date in self._df['Date'].values:
            # update the "wins" value for the row with the specified date
            self._df.loc[self._df['Date'] == date, 'Wins'] = wins
        else:
            # append a new row with the specified date and "wins" value
            new_row = {'Date': date, 'Wins': wins}
            self._df = self._df.append(new_row, ignore_index=True)

        # write the updated DataFrame back to the Excel file
        self._df.to_excel('WarzoneWins.xlsx', index=False, engine='openpyxl')