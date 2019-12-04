__author__ = "Matheus Galhani"


def recursive(list_years):
    try:
        year = list_years[0]
        print(f'Você está no ano {year}')
        list_years.__delitem__(0)
        recursive(list_years)
    except IndexError:
        print("Mundo acabou!")


if __name__ == '__main__':
    years = [2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009]
    recursive(years)
