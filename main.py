"""
@Author: Mohamed Waleed Fathy

@Template: Udacity

@Name of Project: Bike Share Data Analysis App
"""

import time
import pandas as pd


CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    ## Need to remove thhe case sensitivity
    city_inp = input("Please write the name of the city you want to search on: ").lower()
    while True:
        if city_inp == "chicago" or city_inp == "new york city" or city_inp == "washington":
            city = city_inp
            break
        else:
            print("Sorry invalid input")
            city_inp = input("Please rewrite the name of the city you want to search on: ")
            
        
    
    # get user input for month (all, january, february, ... , june)
    month_inp = input("Please write the name of the month you want to search on: ").lower()
    while True:
        if month_inp == "all" or month_inp == "january" or month_inp == "february" or month_inp == "marsh" or month_inp == "april" or month_inp == "may" or month_inp =="june": 
            month = month_inp
            break
        else:
            print("Sorry invalid input")
            month_inp = input("Please rewrite the name of the month you want to search on: ")
    
    # get user input for month (all, january, february, ... , june)
    day_inp = input("Please write the name of the day you want to search on: ").lower()
    while True:
        if day_inp == "all" or day_inp == "sunday" or day_inp == "monday" or day_inp == "tuesday" or day_inp == "wednesday" or day_inp == "thursday" or day_inp == "friday" or day_inp == "saterday":
            day = day_inp
            break
        else:
            print("Sorry invalid input")
            day_inp = input("Please rewrite the name of the day you want to search on: ")
            
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
    
    # loading
    
    df = pd.read_csv(CITY_DATA["new york city"])
    
    # Converting to datetime type
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # Extracting month and day
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    
    # filter by month
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        
    # filter by day
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    # Extracting per hour
    df['hour'] = df['Start Time'].dt.hour


    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    popular_month = df['month'].mode()[0]     
    print('Most Frequent month:', popular_month)

    # display the most common day of week
    popular_day = df['day_of_week'].mode()[0]     
    print('Most Frequent day:', popular_day)

    # display the most common start hour
    popular_hour = df['hour'].mode()[0]     
    print('Most Frequent Start Hour:', popular_hour)



    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start = df['Start Station'].mode()
    print(start)

    # display most commonly used end station
    end = df['End Station'].mode()
    print(end)

    # display most frequent combination of start station and end station trip
    freq = df.groupby(['Start Station','End Station']).size().nlargest(1)
    print(freq)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    print("total travel time ",df["Trip Duration"].sum())
    
    # display mean travel time
    print("mean travel time ",df["Trip Duration"].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print(user_types)

    # Display counts of gender --> In chicago only 
    if "Gender" in df.columns:
        gender = df['Gender'].value_counts()
        print(gender)
    elif "Birth Year" in df.columns:
        birthYear = df['Birth Year'].value_counts()
        print(birthYear)

    # Display earliest, most recent, and most common year of birth
    earliest = df['Birth Year'].min()
    print(earliest)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def display_data(df):
    start_loc = 0
    while True:
        view_data = input("Would you like to view the next 5 rows of individual trip data? Enter yes or no: ").lower()
        if view_data == "yes":
            print(df.iloc[start_loc: start_loc+6])
            start_loc += 5
            continue
        elif view_data == "no":
            print("Thank you for using my app :)")
            break
        else:
            print("Sorry, you should write (yes) or (no) only")
            continue
        

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break

if __name__ == "__main__":
	main()
