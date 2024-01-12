
class Printbox:
    @staticmethod
    def print_box(text):
        lines = text.split('\n')
        max_line_length = max(len(line) for line in lines)
        box_width = max_line_length + 4  # Add padding on both sides
        horizontal_line = '+' + '-' * (box_width - 2) + '+'

        print(horizontal_line)
        for line in lines:
            empty_space = ' ' * (max_line_length - len(line))
            print(f'| {line}{empty_space} |')
        print(horizontal_line)
        
    @staticmethod  
    def player_choice():
        choose_player = input()
        if choose_player == "1":
            return 0 #Return the index 0 for the list 
        elif choose_player == "2":
            return 1
        else:
            Printbox.print_box("Please press 1 or 2...")
            return Printbox.player_choice()

