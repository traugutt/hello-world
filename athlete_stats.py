from isu_scraper import all_skaters

class FigureSkater():

    def __init__(self, name: object) -> str:
            self.name = name
            self.isu_rank = all_skaters[str(name)].get('standing')
            self.standing = all_skaters[str(name)].get('standing')
            self.points = all_skaters[str(name)].get('points')
            self.points_to_beat = all_skaters[str(name)].get('points to beat')

            if self.name not in all_skaters.keys():
                print('This skater is not in ISU rank')
    def all_info(self):
        if int(self.isu_rank) == 1:
            ordinal = 'st'
        elif int(self.isu_rank) == 2:
            ordinal = 'nd'
        elif int(self.isu_rank) == 3:
            ordinal = 'rd'
        else:
            ordinal = 'th'
        print(self.name + ' is currently occupying ' + self.isu_rank + ordinal + ' place in the ISU rank of male skaters with the total of '
              + self.points +' points. \n' + 'He needs to gain ' + str(self.points_to_beat) + ' more points to become first.')


nathan = FigureSkater(name='Nathan CHEN')
shom_shom = FigureSkater(name='Shoma UNO')
yuzu = FigureSkater(name='Yuzuru HANYU')
def check_my_skater():
    user_typed_name = input('Please type the name of the skater in the following format: "Name LASTNAME" \n')
    user_typed_name.strip()
    if user_typed_name not in all_skaters.keys():
        print('Couldn\'t find this skater :(')
        check_my_skater()
    else:
        my_skater = FigureSkater(name=user_typed_name)
        my_skater.all_info()
check_my_skater()