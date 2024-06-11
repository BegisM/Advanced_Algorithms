from utils.bipartite import seating_scheme
from utils.graph import draw_graph

def main():
    guests = ["Anna", "Boris", "Viktor"]
    dislikes = [("Anna", "Boris"), ("Anna", "Viktor"), ("Boris", "Viktor")]

    res = seating_scheme(guests, dislikes)
    print(res)
    draw_graph(guests, dislikes, example_number=1)

    guests = ["Anna", "Boris", "Viktor", "Gleb"]
    dislikes = [("Anna", "Boris"), ("Anna", "Viktor"), ("Boris", "Gleb"), ("Viktor", "Gleb")]

    res = seating_scheme(guests, dislikes)
    print(res)
    draw_graph(guests, dislikes, example_number=2)

if __name__ == "__main__":
    main()
