from PrintLab.gui import run_gui
from PrintLab.models import create_all


def main():
    create_all()
    run_gui()


if __name__ == "__main__":
    main()
