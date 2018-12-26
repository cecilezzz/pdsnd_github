#!/usr/bin/env python
# coding: utf-8

# In[17]:


import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    
    while True:
        city = input('Which city do you want to see? Chicago, New York or Washington? \n> ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Sorry the Input is invailed, please try again')

    # get user input for month (all, january, february, ... , june)
    while True:
        month = input('Which month data do you want to see? all, january, febuary, march, april, may or june? \n> ').lower()
        if month in month:
            break
        else:
            print('Sorry the Input is invailed, please try again')    
    

    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = input('One last thing. Could you type one of the week day you want to analyze?'                   ' You can type \'all\' again to apply no day filter. \n(e.g. all, monday, sunday) \n> ').lower()
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
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    the_most_common_month = df['month'].value_counts().idxmax()
    print("The most common month is :", the_most_common_month)
    # display the most common day of week
    the_most_common_day_of_week = df['day_of_week'].value_counts().idxmax()
    print("The most common day of week is :", the_most_common_day_of_week)

    # display the most common start hour
    the_most_common_start_hour = df['hour'].value_counts().idxmax()
    print("The most common start hour is :", the_most_common_start_hour)

    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    most_common_start_station = df['Start Station'].value_counts().idxmax()
    print("The most common start station :", most_common_start_station)

    # display most commonly used end station
    most_common_end_station = df['End Station'].value_counts().idxmax()
    print("The most common end station :", most_common_end_station)

    # display most frequent combination of start station and end station trip
    df['Start_End Station'] = df['Start Station'] + [' _/_ '] + df['End Station'] 
    print("The most common station combination is :", df['Start_End Station'].value_counts().idxmax())
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print("Total travel time is :", total_travel_time)

    # display mean travel time
    mean_travel = df['Trip Duration'].mean()
    print("Mean travel time :", mean_travel)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    count_user_types = df['User Type'].value_counts()
    print("The user types are:", count_user_types)
    # Display counts of gender
    if city != 'washington':
        
        count_user_gender = df['Gender'].value_counts()
        print("The gender counts are:", count_user_gender)
    else:
        print('Gender not existing for washington')

        
    if city != 'washington':
        
        # Display earliest, most recent, and most common year of birth
        the_most_common_year_of_birth = df['Birth Year'].value_counts().idxmax()
        print("The most common year of birth is:", the_most_common_year_of_birth)
        most_recent = df['Birth Year'].max()
        print("The most recent birth year is:", most_recent)
        earliest_birth_year = df['Birth Year'].min()
        print("The earliest birth year is:", earliest_birth_year)
        
    else:
        print('Birth Year not existing for washington')

    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    print('\nDo you want to see the first 5 Data rows?\n')
    anwser = input().lower()
    if anwser == 'yes':
        print(df.head())
    else:
        print('thank you for your time')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df,city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()


# In[ ]:




