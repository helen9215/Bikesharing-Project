import time
import pandas as pd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april','may', 'june','all'] 
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday' , 'All']
       
def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
   
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
      
    while True:
        city = input('Would you like to see data for Chicago, New York, or Washington?\n')
        city = city.lower() 
        if city in CITY_DATA.keys():
            break
        else:
            print('\n Invalid input.')
            continue

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month? January, February, March, May, April, June or all?\n')
        month = month.lower()
        if month in months:
            break
        else:
            print('\n Invalid input.')
            continue
   
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Which day? Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all?\n')
        day = day.lower().title() 
        if day in days:
            break
        else:
            print('\n Invalid input.')
            continue

    print('-'*40)
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
    df = pd.read_csv(CITY_DATA[city])
    
    ## filter by month 
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    if month != 'all':
        month = months.index(month) + 1
        df = df[df['month']== month]
    
     ## filter by day
    df['day'] = pd.to_datetime(df['Start Time']).dt.weekday_name
    if day != 'All':
        df = df[df['day']== day]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]
    print('The most frequent month:{}.'.format(popular_month))
    
    # TO DO: display the most common day of week
    popular_day = df['day'].mode()[0]
    print('The most frequent day:{}.'.format(popular_day))
    
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('The most frequent hour:{}.'.format(popular_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start= df['Start Station'].mode()[0]
    print('The most popular start station:{}.'.format(popular_start))
    
    # TO DO: display most commonly used end station
    popular_end= df['End Station'].mode()[0]
    print('The most popular end station:{}.'.format(popular_end))
    
    # TO DO: display most frequent combination of start station and end station trip
    df['Combined Station'] = df['Start Station'] +'--' + df['End Station']
    popular_combine= df['Combined Station'].mode()[0]
    print('The most frequent combination of start and end station:{}.'.format(popular_combine))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total travel time:{} hour.'.format(round(total_time/360,2)))
     
    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean travel time:{} hour.'.format(round(mean_time/360,2)))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user = df['User Type'].value_counts()
    print('Displaying counts of user types:\n{}\n'.format(user))
    
    # TO DO: Display counts of gender
    if 'gender' in df:
        gender = df['Gender'].value_counts()
        print('Displaying counts of gender:\n{}\n'.format(gender)) 
    else:
        print('Gender information does not exist.\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        birth_early = int(df['Birth Year'].min())
        birth_recent = int(df['Birth Year'].max())
        birth_common = int(df['Birth Year'].mode()[0])
        print('Earliest birth year:{}.\nMost recent birth year:{}.\nMost common birth year:{}.'.format(birth_early,birth_recent, birth_common))
    else:
        print('Birth year information does not exist.\n')
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

