from data import get_info, save_info, COMPOUNDS, represent


def main():
    while True:
        print("\nChoose thing you want me to do : ")
        print("""
        1 : Populate DB 
        2 : Show me the data
        0 : Exit
            """)
        choice = input("\nEnter your choice : ")

        if choice == '1':
            save_info(COMPOUNDS)
        elif choice == '2':
            represent()
        elif choice == '0':
            exit()


if __name__ == "__main__":
    main()
