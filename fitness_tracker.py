"""
fitness_tracker.py

Module for tracking individual fitness workout sessions.
This module defines the WorkoutSession by calculating the calroies burned 
based on the duration and intensity of the workout. Then the module summarizes the workout. 

Author: Erika Coreth
Date: January 2026


"""

class WorkoutSession:
    """

    Represents a single workout session performed by a user.

    A WorkoutSession stores basic information about an exercise, including
    the name of the exercise, how long it was performed, and the intensity level.
    It also provides functionality to estimate calories burned and to summarize
    the workout in a user-friendly format.
    
    
    """

def __init__(self, exercise_name, duration, intensity):
    """
    Iinitializes a new WorkoutSession instance.

    Args:
    exercise_name (str): Name of the exercise performed.
    duration (int): Duration of the workout in minutes.
    intensity (str): Intensity level of the workout ("Low", "Medium", or "High").

    
    """
    self.exercise_name = exercise_name
    self.duration = duration
    self.intetnsity = intensity


def calculate_calories(self):
    """
    Calculates the estimated number of calories burned during the workout. 

    Returns:
    int: Estimated calories burned (cal/min) based on duration and intensity level.
    
    """
    intensity_rank = {
        "Low": 5,
        "Medium": 10,
        "High": 15
    }
    calories_per_min = intensity_rank.get(self.intensity, 0)
    return self.duration * calories_per_min


def get_summary(self):

    """
    Generates a formatted summary of the workout session.

    Returns:
    str: A human-readable string describing the workout details.

    
    """
    return (
        f"Exercise: {self.exercise_name}\n"
        f"Duration: {self.duration} minutes \n"
        f"Intensity: {self.intensity}\n"
        f"Estimated Calories Burned: {self.calculate_calories()}"
    )

def update_duration(self, new_duration):

    """
    Updates the duration of the workout session.

    Args:
    new_duration (int): The new duration of the workout in minutes.

    Returns:
    None

    """
    self.duration = new_duration