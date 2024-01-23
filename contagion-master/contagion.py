"""Simple grid model of contagion"""

import grid_view
import change_listener
import model
import contagion_stats

import time
import config
import argparse

import logging
logging.basicConfig()
log = logging.getLogger(__name__)
log.setLevel(logging.WARN)


def cli() -> object:
    """Command line interface returns an object with
    an instance variable for each command line argument.
    """
    parser = argparse.ArgumentParser(
        description="Contagion, a simple model of disease spread")
    parser.add_argument("conf", nargs="?",
                        default="contagion.ini")
    return parser.parse_args()


def main():
    """View a simulation of contagion"""
    args = cli()
    config.configure(args.conf)
    n_rows = config.get_int("Grid", "rows")
    n_cols = config.get_int("Grid", "cols")

    population = model.Population(n_rows, n_cols)

    # View of the main model
    view = grid_view.GridView(config.get_int("Grid", "Width"),
                              config.get_int("Grid", "Height"),
                              nrows=n_rows, ncols=n_cols,
                              title="Contagion", autoflush=False)

    # Summary statistics
    stats_view = contagion_stats.Stats(population)

    # Monitor changes to cells ---
    #    - for monitoring progress
    #    - for updating the main view
    monitor = change_listener.ChangeListener()
    # Attach listeners to each cell
    for row in range(n_rows):
        for col in range(n_cols):
            cell_view = grid_view.CellView(row, col, view)
            population.cells[row][col].add_listener(cell_view)  # Graphics
            population.cells[row][col].add_listener(monitor)    # Change tracking
        view.update(rate=5)

    # Initial view, before simulation starts
    view.update()
    time.sleep(1)
    log.info("Seeding")
    population.seed()  # Note this should set change monitor
    view.update()
    time.sleep(1)

    # Evolve until it reaches quiescence
    log.info("Running")
    steps = 0
    epoch = 0
    monitor.set(True)
    while monitor.check():
        monitor.set(False)  # No changes yet in this cycle
        # An 'epoch' is 10 steps.  We stop when an epoch has
        # gone by without a noticeable state change, and we
        # chart each epoch rather than each step
        for _ in range(10):
            steps += 1
            log.debug(f"Step {steps}")
            population.step()
            view.update()
            stats_view.update(day=steps)
            time.sleep(0.1)
        epoch += 1

        # Print stats and update bar graph after each epoch
        stats_view.show(day=steps, epoch=epoch)

    # Simulation is no longer changing.  Leave view open
    # until the user presses enter
    stats_view.show_summary()
    _ = input("Press enter to close")


if __name__ == "__main__":
    main()









