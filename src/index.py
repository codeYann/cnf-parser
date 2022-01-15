if __name__ == "__main__":
    import Cnf as cnf_parser
    import Analyzer as checker
    import sys

    if len(sys.argv) <= 3:
        if "--check" in sys.argv:
            print(checker.is_formula(sys.argv[1]))
        elif "--parser" in sys.argv:
            print(cnf_parser.to_cnf(sys.argv[1]))
        elif "--help" in sys.argv:
            print("After a formula write a flag\n")
            print(
                "{:<15} {:<10}".format(
                    "--check", "Used to check if a string is a valid formula"
                )
            )
            print(
                "{:<15} {:<10}".format(
                    "--parser", "Parser a formula into a CNF formula"
                )
            )
        else:
            print("Bad option! Use --help to see what you can do")
