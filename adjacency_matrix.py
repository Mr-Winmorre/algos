class AdjacencyMatrix(object):
    def __init__(self, size):
        self.adj_matrix = []
        for i in range(size):
            self.adj_matrix.append([0 for i in range(size)])
        self.size = size

    # Add Edge
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("Same vertex %d and %d" % (v1, v2))
        self.adj_matrix[v1][v2] = 1
        self.adj_matrix[v2][v1] = 1

    # remove Edge
    def remove_edge(self, v1, v2):
        if self.adj_matrix[v1][v2] == 0:
            print("No edge between %d and %d" % (v1, v2))
            return
        self.adj_matrix[v1][v2] = 0
        self.adj_matrix[v2][v1] = 0

    def __len__(self):
        return self.size

    # Print matrix
    def print_matrix(self):
        for row in self.adj_matrix:
            for val in row:
                print('{:4}'.format(val))

    def print_rows(self):
        for row in self.adj_matrix:
            print(row)

    def show_data(self):
        return self.adj_matrix
