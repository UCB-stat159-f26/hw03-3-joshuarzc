# tennis-career

## Overview

`tennis-career` is a Python package for retrieving, cleaning, and visualizing professional tennis career-match data from Tennis Abstract. Given a player name, it resolves the corresponding career data, returns a standardized `pandas.DataFrame`, and produces a scatter plot of the player's age against the age difference with each opponent.

## Installation

## Usage

### Get career-match data

### Create a career-match plot

## Data source

Match records are retrieved at runtime from [Tennis Abstract](https://www.tennisabstract.com/) career JavaScript files. The standardized output contains the match date, tournament, surface, result, opponent, player age, opponent age, and age difference.

Female career files record opponents' dates of birth, from which opponent ages are calculated using match dates. Male career files provide opponent ages directly. Data coverage and availability remain determined by Tennis Abstract.

## Development

### Run tests
