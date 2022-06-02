class Menu:

    def __init__(self, option_dict, start_message=None, end_message=None):
        self.start_message = start_message
        self.end_message = end_message
        self.option_dict = option_dict

    def show_menu(self):
        ''' Displays a menu to the screen '''
        if self.start_message:
            print(self.start_message + '\n')

        for option, description in self.option_dict.items():
            print(f'{option}. {description}')

        if self.end_message:
            print('\n' + self.end_message)

    def get_choice(self):
        '''Gets menu choice from the user and returns it'''
        while True:
            choice = input('Your choice: ')

            if choice in self.option_dict.keys():
                break

            print('Invalid choice')
            continue
        return choice

    def __repr__(self):
        return f'<{self.__class__.__name__} containing {len(self.option_dict)} options>'