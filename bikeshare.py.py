import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
valid_month = ['january','february', 'march', 'april', 'may', 'june','all']
valid_day = ['all', 'monday', 'tuesday', 'wednesday', 'thursday','friday', 'saturday','sunday']
""" This is code """

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('\n'*3)
    print('*'*52)
    print('*'*52)
    print('*'*52)
    print('*** Hello! Let\'s explore some US bikeshare data! ***')
    print('*'*52)
    print('*'*52)
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    is_valid = False
    while is_valid == False:
        city=input('  SELECTION_1: Would you like to see data for Chicago, New York City, or Washington?')
        if city == 'Chicago' or city == 'New York City' or city == 'Washington':
            is_valid = True
        else:
            print('-'*52)
            print('--> That\'s not a valid City please repeat your entry!')
            print('-'*52)
    # get user input for month (all, january, february, ... , june)
    is_valid = False
    while is_valid == False:
        month=input('\n  SELECTION_2: Please enter a Month (all, january, february,...,june): ')
        if month in valid_month:# Check month in a list of valid entries
            is_valid = True
        else:
            print('-'*52)
            print('-- That\'s not a valid month please repeat your entry! ')
            print('-'*52)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    is_valid = False
    while is_valid == False:
        day=input('\n  SELECTION_3: Please enter a day of the week (all, monday, tuesday,...): ')
        if day in valid_day:#Check if entry is part of the list: valid_day
            is_valid = True
        else:
            print('-'*52)
            print('-- That\'s not a valid day of the week please repeat your entry! ')
            print('-'*52)

    print('-'*52)
    print('-'*52)
    print('Your selection is {}, {}, {}'.format(city, month, day))
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    """-----------Andreas-------------------"""
    """__Loading data with panda__"""
    city_key = city.casefold() # Andreas: Casefold sets City names to all small letters
    filename=CITY_DATA.get(city_key)
    df = pd.read_csv(filename)
    """___Filtering by month and day___"""

    """___Format Start Time___"""
    df['Start Time'] = pd.to_datetime(df['Start Time']) #Format Start Time
    #print(df) #Ausgabe des dataframe
    """___Create Column with Month and weekday___"""
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.weekday_name
    #print() #Ausgabe des dataframe
    #print() #Ausgabe des dataframe
    #print(df) #Ausgabe des dataframe
    """___Filtering by day if selection is not 'all'___"""
    if day != 'all':
        df = df[df['day'] == day.title()] #filter df by day
    """___Filtering by month if selection is not 'all'___"""
    month_index = valid_month.index(month) + 1 # get number of month, add 1 because index starts at 0
    #print ('Month index= {}'.format(month_index))
    if month!= 'all':
        df = df[df['month'] == month_index]
    #print() #Ausgabe des dataframe
    #print() #Ausgabe des dataframe
    #print(df) #Ausgabe des dataframe
    """-----------Andreas-------------------"""
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""
    print('')
    print('-'*52)
    print('-'*52)
    print('--- STAT1: Calculating The Most Frequent Times of Travel...')
    print('-'*52)
    start_time = time.time()

    # display the most common month
    if month != 'all':
        print('')
        print('As there is a filter on month, \'most common month\' is not analysed')
        print('')
    else:
        print('')
        print('The most common month is: ', df['month'].value_counts().idxmax())
        print('')
        print('The Rank of all month is listed:\n ', df['month'].value_counts())
        print('')

    # display the most common day of week
    if day != 'all':
        print('')
        print('As there is a filter on day, \'most common day\' is not analysed')
        print('')
    else:
        #dict_freq = df['day'].value_counts().idxmax()
        #most_comm_day = dict_freq[0]
        print('')
        print('The most common day is: ', df['day'].value_counts().idxmax())
        print('')

    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    print('')
    print('The most common hour is: ', df['hour'].value_counts().idxmax())
    print('')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*52)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('')
    print('-'*52)
    print('-'*52)
    print('--- STAT2: Calculating The Most Popular Stations and Trip...')
    print('-'*52)

    start_time = time.time()

    # display most commonly used start station
    print('The most common start station is: ', df['Start Station'].value_counts().idxmax())
    print('-'*52)
    print('Start Station Analysis:\n\n', df['Start Station'].value_counts())
    print('')
    print('-'*52)
    # display most commonly used end station

    print('The most common End station is: ',df['End Station'].value_counts().idxmax())
    print('-'*52)
    print('-'*52)
    print('End Station Analysis:\n\n',df['End Station'].value_counts())
    print('')
    print('-'*52)


    # display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*52)


def trip_duration_stats(df, city, month, day):
    """Displays statistics on the total and average trip duration."""
    print('')
    print('-'*52)
    print('-'*52)
    print('--- STAT3: Calculating Trip Duration...')
    print('-'*52)
    start_time = time.time()

    # display total travel time
    print('The TOTAL travel time in {} in month: {} on weekday: {} is: {} hours'.format(city, month, day, df['Trip Duration'].sum()/3600))
    print('-'*52)
    print('-'*52)

    # display mean travel time
    print('The MEAN travel time in {} in month: {} on weekday: {} is: {} hours'.format(city, month, day, df['Trip Duration'].mean()/3600))
    print('-'*52)
    print('-'*52)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*52)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""
    print('')
    print('-'*52)
    print('-'*52)
    print('--- STAT4: Calculating User Stats...')
    print('-'*52)
    start_time = time.time()

    # Display counts of user types
    print('Counts of user types:\n\n',df['User Type'].value_counts())
    print('')
    print('-'*52)

    # Display counts of gender
    """ It needs to be checked, whether Gender exists in the database or not. Washington database does not have 'gender'"""
    if 'Gender' in df.index:
        print('Counts of gender:\n\n',df['Gender'].value_counts())
        print('')
        print('-'*52)
    else:
        print('Gender Statistic not available for: ', city)
        print('-'*52)
    if 'Birth Year' in df.index:
        # Display earliest, most recent, and most common year of birth
        print('Earliest year of birth is: ',df['Birth Year'].min())
        print('Most recent year of birth is: ',df['Birth Year'].max())
        print('Most common year of birth is: ',df['Birth Year'].value_counts().idxmax())
        print('-'*52)
        print("\nThis took %s seconds." % (time.time() - start_time))
        print('-'*52)
    else:
        print('Birth Year Statistic not available for: ', city)
        print('-'*52)
def main():
    """-----------Andreas------------------"""
    #city, month, day = get_filters()
    #df = load_data(city, month, day)

    """-----------Andreas------------------"""
    while True:

        city, month, day = get_filters()
        df = load_data(city, month, day)
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df, city, month, day)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break



"""Codebedeutung unklar, deshalb ausgeklammert

if __name__ == "__main__":
	main()


"""
main()
