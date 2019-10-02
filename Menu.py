class Menu():

    def __init__(self, option_dict, start_message=None, end_message=None):
        self.start_message = start_message
        self.end_message = end_message
        self.option_dict = option_dict

    def show_menu(self):

        if self.start_message:
            print(self.start_message + '\n')

        for option, description in self.option_dict.items():
            print(option + '. ' + description)

        if self.end_message:
            print('\n' + self.end_message)

    def get_choice(self):
        while True:
            choice = input('Your choice: ')
            
            if choice not in self.option_dict.keys():
                print('Invalid choice')
                continue
            else:
                break
            
        return choice