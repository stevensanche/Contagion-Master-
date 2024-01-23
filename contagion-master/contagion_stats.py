"""Track and optionally display statistics about a
contagion model.
"""

import model
import config
import bar_chart

class Stats:
    def __init__(self, population: model.Population):
        self.pop = population
        # Accompanying chart of current cases and total deaths
        chart_width = config.get_int("Chart", "Width")
        chart_height = config.get_int("Chart", "Height")
        self.chart = bar_chart.Chart(chart_width,
                                chart_height,
                                config.get_int("Chart", "Cols"),
                                v_min=0,
                                v_max=config.get_int("Chart", "Max"),
                                title="Current cases, cumulative deaths")
        # Move the chart out from under the main model view
        self.chart.win.master.geometry(f"{chart_width}x{chart_height}-5+0")
        #
        # Summary stats
        self.max_symptomatic = 0
        self.max_period_dead = 0
        self.prior_day_dead = 0
        self.prior_period_dead = 0
        self.max_symptomatic_day = 0
        self.max_deaths_day = 0

    def update(self, day=0):
        current_cases = self.pop.count_in_state(model.Health.symptomatic)
        deaths = self.pop.count_in_state(model.Health.dead)
        new_deaths = deaths - self.prior_day_dead
        if new_deaths > self.max_period_dead:
            self.max_period_dead = new_deaths
            self.max_deaths_day = day
        if current_cases > self.max_symptomatic:
            self.max_symptomatic = current_cases
            self.max_symptomatic_day = day
        self.prior_day_dead = deaths

    def show(self, day: int, epoch: int):
        current_cases = self.pop.count_in_state(model.Health.symptomatic)
        deaths = self.pop.count_in_state(model.Health.dead)
        new_deaths = deaths - self.prior_period_dead
        self.prior_period_dead = deaths

        print(f"Day {day:3}\t{current_cases:4} symptomatic\t{deaths:4}" +
              f" cumulative deaths ({new_deaths:4} this period)")
        self.chart.bar(epoch, current_cases,
                  color=bar_chart.color(250, 200, 250))
        self.chart.bar(epoch, deaths,
                  color=bar_chart.color(0,0,0),frac_width=0.75)

    def show_summary(self):
        print(f"Peak {self.max_symptomatic} symptomatic " +
              f"on day {self.max_symptomatic_day}")
        print(f"Peak {self.max_period_dead} deaths on day {self.max_deaths_day}")




